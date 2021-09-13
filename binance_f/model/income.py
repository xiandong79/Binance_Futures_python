class Income:

    def __init__(self):
        self.tranId = ""
        self.tradeId = ""
        self.symbol = ""
        self.incomeType = ""
        self.income = 0.0
        self.asset = ""
        self.time = 0
    
    @staticmethod
    def json_parse(json_data):
        result = Income()
        result.tranId = json_data.get_string("tranId")
        result.tradeId = json_data.get_string("tradeId")
        result.symbol = json_data.get_string("symbol")
        result.incomeType = json_data.get_string("incomeType")
        result.income = json_data.get_float("income")
        result.asset = json_data.get_string("asset")
        result.time = json_data.get_int("time")

        return result
