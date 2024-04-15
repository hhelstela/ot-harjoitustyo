```mermaid
 classDiagram
    Index --> Login
    Index --> GUI
    GUI --> TaskService
    TaskService --> TaskRepository
    TaskService --> UserRepository
```