import sensorsActuators.*;


public class LowLevelController {
	private Motor lift;
	private Motor thrust;
	private Motor rudder;
	
	private DistanceSensor altimeter;
	
	/**
	 * Set the desired height of the machine. The height is measured relative to the 
	 * position of the distance sensor. The machine will gradually move to the desired 
	 * @param newHeight		new height in Meters.
	 */
	public void setHeight(double newHeight){
		
	}
}
