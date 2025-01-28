from common import *
import random
import json

WAREHOUSECODES = [ "D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D50","D51","D12","D13","D99","D14","D60" ]
PRODUCTCODES = [ "33008","33009","33010","33011","33012","33013","33014","2605","31620","33015","33016","33017","33018","33019","33020","33021","33022","33023","33024","33025","33026","33027","33028","33029","33030","33031","33032","33033","33034","33035","33036","33037","33038","33039","33040","33041","33042","33043","33044","33045","33046","33047","33048","33049","33050","33051","33052","33053","33054","33055" ]

class TestPlankton():

    def PutProductStock(self) -> None:
        self.PrintTitle("Test /plankton/api/productstock")
        data = []

        # Product 1
        p = {}
        data.append(p)
        p["productCode"] = PRODUCTCODES[0]
        p["stock"] = []

        s = {}
        s["warehouseCode"] = WAREHOUSECODES[0]
        s["stockCount"] = random.randint(0, 100)
        s["stockIndication"] = ""
        p["stock"].append(s)

        s = {}
        s["warehouseCode"] = WAREHOUSECODES[1]
        s["stockCount"] = random.randint(0, 100)
        s["stockIndication"] = ""
        p["stock"].append(s)

        # Product 2
        p = {}
        data.append(p)
        p["productCode"] = PRODUCTCODES[2]
        p["stock"] = []

        s = {}
        s["warehouseCode"] = WAREHOUSECODES[0]
        s["stockCount"] = random.randint(0, 100)
        s["stockIndication"] = ""
        p["stock"].append(s)

        s = {}
        s["warehouseCode"] = WAREHOUSECODES[1]
        s["stockCount"] = random.randint(0, 100)
        s["stockIndication"] = ""
        p["stock"].append(s)

        j = json.dumps(data)
        print(f"{dim}{j}{reset}")

        statuscode, timetaken, result = fire_put_request("productstock", j)
        self.HandleResult(statuscode, timetaken, result)


    def PrintTitle(self, title: str) -> None:
        print(f"{bold}{yellow}------ {title} ------{reset}")

    def HandleResult(self, statuscode: int, timetaken: float, result: str) -> None:
        if statuscode != 200:
            print(f"{red}Failed{reset}")
            print(result)
            if result is not None and result != "":
                err = json.loads(result)
                print(f"{red}{err['title']}{reset}")
                print(f"Status: {red}{err['status']}{reset}")
                if "detail" in err:
                    print(f"Detail: {dim}{err['detail']}{reset}")
            else:
                print(f"{red}No error details available{reset}")
        else:
            print(f"{green}Success{reset}")
            print(f"API call took {yellow}{timetaken:.03f}{reset} seconds")

    def CheckConnection(self) -> None:
        self.PrintTitle("Test Connection")
        statuscode, timetaken, result = fire_get_request("")
        data = json.loads(result)

        print(f"Status: {statuscode}")
        print(data["message"])
        print(f"API Key Valid: {data['isValidApiKey']}")


if __name__ == '__main__':
    random.seed()
    t = TestPlankton()

    t.CheckConnection()
    t.PutProductStock()

