GAMMA = 1.76 * 10 ** 7


class FerromagneticNanoparticle:

    def __init__(self, input_data):
        self.magnetization = float(input_data["magnetization"])
        self.viscosity = float(input_data["viscosity"])
        self.alpha = float(input_data["alpha"])
        self.beta = 0.0
        self.amplitude = float(input_data["amplitude"])
        self.omega = 0.0
        self.hz = 0.0
        self.alpha_1 = 0.0
        self.beta_1 = 0.0
        self.dt = float(input_data["numberOfPeriods"]) / float(input_data["timeStep"])
        self.time = float(input_data["printStep"]) * float(input_data["numberOfPeriods"]) / float(input_data["timeStep"])
        self.tau_1 = 0.0
        self.tau_2 = 0.0
        self.small_theta = float(input_data["smallTheta"])
        self.small_phi = float(input_data["smallPhi"])
        self.big_theta = float(input_data["bigTheta"])
        self.big_phi = float(input_data["bigPhi"])
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
        self.rho = float(input_data["hySign"])

    def calc_parameters(self):
        self.beta = (self.alpha * self.magnetization) / (6 * GAMMA * self.viscosity)
        self.alpha_1 = self.alpha / (1 + self.beta)
        self.beta_1 = 1 + self.beta
        self.tau_1 = 1 / (1 + self.alpha_1 ** 2)
        self.tau_2 = self.beta * self.beta_1 / self.alpha

# # Set default degree value
# a_teta = np.deg2rad(np.pi / 3)
# a_varteta = np.deg2rad(2 * np.pi / 3)
# a_varfi = np.deg2rad(np.pi / 4)
# a_fi = np.deg2rad(np.pi / 6)
#
# print(a_teta, a_fi, a_varfi, a_varteta)
#
# # Initial value for the main four axises
# teta_0 = float(config_data["smallTheta"])
# fi_0 = float(config_data["smallPhi"])
# varfi_0 = float(config_data["bigPhi"])
# varteta_0 = float(config_data["bigTheta"])
#
# print(teta_0, fi_0, varfi_0, varteta_0)
#
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
