import py_qmc5883l


class CompassHelper:
    
    def __init__(self):
        self.sensor = py_qmc5883l.QMC5883L()
        self.sensor.set_declination(-8.87)
        self.sensor.calibration = [[1.2115, 0.11794, 1104.34691],
                              [0.11794, 1.06576, -625.31453],
                              [0, 0, 1.0]]

    def get_bearing(self):
        return self.sensor.get_bearing()