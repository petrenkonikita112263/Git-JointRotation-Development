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
        f = np.cos(np.deg2rad(self.small_theta)) * np.sin(np.deg2rad(self.big_theta)) + \
            np.cos(np.deg2rad(self.small_phi - self.big_phi)) * np.sin(np.deg2rad(self.big_theta)) * \
            np.sin(np.deg2rad(self.small_theta))
        c_1 = f * np.cos(np.deg2rad(self.small_phi - self.big_phi)) * np.sin(np.deg2rad(self.big_theta))
        c_2 = f * np.sin(np.deg2rad(self.small_phi - self.big_phi)) * np.sin(np.deg2rad(self.big_theta))
        h_1 = self.get_hx(t) * np.cos(np.deg2rad(self.small_phi)) + self.get_hy(t) * \
              np.sin(np.deg2rad(self.small_phi))
        h_2 = self.get_hx(t) * np.sin(np.deg2rad(self.small_phi)) - self.get_hy(t) * \
              np.cos(np.deg2rad(self.small_phi))

# # Calculate anpther additional values
# hx = h_0 * np.cos(np.deg2rad(omega))
# hy = rho * h_0 * np.sin(np.deg2rad(omega))
# hz = np.cos(np.deg2rad(omega))
# F = np.cos(a_varteta) * np.cos(a_teta) + np.cos(a_fi - a_varfi) * np.sin(a_varteta) * np.sin(a_teta)
# f1 = -(F * np.sin(a_varteta) * np.sin(a_fi - a_varfi) + (1 + beta) *
#        (hx * np.sin(a_fi) - hy * np.cos(a_fi)))
# f2 = (np.cos(a_teta) * (F * np.sin(a_varteta) * np.cos(a_fi - a_varfi) + (1 + beta) *
#                         (hy * np.sin(a_fi) + hx * np.cos(a_fi))) -
#       np.sin(a_teta) * ((1 + beta) * hz + F * np.cos(a_varteta)))
#
# print(hx, hy, hz, F, f1, f2)
#
# wx = (((1 + beta) ** -1) * (np.cos(a_teta) * np.cos(a_fi) * teta_0 -
#                             np.sin(a_teta) * np.sin(a_fi) * fi_0) +
#       np.sin(a_teta) * np.sin(a_fi) * hz - np.cos(a_teta) * hy)
# wy = (((1 + beta) ** -1) * (np.cos(a_teta) * np.sin(a_fi) * teta_0 +
#                             np.sin(a_teta) * np.cos(a_fi) * fi_0) -
#       np.sin(a_teta) * np.cos(a_fi) * hz + np.cos(a_teta) * hx)
# wz = (-np.sin(a_teta)) * (((1 + beta) ** -1) * teta_0 -
#                           np.cos(a_fi) * hy + np.sin(a_fi) * hx)
#
# print(wx, wy, wz)
