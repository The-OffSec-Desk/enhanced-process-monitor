# ELPM Architecture Documentation

## Application Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                         ELPM Main Window                            │
│                      (gui/main_window.py)                           │
├─────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                       Top Bar Widget                          │  │
│  │                   (gui/widgets/top_bar.py)                    │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │  [Logo] ELPM v1.0  |  [Search Bar]  |  [Refresh] [Settings]   │  │
│  └───────────────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    Tab Navigation Bar                         │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ [Processes] [Process Tree] [Network] [Graphs] [History]       │  │
│  └───────────────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                                                               │  │
│  │                    Content Area                               │  │
│  │                (QTabWidget - Current View)                    │  │
│  │                                                               │  │
│  │  ┌─────────────────────────────────────────────────────┐      │  │
│  │  │  Current Tab View (e.g., ProcessesView)             │      │  │
│  │  │  - Processes: Table + Details Panel                 │      │  │
│  │  │  - Graphs: CPU + Memory Charts                      │      │  │
│  │  │  - Others: Placeholder                              │      │  │
│  │  └─────────────────────────────────────────────────────┘      │  │
│  │                                                               │  │
│  └───────────────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                     Status Bar Widget                         │  │
│  │                  (gui/widgets/status_bar.py)                  │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │  CPU: 45.2% | Memory: 62.4% | Disk: 78.3% | ... | 14:32:45    │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

## Processes View Layout

```
┌───────────────────────────────────────────────────────────────────────┐
│                         Processes View                                │
│                  (gui/views/processes_view.py)                        │
├───────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  Control Bar                                                    │  │
│  │  [Sort: CPU%] [☑ Root only] [☑ Hide kernel] [☑ Auto-refresh]    │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────┬──────────────────────────────────┐  │
│  │   Process Table (70%)        │  Process Details Panel (30%)     │  │
│  ├──────────────────────────────┼──────────────────────────────────┤  │
│  │ PID  User   CPU%  MEM%  ...  │  Process Information             │  │
│  │ ─────────────────────────────│  ───────────────────────         │  │
│  │ 1    root   0.1   0.3   ...  │  PID: 1247                       │  │
│  │ 1247 root   85.4  12.5  ...  │  Name: suspicious-miner          │  │
│  │ 892  root   2.3   1.8   ...  │  Status: [Running]               │  │
│  │ 1523 user   45.2  8.7   ...  │  User: root                      │  │
│  │ 2341 user   0.5   2.1   ...  │                                  │  │
│  │ 3456 root   72.8  15.3  ...  │  Resource Usage                  │  │
│  │ ...                           │  ────────────────               │  │
│  │                               │  CPU: 85.4% [████████░]         │  │
│  │ [22 processes total]          │  Memory: 12.5% [███░░░]         │  │
│  │                               │  Threads: 8                     │  │
│  │                               │                                 │  │
│  │                               │  Command                        │  │
│  │                               │  ────────────────               │  │
│  │                               │  /usr/bin/suspicious-minr       │  │
│  │                               │  --pool=malicious.com           │  │
│  │                               │                                 │  │
│  │                               │  ┌───────────────────────────┐  │  │
│  │                               │  │ [SIGTERM (15)]            │  │  │
│  │                               │  │ [SIGKILL (9)]             │  │  │
│  │                               │  │ [SIGSTOP (19)]            │  │  │
│  │                               │  │ [SIGCONT (18)]            │  │  │
│  │                               │  └───────────────────────────┘  │  │
│  └──────────────────────────────┴──────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────┘
```

## Graphs View Layout

```
┌───────────────────────────────────────────────────────────────────────┐
│                           Graphs View                                 │
│                    (gui/views/graphs_view.py)                         │
├───────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  CPU Usage History (60 seconds)               Current: 45.2%    │  │
│  ├─────────────────────────────────────────────────────────────────┤  │
│  │ 100% ┤                                                          │  │
│  │  75% ┤         ╱╲    ╱╲                                         │  │
│  │  50% ┤    ╱╲  ╱  ╲  ╱  ╲   ╱╲                                   │  │
│  │  25% ┤   ╱  ╲╱    ╲╱    ╲╱  ╲                                   │  │
│  │   0% ┤──────────────────────────────────────                    │  │
│  │      └──┬─────┬─────┬─────┬─────┬─────┬──                       │  │
│  │       -60s  -45s  -30s  -15s   -5s    0s                        │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  Memory Usage History (60 seconds)   Current: 62.4% (10GB/16GB) │  │
│  ├─────────────────────────────────────────────────────────────────┤  │
│  │ 100% ┤                                                          │  │
│  │  75% ┤                                                          │  │
│  │  50% ┤  ╱─╲  ╱─╲  ╱─╲  ╱─╲  ╱─╲                                 │  │
│  │  25% ┤ ╱   ╲╱   ╲╱   ╲╱   ╲╱   ╲                                │  │
│  │   0% ┤──────────────────────────────────────                    │  │
│  │      └──┬─────┬─────┬─────┬─────┬─────┬──                       │  │
│  │       -60s  -45s  -30s  -15s   -5s    0s                        │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  Statistics                                                     │  │
│  ├─────────────────────────────────────────────────────────────────┤  │
│  │  CPU:  Avg: 45.2%  │  Max: 75.8%  │  Min: 28.4%                 │  │
│  │  Mem:  Avg: 62.1%  │  Max: 68.3%  │  Min: 55.7%                 │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────┘
```

## Class Hierarchy

```
MainWindow (QMainWindow)
├── TopBarWidget (QWidget)
│   ├── Logo (QLabel with gradient)
│   ├── SearchBar (QLineEdit)
│   └── ControlButtons (QPushButton × 4)
│
├── TabWidget (QTabWidget)
│   ├── ProcessesView (QWidget)
│   │   ├── ControlBar (QFrame)
│   │   │   ├── SortComboBox (QComboBox)
│   │   │   └── FilterCheckboxes (QCheckBox × 3)
│   │   ├── ProcessTable (QTableWidget)
│   │   └── DetailsPanel (QFrame)
│   │       ├── InfoSections (QLabel groups)
│   │       └── SignalButtons (QPushButton × 4)
│   │
│   ├── GraphsView (QWidget)
│   │   ├── CPUGraph (GraphWidget)
│   │   ├── MemoryGraph (GraphWidget)
│   │   └── StatsPanel (QFrame)
│   │
│   └── PlaceholderView (QWidget) × 3
│       └── IconLabel (QLabel)
│
└── StatusBarWidget (QWidget)
    ├── SystemStats (QLabel × 3)
    ├── ProcessCount (QLabel)
    └── TimeDisplay (QLabel)
```

## Data Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Data Flow Diagram                          │
└─────────────────────────────────────────────────────────────────────┘

1. Application Startup
   ────────────────────
   elpm_main.py
        │
        ├── Create QApplication
        │
        └── Create MainWindow
                 │
                 ├── Initialize UI
                 │    ├── Create TopBar
                 │    ├── Create TabWidget
                 │    │    ├── Create ProcessesView
                 │    │    ├── Create GraphsView
                 │    │    └── Create PlaceholderViews
                 │    └── Create StatusBar
                 │
                 └── Start Timers
                      ├── Main Refresh Timer (2s)
                      ├── Graph Update Timer (2s)
                      └── Status Update Timer (1s)

2. Data Loading
   ────────────
   models/process_model.py
        │
        └── get_sample_processes()
                 │
                 └── Returns List[Process]
                          │
                          └── ProcessesView.processes

3. Update Cycle (every 2 seconds)
   ────────────────────────────────
   Timer fires
        │
        ├── ProcessesView.refresh_data()
        │    ├── Filter processes by search query
        │    ├── Apply filters (root only, hide kernel)
        │    ├── Sort by selected criteria
        │    ├── Update table rows
        │    └── Update selected process details
        │
        ├── GraphsView.update_graphs()
        │    ├── Generate new data point
        │    ├── Add to data queue (60 points max)
        │    ├── Trigger repaint
        │    └── Update statistics
        │
        └── StatusBar.update_stats()
             ├── Update CPU percentage
             ├── Update memory percentage
             ├── Update disk usage
             └── Update time display

4. User Interaction
   ────────────────
   User Action
        │
        ├── Click Process Row
        │    └── on_process_selected()
        │         └── update_details_panel()
        │
        ├── Type in Search
        │    └── on_search_changed()
        │         └── filter_processes()
        │              └── populate_table()
        │
        ├── Change Sort
        │    └── on_sort_changed()
        │         └── sort_processes()
        │              └── populate_table()
        │
        └── Toggle Filter
             └── on_filter_changed()
                  └── filter_processes()
                       └── populate_table()
```

## Threading Model

```
Main Thread (GUI Thread)
├── Event Loop (QApplication.exec())
│   ├── UI Updates
│   ├── User Input Handling
│   └── Timer Events
│
└── Timers (QTimer)
    ├── Main Refresh Timer (2000ms)
    │   └── Calls: refresh_data()
    ├── Graph Update Timer (2000ms)
    │   └── Calls: update_graphs()
    └── Status Update Timer (1000ms)
        └── Calls: update_stats()

Note: Currently single-threaded
Future: Add QThread for process data collection
```

## Signal/Slot Connections

```
TopBarWidget
├── search_changed (Signal)
│   └── → MainWindow.on_global_search()
│        └── → ProcessesView.filter_by_search()
│
└── refresh_clicked (Signal)
     └── → MainWindow.refresh_all_views()

ProcessesView
├── process_table.itemSelectionChanged (Signal)
│   └── → on_process_selected()
│        └── update_details_panel()
│
├── sort_combo.currentTextChanged (Signal)
│   └── → on_sort_changed()
│        └── sort_and_update()
│
└── filter_checkboxes.stateChanged (Signal)
    └── → on_filter_changed()
         └── filter_and_update()

MainWindow.refresh_timer.timeout (Signal)
└── → refresh_all_data()
     ├── → ProcessesView.refresh()
     └── → GraphsView.update()

MainWindow.status_timer.timeout (Signal)
└── → StatusBar.update_stats()
```

## File Dependencies

```
elpm_main.py
└── gui/main_window.py
    ├── gui/styles.py
    ├── gui/widgets/top_bar.py
    ├── gui/widgets/status_bar.py
    ├── gui/views/processes_view.py
    │   ├── gui/styles.py
    │   └── models/process_model.py
    ├── gui/views/graphs_view.py
    │   └── gui/styles.py
    └── gui/views/placeholder_view.py
```

## Memory Layout

```
MainWindow Instance
├── Top Bar (~50 KB)
│   ├── Widgets (buttons, search) ~10 KB
│   └── Pixmaps (logo gradient) ~40 KB
│
├── Tab Widget (~5 MB)
│   ├── ProcessesView (~3 MB)
│   │   ├── Process Table (~2 MB)
│   │   │   ├── 22 rows × 9 columns
│   │   │   └── QTableWidgetItems
│   │   └── Details Panel (~1 MB)
│   │       └── Multiple QLabels
│   │
│   ├── GraphsView (~2 MB)
│   │   ├── CPU Graph Data (60 points) ~5 KB
│   │   ├── Memory Graph Data (60 points) ~5 KB
│   │   └── Graph Widgets ~2 MB
│   │
│   └── Placeholder Views (~50 KB each)
│
├── Status Bar (~20 KB)
│   └── Status Labels
│
└── Timers (~5 KB)
    └── QTimer instances

Total: ~5-10 MB (typical)
Peak: ~20 MB (with large process lists)
```

## Customization Points

```
Application Customization Points
│
├── Colors & Theme
│   └── gui/styles.py
│       └── MAIN_STYLES (string)
│           ├── Background colors (#1a1a1a, #2d2d2d)
│           ├── Accent colors (#00d4ff, #ff6b6b)
│           └── Text colors (#e0e0e0, #a0a0a0)
│
├── Refresh Rates
│   └── gui/main_window.py
│       └── init_ui()
│           ├── self.refresh_timer.setInterval(2000)  # Main refresh
│           └── self.status_timer.setInterval(1000)   # Status bar
│
├── Data Source
│   └── models/process_model.py
│       └── get_sample_processes()
│           └── Replace with psutil integration
│
├── Graph Settings
│   └── gui/views/graphs_view.py
│       └── GraphWidget.__init__()
│           ├── data_points maxlen (60)
│           └── Graph dimensions
│
└── Window Configuration
    └── gui/main_window.py
        └── __init__()
            ├── setGeometry(100, 100, 1400, 800)
            └── setWindowTitle("ELPM - Enhanced Linux Process Monitor")
```

## Performance Optimization Points

```
Optimization Opportunities
│
├── Table Updates
│   └── gui/views/processes_view.py
│       └── populate_table()
│           ├── Current: Full table rebuild
│           └── Optimize: Update only changed rows
│
├── Graph Rendering
│   └── gui/views/graphs_view.py
│       └── GraphWidget.paintEvent()
│           ├── Current: Full repaint
│           └── Optimize: Cached pixmap for grid
│
├── Data Collection
│   └── models/process_model.py
│       └── get_sample_processes()
│           ├── Current: Generate on every call
│           └── Optimize: Cache and update incrementally
│
└── Timer Management
    └── gui/main_window.py
        └── Multiple timers
            ├── Current: Separate timers (2s, 1s)
            └── Optimize: Single timer with counters
```

---

**Last Updated**: 10-15-2025
**Version**: 1.0.0
