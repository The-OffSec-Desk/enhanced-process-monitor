"""
Process data model with real-time psutil integration
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import psutil


@dataclass
class ProcessModel:
    """Model representing a system process"""
    pid: int
    user: str
    cpu: float
    mem: float
    vsz: int
    rss: int
    status: str
    threads: int
    command: str
    ppid: int
    created: str
    cpu_time_user: float
    cpu_time_sys: float
    cwd: str
    open_files: int
    network_conns: int
    priority: int


def format_bytes(bytes_value):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f}{unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f}PB"


def get_process_info(proc: psutil.Process) -> Optional[ProcessModel]:
    """Extract process information safely from psutil Process"""
    try:
        with proc.oneshot():
            mem_info = proc.memory_info()
            cpu_times = proc.cpu_times()
            
            # Get command line
            try:
                cmdline = proc.cmdline()
                command = ' '.join(cmdline) if cmdline else proc.name()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                command = f"[{proc.name()}]"
            
            # Get working directory
            try:
                cwd = proc.cwd()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                cwd = "N/A"
            
            # Get open files count
            try:
                open_files = len(proc.open_files())
            except (psutil.AccessDenied, psutil.ZombieProcess):
                open_files = 0
            
            # Get network connections count
            try:
                network_conns = len(proc.connections())
            except (psutil.AccessDenied, psutil.ZombieProcess):
                network_conns = 0
            
            # Get username
            try:
                username = proc.username()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                username = "N/A"
            
            # Get parent PID
            try:
                ppid = proc.ppid()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                ppid = 0
            
            # Get number of threads
            try:
                num_threads = proc.num_threads()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                num_threads = 0
            
            # Format creation time
            try:
                create_time = datetime.fromtimestamp(proc.create_time()).strftime('%Y-%m-%d %H:%M:%S')
            except (psutil.AccessDenied, psutil.ZombieProcess, OSError):
                create_time = "N/A"
            
            # Get priority/nice value
            try:
                priority = proc.nice()
            except (psutil.AccessDenied, psutil.ZombieProcess):
                priority = 0
            
            return ProcessModel(
                pid=proc.pid,
                user=username,
                cpu=proc.cpu_percent(),
                mem=proc.memory_percent(),
                vsz=mem_info.vms,
                rss=mem_info.rss,
                status=proc.status(),
                threads=num_threads,
                command=command[:500],  # Limit command length
                ppid=ppid,
                created=create_time,
                cpu_time_user=cpu_times.user,
                cpu_time_sys=cpu_times.system,
                cwd=cwd,
                open_files=open_files,
                network_conns=network_conns,
                priority=priority
            )
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return None


def get_real_processes() -> List[ProcessModel]:
    """Get real process data from the system using psutil"""
    processes = []
    
    for proc in psutil.process_iter():
        info = get_process_info(proc)
        if info:
            processes.append(info)
    
    return processes


def get_system_stats():
    """Get overall system statistics"""
    cpu_percent = psutil.cpu_percent(interval=0.1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        'cpu_percent': cpu_percent,
        'mem_percent': mem.percent,
        'mem_used': mem.used,
        'mem_total': mem.total,
        'disk_percent': disk.percent,
        'disk_used': disk.used,
        'disk_total': disk.total,
    }


def get_network_connections():
    """Get all network connections"""
    connections = []
    
    try:
        for conn in psutil.net_connections(kind='inet'):
            try:
                # Get process name if PID exists
                proc_name = "N/A"
                if conn.pid:
                    try:
                        proc = psutil.Process(conn.pid)
                        proc_name = proc.name()
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass
                
                # Format addresses
                local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                
                connections.append({
                    'pid': conn.pid or 0,
                    'process': proc_name,
                    'protocol': 'TCP' if conn.type == 1 else 'UDP',
                    'local': local_addr,
                    'remote': remote_addr,
                    'status': conn.status
                })
            except Exception:
                continue
    except (psutil.AccessDenied, Exception):
        pass
    
    return connections


def build_process_tree(processes: List[ProcessModel], max_depth: int = 10):
    """Build a hierarchical process tree"""
    # Create a dict for quick lookup
    proc_dict = {p.pid: p for p in processes}
    
    # Find root processes (typically init/systemd with PID 1 or processes with PPID 0)
    roots = [p for p in processes if p.ppid == 0 or p.pid == 1]
    
    def get_children(parent_pid, depth=0):
        """Recursively get children of a process"""
        if depth > max_depth:
            return []
        
        children = []
        for proc in processes:
            if proc.ppid == parent_pid:
                children.append({
                    'process': proc,
                    'children': get_children(proc.pid, depth + 1),
                    'depth': depth
                })
        
        # Sort by CPU usage
        children.sort(key=lambda x: x['process'].cpu, reverse=True)
        return children
    
    tree = []
    for root in roots:
        tree.append({
            'process': root,
            'children': get_children(root.pid),
            'depth': 0
        })
    
    return tree


# Backward compatibility - use real processes by default
def get_sample_processes() -> List[ProcessModel]:
    """Get real process data (replaces old sample data)"""
    return get_real_processes()