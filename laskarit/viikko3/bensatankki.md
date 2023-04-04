sequenceDiagram
    main->>Machine: init
    Machine->>FuelTank: init
    Machine->>FuelTank: tank.fill(40)
    Machine->>Engine: init(self.__tank)
    Machine-->>main: 
    main->>Machine: drive
    Machine->>Engine: self.__engine.start()
    Engine->>FuelTank: self._fuel_tank.consume(5)
    Machine->>Engine: self.__engine.is_running()
    Engine->>Machine: True
    Machine->>Engine: self._engine.use_energy()
    Engine->>FuelTank: self._fuel_tank.consume(10)
    Engine->>Machine: True
    Machine->>Engine: self._engine.use_energy()
    Engine->>FuelTank: self._fuel_tank.consume(10)
    Machine->>Engine: self._engine.use_energy()
    Engine->>Machine: True
    Engine->>FuelTank: self._fuel_tank.consume(10)
    Machine->>Engine: self._engine.use_energy()
    Engine->>Machine: True
    Engine->>FuelTank: self._fuel_tank.consume(10)
    Machine->>Engine: self._engine.use_energy()
    Engine->>Machine: False
    Machine-->>main: 
