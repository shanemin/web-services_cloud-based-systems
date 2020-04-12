/**
 * Application_ServiceLocator.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis 1.4 Apr 22, 2006 (06:55:48 PDT) WSDL2Java emitter.
 */

package tns;

public class Application_ServiceLocator extends org.apache.axis.client.Service implements tns.Application_Service {

    public Application_ServiceLocator() {
    }


    public Application_ServiceLocator(org.apache.axis.EngineConfiguration config) {
        super(config);
    }

    public Application_ServiceLocator(java.lang.String wsdlLoc, javax.xml.namespace.QName sName) throws javax.xml.rpc.ServiceException {
        super(wsdlLoc, sName);
    }

    // Use to get a proxy class for Application
    private java.lang.String Application_address = "http://localhost:8000/wsdl.wsdl";

    public java.lang.String getApplicationAddress() {
        return Application_address;
    }

    // The WSDD service name defaults to the port name.
    private java.lang.String ApplicationWSDDServiceName = "Application";

    public java.lang.String getApplicationWSDDServiceName() {
        return ApplicationWSDDServiceName;
    }

    public void setApplicationWSDDServiceName(java.lang.String name) {
        ApplicationWSDDServiceName = name;
    }

    public tns.Application_PortType getApplication() throws javax.xml.rpc.ServiceException {
       java.net.URL endpoint;
        try {
            endpoint = new java.net.URL(Application_address);
        }
        catch (java.net.MalformedURLException e) {
            throw new javax.xml.rpc.ServiceException(e);
        }
        return getApplication(endpoint);
    }

    public tns.Application_PortType getApplication(java.net.URL portAddress) throws javax.xml.rpc.ServiceException {
        try {
            tns.Application_BindingStub _stub = new tns.Application_BindingStub(portAddress, this);
            _stub.setPortName(getApplicationWSDDServiceName());
            return _stub;
        }
        catch (org.apache.axis.AxisFault e) {
            return null;
        }
    }

    public void setApplicationEndpointAddress(java.lang.String address) {
        Application_address = address;
    }

    /**
     * For the given interface, get the stub implementation.
     * If this service has no port for the given interface,
     * then ServiceException is thrown.
     */
    public java.rmi.Remote getPort(Class serviceEndpointInterface) throws javax.xml.rpc.ServiceException {
        try {
            if (tns.Application_PortType.class.isAssignableFrom(serviceEndpointInterface)) {
                tns.Application_BindingStub _stub = new tns.Application_BindingStub(new java.net.URL(Application_address), this);
                _stub.setPortName(getApplicationWSDDServiceName());
                return _stub;
            }
        }
        catch (java.lang.Throwable t) {
            throw new javax.xml.rpc.ServiceException(t);
        }
        throw new javax.xml.rpc.ServiceException("There is no stub implementation for the interface:  " + (serviceEndpointInterface == null ? "null" : serviceEndpointInterface.getName()));
    }

    /**
     * For the given interface, get the stub implementation.
     * If this service has no port for the given interface,
     * then ServiceException is thrown.
     */
    public java.rmi.Remote getPort(javax.xml.namespace.QName portName, Class serviceEndpointInterface) throws javax.xml.rpc.ServiceException {
        if (portName == null) {
            return getPort(serviceEndpointInterface);
        }
        java.lang.String inputPortName = portName.getLocalPart();
        if ("Application".equals(inputPortName)) {
            return getApplication();
        }
        else  {
            java.rmi.Remote _stub = getPort(serviceEndpointInterface);
            ((org.apache.axis.client.Stub) _stub).setPortName(portName);
            return _stub;
        }
    }

    public javax.xml.namespace.QName getServiceName() {
        return new javax.xml.namespace.QName("tns", "Application");
    }

    private java.util.HashSet ports = null;

    public java.util.Iterator getPorts() {
        if (ports == null) {
            ports = new java.util.HashSet();
            ports.add(new javax.xml.namespace.QName("tns", "Application"));
        }
        return ports.iterator();
    }

    /**
    * Set the endpoint address for the specified port name.
    */
    public void setEndpointAddress(java.lang.String portName, java.lang.String address) throws javax.xml.rpc.ServiceException {
        
if ("Application".equals(portName)) {
            setApplicationEndpointAddress(address);
        }
        else 
{ // Unknown Port Name
            throw new javax.xml.rpc.ServiceException(" Cannot set Endpoint Address for Unknown Port" + portName);
        }
    }

    /**
    * Set the endpoint address for the specified port name.
    */
    public void setEndpointAddress(javax.xml.namespace.QName portName, java.lang.String address) throws javax.xml.rpc.ServiceException {
        setEndpointAddress(portName.getLocalPart(), address);
    }

}
