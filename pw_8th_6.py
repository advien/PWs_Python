#6.

# ДЛЯ ВСТАВКИ СКРИПТА: о AddStorageError(StorageError) и TransferStorageError(StorageError) из задания №5

AddStorageError = AcceptStorageError

class ValidateEquipmentError(AppError):
    pass

class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, equipments):    #попытка добавить на склад не оргтехнику
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorageError(f'U try to add non-office equipment!')

        self.__storage.extend(equipments)

    def transfer(self, idx: int, department: str):    #недопустимая тип техники
        if not isinstance(idx, int):
            raise TransferStorageError(f"Unacceptable item! - '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"{item} is already for {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):      #доступно на складе
        return f"On the storage: {len(self.__storage)} item(-s)"

# ДЛЯ ВСТАВКИ СКРИПТА: class OfficeEquipment

# ДЛЯ ВСТАВКИ СКРИПТА: классы оргтехники (через кварги)

# ДЛЯ ВСТАВКИ СКРИПТА: о передаче устройства другому отделу из задания №5