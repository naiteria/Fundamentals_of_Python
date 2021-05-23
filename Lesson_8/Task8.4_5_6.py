class QuantityNotNumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    warehouse_quantity = 9
    total_quantity = 0

    def __init__(self):
        self.equipment_list = []

    def equipment_placement(self, equipment):
        try:
            if isinstance(OfficeEquipment.total_quantity(equipment), str):
                raise QuantityNotNumberException('Quantity is not number')
            elif (self.total_quantity + OfficeEquipment.total_quantity(equipment)) <= \
                    self.warehouse_quantity:
                self.total_quantity += OfficeEquipment.total_quantity(equipment)
                self.equipment_list.append([equipment])
            else:
                print(f"\nPresent warehouse capacity is {self.total_quantity} out of "
                      f"{self.warehouse_quantity} pcs! Warehouse can't place another "
                      f"{OfficeEquipment.total_quantity(equipment)} pcs!")
        except QuantityNotNumberException:
            print('\nPlease enter quantity in digits only!')

    def equipment_extraction(self, equipment):
        if [equipment] in self.equipment_list:
            index = self.equipment_list.index([equipment])
            self.total_quantity -= OfficeEquipment.total_quantity(equipment)
            self.equipment_list.pop(index)
            return f'\nExtraction of {[equipment]} to Sales department.'

    def __repr__(self):
        return_str = '\n'.join([str(user_list) for user_list in self.equipment_list])
        return f'\nWarehouse contains:\n{str(return_str)}.\n' \
               f'Warehouse capacity is {self.total_quantity} out of {self.warehouse_quantity}'


class OfficeEquipment:
    def __init__(self, company, model, year, quantity):
        self.company = company
        self.model = model
        self.year = year
        self.quantity = quantity
        self.group = self.__class__.__name__

    def total_quantity(self):
        return self.quantity

    def __repr__(self):
        return f'{self.group}: {self.company} {self.model}, {self.year}, {self.quantity} pcs'


class Printer(OfficeEquipment):
    def __init__(self, company, model, series, year, quantity):
        super().__init__(company, model, year, quantity)
        self.series = series

    def __repr__(self):
        return f'{self.group}: {self.company} {self.model} {self.series}, {self.year}, ' \
               f'{self.quantity} pcs'


class Scanner(OfficeEquipment):
    def __init__(self, company, model, year, resolution, scan_speed, quantity):
        super().__init__(company, model, year, quantity)
        self.resolution = resolution
        self.scan_speed = scan_speed

    def __repr__(self):
        return f'{self.group}: {self.company} {self.model}, {self.year}, ' \
               f'{self.resolution}, {self.scan_speed}, {self.quantity} pcs'


class Xerox(OfficeEquipment):
    def __init__(self, company, model, year, quantity):
        super().__init__(company, model, year, quantity)


company_warehouse = Warehouse()

scanner1 = Scanner('Brother', 'DS-640', 2019, '1200х1200 dpi', '15 ppm', 2)
company_warehouse.equipment_placement(scanner1)

printer1 = Printer('Samsung', 'ProXpress', 'SL-M4020ND', 2012, 5)
company_warehouse.equipment_placement(printer1)

xerox1 = Xerox('Phaser', '3300MFP', 2020, 2)
company_warehouse.equipment_placement(xerox1)

print(company_warehouse)

print(company_warehouse.equipment_extraction(scanner1))

print(company_warehouse)
