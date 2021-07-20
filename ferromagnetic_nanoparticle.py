import numpy as np

GAMMA = 1.76 * 10 ** 7


class FerromagneticNanoparticle:

    def __init__(self, input_data):
        self.amplitude = float(input_data["amplitude"])
        self.omega = float(input_data["frequency"])
        self.period = int(input_data["numberOfPeriods"])
        self.max_period = float(input_data["maxNumberOfPeriods"])
        self.extremus = int(input_data["numberOfExtremums"])
        self.skip_period = float(input_data["skipPeriods"])
        self.print_step = float(input_data["printStep"])
        self.print_period = int(input_data["printLastNperiods"])
        self.time_step = int(input_data["timeStep"])
        self.diff = float(input_data["acceptableDiff"])
        self.alpha = float(input_data["alpha"])
        self.magnetization = float(input_data["magnetization"])
        self.viscosity = float(input_data["viscosity"])
        self.small_theta = float(input_data["smallTheta"])
        self.small_phi = float(input_data["smallPhi"])
        self.big_theta = float(input_data["bigTheta"])
        self.big_phi = float(input_data["bigPhi"])
        self.rho = float(input_data["hySign"])
        self.output_precession = int(input_data["outputPrecision"])
        self.beta = 0.0
        self.hz = 0.0
        self.alpha_1 = 0.0
        self.beta_1 = 0.0
        self.tau_1 = 0.0
        self.tau_2 = 0.0
        self.energy = 0.0
        self.f_small_theta = 0.0
        self.f_small_phi = 0.0
        self.f_big_theta = 0.0
        self.f_big_phi = 0.0
        self.d_small_theta = 0.0
        self.d_small_phi = 0.0
        self.d_big_theta = 0.0
        self.d_big_phi = 0.0
        self.d_energy = 0.0

    def calc_parameters(self):
        self.beta = (self.alpha * self.magnetization) / (6 * GAMMA * self.viscosity)
        self.alpha_1 = self.alpha / (1 + self.beta)
        self.beta_1 = 1 + self.beta
        self.tau_1 = 1 / (1 + self.alpha_1 ** 2)
        self.tau_2 = self.beta * self.beta_1 / self.alpha

    def calc_time_parameters(self):
        time = self.print_step * self.period / self.time_step
        dt = self.period / self.time_step
        return time, dt

    def get_hx(self, t):
        return self.amplitude * np.cos(np.deg2rad(self.omega * t))

    def get_hy(self, t):
        return self.rho * self.amplitude * np.sin(np.deg2rad(self.omega * t))

    def get_hz(self, t):
        return self.amplitude * np.cos(np.deg2rad(self.omega * t))

    def calc_main_func(self, t):
        cos_small_theta = np.cos(np.deg2rad(self.small_theta))
        cos_big_theta = np.cos(np.deg2rad(self.big_theta))
        cos_small_phi = np.cos(np.deg2rad(self.small_phi))
        cos_big_phi = np.cos(np.deg2rad(self.big_phi))
        sin_small_theta = np.sin(np.deg2rad(self.small_theta))
        sin_big_theta = np.sin(np.deg2rad(self.big_theta))
        sin_small_phi = np.cos(np.deg2rad(self.small_phi))
        sin_big_phi = np.cos(np.deg2rad(self.big_phi))

        f = cos_small_theta * cos_big_theta + \
            np.cos(np.deg2rad(self.small_phi - self.big_phi)) * sin_big_theta * sin_small_theta
        c_1 = f * np.cos(np.deg2rad(self.small_phi - self.big_phi)) * sin_big_theta
        c_2 = f * np.sin(np.deg2rad(self.small_phi - self.big_phi)) * sin_big_theta
        h_1 = self.get_hx(t) * cos_small_phi + self.get_hy(t) * sin_small_phi
        h_2 = self.get_hx(t) * sin_small_phi - self.get_hy(t) * cos_small_phi
        f_1 = - (c_2 + self.beta_1 * h_2)
        f_2 = cos_small_theta * (c_1 + self.beta_1 * h_1) - \
              (f * cos_big_theta + self.beta_1 * self.get_hz(t)) * sin_small_theta

        self.f_small_theta = self.tau_1 * (f_1 + self.alpha_1 * f_2)
        self.f_small_phi = self.tau_1 * (self.alpha_1 * f_1 - f_2) / sin_small_theta

        print(f"Values of small: theta - {self.f_small_theta}, phi - {self.f_small_phi}")

        w_x = (self.f_small_theta * cos_small_theta * cos_small_phi -
               self.f_small_phi * sin_small_theta * sin_small_phi) / self.beta_1 + \
              self.get_hz(t) * sin_small_theta * sin_small_phi - self.get_hy(t) * cos_small_theta

        w_y = (self.f_small_theta * cos_small_theta * sin_small_phi +
               self.f_small_phi * sin_small_theta * cos_small_phi) / self.beta_1 + \
              self.get_hx(t) * cos_small_theta - self.get_hz(t) * sin_small_theta * cos_small_phi

        w_z = - (self.f_small_theta / self.beta_1 + h_2) * sin_small_theta

        print(w_x, w_y, w_z)

        self.f_big_theta = self.tau_2 * (w_y * cos_big_phi - w_x * sin_big_phi)
        self.f_big_phi = self.tau_2 * (w_z - cos_big_theta * (w_x * cos_big_phi + w_y * sin_big_phi) / sin_big_theta)

        print(f"Values of big: theta - {self.f_big_theta}, phi - {self.f_big_phi}")

    def calc_energy(self, t):
        cos_small_theta = np.cos(np.deg2rad(self.small_theta))
        cos_big_theta = np.cos(np.deg2rad(self.big_theta))
        cos_small_phi = np.cos(np.deg2rad(self.small_phi))
        sin_small_theta = np.sin(np.deg2rad(self.small_theta))
        sin_big_theta = np.sin(np.deg2rad(self.big_theta))
        sin_small_phi = np.cos(np.deg2rad(self.small_phi))

        f = cos_small_theta * cos_big_theta + \
            np.cos(np.deg2rad(self.small_phi - self.big_phi)) * sin_big_theta * sin_small_theta
        h_1 = self.get_hx(t) * cos_small_phi + self.get_hy(t) * sin_small_phi
        h_2 = self.get_hx(t) * sin_small_phi - self.get_hy(t) * cos_small_phi
        h_3 = self.get_hz(t)
        c_1 = f * np.cos(np.deg2rad(self.small_phi - self.big_phi)) * sin_big_theta
        c_2 = f * np.sin(np.deg2rad(self.small_phi - self.big_phi)) * sin_big_theta
        c_3 = f * cos_big_theta

        print(f"h_1 = {h_1}, c_1={c_1}")
        print(f"h_2 = {h_2}, c_2={c_2}")
        print(f"h_3 = {h_3}, c_3={c_3}")

        # further realization
        # before that need to find the original values of  pair easy axes and pair magnetic moments
        # (small_theta & big_theta, small_phi & big_Phi)
        # by runge kutta 4th order method
        """energy = cos_small_theta * (h_1 + c_1) * \
                 self.f_small_theta - sin_small_theta * (h_2 + c_2) * self.small_phi - \
                 sin_small_theta * (h_3 + c_3) * self.small_theta

        print(f"Energy = {energy}")"""
