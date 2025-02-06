# billu
A step though modeling style

```mermaid
graph LR
    ModA[Agents] --> Mod(Model) --> Sim(Simulation)
    ModSpace[Space] --> Mod(Model)
    ModRules[Rules] --> Sim(Simulation)
    Param[Parameters] --> Sim(Simulation)
    Sim[Simulation] --> Data[Database]
    Data[Database] --> G[Visualization]