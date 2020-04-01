import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer, Double
from soaplib.core.server import wsgi

class CalculatorService(DefinitionBase):
    @soap(Double,Double,_returns=Double)
    def add(self,value1,value2):
        return value1 + value2

    @soap(Double,Double,_returns=Double)
    def sub(self,value1,value2):
        return value1 - value2

    @soap(Double,Double,_returns=Double)
    def mul(self,value1,value2):
        return value1 * value2

    @soap(Double,Double,_returns=Double)
    def div(self,value1,value2):
        return value1 / value2

if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        soap_application = soaplib.core.Application([CalculatorService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 8000, wsgi_application)
        server.serve_forever()
    except ImportError:
        print('Error: example server code requires Python >= 2.5')
