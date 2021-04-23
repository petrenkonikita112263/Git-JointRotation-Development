class DataSaver:
    """Save info to log file, pBody file and mMoment file.
    At the time safe the data from dictionary that is based on config file"""

    def __init__(self, log_path, p_path, m_path, info_data):
        self.log_file = log_path
        self.p_file = p_path
        self.m_file = m_path
        self.data = info_data

    def create_log_file(self):
        with open(self.log_file, "w") as log:
            for k, v in self.data.items():
                dict_content = "# " + k + " = " + v + "\n"
                log.write(dict_content)

    def write_result(self):
        with open(self.log_file, "a") as log:
            skip_text = f"===== Skipping {self.data['skipPeriods']} periods =====\n"
            column_names = f"period\t\t\ttime\t\t\tsmallTheta" \
                           f"\t\t\tbigTheta\t\t\tsmallPhi\t\t\tbigPhi" \
                           f"\t\t\tenergy\t\t\tenergy/time\t\t\t{self.data['variable']}"
            skip_text += column_names
            log.write(skip_text)

    def write_additional_result(self):
        with open(self.p_file, "w") as p_file, open(self.m_file, "w") as m_file:
            p_column_names = "frequency\t\t\tamplitude\t\t\tenergy/time" \
                             "\t\t\tmaxBigTheta\t\t\tminBigTheta\t\t\t" \
                             "averageBigTheta\t\t\tperiodTheta(before)" \
                             "\t\t\tperiodTheta(after)\t\t\tvelocityBigPhi" \
                             "\t\t\tphaseBigPhi\t\t\tmode\n"
            m_column_names = "frequency\t\t\tamplitude\t\t\tenergy/time" \
                             "\t\t\tmaxSmallTheta\t\t\tminSmallTheta\t\t\t" \
                             "averageSmallTheta\t\t\tperiodTheta(before)" \
                             "\t\t\tperiodTheta(after)\t\t\tvelocitySmallPhi" \
                             "\t\t\tphaseSmallPhi\t\t\tmode\n"
            p_file.write(p_column_names)
            m_file.write(m_column_names)
