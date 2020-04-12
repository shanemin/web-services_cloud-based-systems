package tns;

public class ApplicationProxy implements tns.Application_PortType {
  private String _endpoint = null;
  private tns.Application_PortType application_PortType = null;
  
  public ApplicationProxy() {
    _initApplicationProxy();
  }
  
  public ApplicationProxy(String endpoint) {
    _endpoint = endpoint;
    _initApplicationProxy();
  }
  
  private void _initApplicationProxy() {
    try {
      application_PortType = (new tns.Application_ServiceLocator()).getApplication();
      if (application_PortType != null) {
        if (_endpoint != null)
          ((javax.xml.rpc.Stub)application_PortType)._setProperty("javax.xml.rpc.service.endpoint.address", _endpoint);
        else
          _endpoint = (String)((javax.xml.rpc.Stub)application_PortType)._getProperty("javax.xml.rpc.service.endpoint.address");
      }
      
    }
    catch (javax.xml.rpc.ServiceException serviceException) {}
  }
  
  public String getEndpoint() {
    return _endpoint;
  }
  
  public void setEndpoint(String endpoint) {
    _endpoint = endpoint;
    if (application_PortType != null)
      ((javax.xml.rpc.Stub)application_PortType)._setProperty("javax.xml.rpc.service.endpoint.address", _endpoint);
    
  }
  
  public tns.Application_PortType getApplication_PortType() {
    if (application_PortType == null)
      _initApplicationProxy();
    return application_PortType;
  }
  
  public java.lang.Double add(java.lang.Double value1, java.lang.Double value2) throws java.rmi.RemoteException{
    if (application_PortType == null)
      _initApplicationProxy();
    return application_PortType.add(value1, value2);
  }
  
  public java.lang.Double div(java.lang.Double value1, java.lang.Double value2) throws java.rmi.RemoteException{
    if (application_PortType == null)
      _initApplicationProxy();
    return application_PortType.div(value1, value2);
  }
  
  public java.lang.Double mul(java.lang.Double value1, java.lang.Double value2) throws java.rmi.RemoteException{
    if (application_PortType == null)
      _initApplicationProxy();
    return application_PortType.mul(value1, value2);
  }
  
  public java.lang.Double sub(java.lang.Double value1, java.lang.Double value2) throws java.rmi.RemoteException{
    if (application_PortType == null)
      _initApplicationProxy();
    return application_PortType.sub(value1, value2);
  }
  
  
}