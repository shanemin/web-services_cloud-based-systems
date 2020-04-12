package tns;

import java.rmi.RemoteException;

import javax.xml.rpc.ServiceException;

public class Client {

	public static void main(String[] args) {
		Application_ServiceLocator asLocator = new Application_ServiceLocator();
		try {
			asLocator.setEndpointAddress("Application", "http://localhost:8000/applicationService");
			Application_PortType service = asLocator.getApplication();
			
			double add = service.add((double) 12, (double) 12);
			double sub = service.sub((double) 12, (double) 12);
			double mul = service.mul((double) 12, (double) 12);
			double div = service.div((double) 12, (double) 12);
			
			System.out.println("12 + 12 = " + add);
			System.out.println("12 - 12 = " + sub);
			System.out.println("12 * 12 = " + mul);
			System.out.println("12 / 12 = " + div);
			
			System.exit(0);
		} catch (ServiceException | RemoteException e) {
			e.printStackTrace();
		}
	}
}
