import numpy as np

from config_reader import ConfigReader
from data_saver import DataSaver

INPUT_CONFIG = "data/input.cfg"
LOG_FILE = "data/log.txt"
M_MOMENT_FILE = "data/mMoment.txt"
P_BODY_FILE = "data/pBody.txt"

config_reader = ConfigReader(INPUT_CONFIG)

config_reader.read_file()
config_data = config_reader.data

data_saver = DataSaver(LOG_FILE, P_BODY_FILE, M_MOMENT_FILE, config_data)
data_saver.create_log_file()
data_saver.write_result()
data_saver.write_additional_result()

# initialize value from input.cfg
gamma = 1.76 * 10 ** 7
mu = float(config_data["magnetization"])
eta = 5 * 10 ** -2
h_a = 910.0
alpha = float(config_data["alpha"])
h_0 = float(config_data["amplitude"])
omega = 0.001
rho = float(config_data["hySign"])

print(gamma, mu, eta, h_a, alpha, h_0, omega, rho)

# Calculate additional values
beta = (alpha * mu) / (6 * gamma * eta)
alpha_1 = alpha / (1 + beta)

print(beta, alpha_1)

# Set default degree value
a_teta = np.deg2rad(np.pi / 3)
a_varteta = np.deg2rad(2 * np.pi / 3)
a_varfi = np.deg2rad(np.pi / 4)
a_fi = np.deg2rad(np.pi / 6)

print(a_teta, a_fi, a_varfi, a_varteta)

# Initial value for the main four axises
teta_0 = float(config_data["smallTheta"])
fi_0 = float(config_data["smallPhi"])
varfi_0 = float(config_data["bigPhi"])
varteta_0 = float(config_data["bigTheta"])

print(teta_0, fi_0, varfi_0, varteta_0)

# Calculate anpther additional values
hx = h_0 * np.cos(np.deg2rad(omega))
hy = rho * h_0 * np.sin(np.deg2rad(omega))
hz = np.cos(np.deg2rad(omega))
F = np.cos(a_varteta) * np.cos(a_teta) + np.cos(a_fi - a_varfi) * np.sin(a_varteta) * np.sin(a_teta)
f1 = -(F * np.sin(a_varteta) * np.sin(a_fi - a_varfi) + (1 + beta) *
       (hx * np.sin(a_fi) - hy * np.cos(a_fi)))
f2 = (np.cos(a_teta) * (F * np.sin(a_varteta) * np.cos(a_fi - a_varfi) + (1 + beta) *
                        (hy * np.sin(a_fi) + hx * np.cos(a_fi))) -
      np.sin(a_teta) * ((1 + beta) * hz + F * np.cos(a_varteta)))

print(hx, hy, hz, F, f1, f2)

wx = (((1 + beta) ** -1) * (np.cos(a_teta) * np.cos(a_fi) * teta_0 -
                            np.sin(a_teta) * np.sin(a_fi) * fi_0) +
      np.sin(a_teta) * np.sin(a_fi) * hz - np.cos(a_teta) * hy)
wy = (((1 + beta) ** -1) * (np.cos(a_teta) * np.sin(a_fi) * teta_0 +
                            np.sin(a_teta) * np.cos(a_fi) * fi_0) -
      np.sin(a_teta) * np.cos(a_fi) * hz + np.cos(a_teta) * hx)
wz = (-np.sin(a_teta)) * (((1 + beta) ** -1) * teta_0 -
                          np.cos(a_fi) * hy + np.sin(a_fi) * hx)

print(wx, wy, wz)
