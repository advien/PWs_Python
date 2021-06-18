#5.

# ОБРАТИТЬСЯ К ЗАДАНИЮ №4 ЗА:
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например, словарь.


class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

#'Невозможно добавить товар на склад'
class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f'Impossible to add the good in storage: \n {text}'

#Ошибка прередачи оборудования
class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f'Error of the device transfer: \n {text}'


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} - non-office equipment!")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Unacceptable item! - '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"{item}  is already for {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

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

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


# ДЛЯ ВСТАВКИ СКРИПТА: классы оргтехники (через аргументы)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("Epson", "Fs325"))
    storage.add(Scanner("OKI", "53BL-AD"))
    storage.add(Xerox("Xerox", "XP-730"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print('Transfer one device')
    storage.transfer(last_idx, 'PR Department')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print('Delete one device')
    del storage[last_idx]
    print(storage)
