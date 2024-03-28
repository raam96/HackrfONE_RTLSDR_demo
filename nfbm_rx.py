#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: WBFM Receiver
# Author: Lt Raam
# GNU Radio version: v3.9.2.0-85-g08bb05c1

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import osmosdr
import time



from gnuradio import qtgui

class nfbm_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "WBFM Receiver", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("WBFM Receiver")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "nfbm_rx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_0 = variable_0 = 0
        self.samp_rate = samp_rate = 1.8e6
        self.reveiver_gain = reveiver_gain = 40
        self.resampler_decimation = resampler_decimation = 4
        self.main_sample_rate = main_sample_rate = 12e3
        self.input_decimation = input_decimation = 26
        self.base_band_freq = base_band_freq = 399994800
        self.VOLUME = VOLUME = 0.7
        self.LPF_CUTOFF_FEQ = LPF_CUTOFF_FEQ = 2e6

        ##################################################
        # Blocks
        ##################################################
        self._reveiver_gain_range = Range(10, 70, 1, 40, 200)
        self._reveiver_gain_win = RangeWidget(self._reveiver_gain_range, self.set_reveiver_gain, 'reveiver_gain', "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._reveiver_gain_win)
        self._base_band_freq_range = Range(399e6, 401e6, 1e2, 399994800, 200)
        self._base_band_freq_win = RangeWidget(self._base_band_freq_range, self.set_base_band_freq, 'base_band_freq', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._base_band_freq_win)
        self._LPF_CUTOFF_FEQ_range = Range(2e6, 3e6, 1e5, 2e6, 200)
        self._LPF_CUTOFF_FEQ_win = RangeWidget(self._LPF_CUTOFF_FEQ_range, self.set_LPF_CUTOFF_FEQ, 'LPF_CUTOFF_FEQ', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._LPF_CUTOFF_FEQ_win)
        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.rtlsdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(base_band_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(reveiver_gain, 0)
        self.rtlsdr_source_0.set_if_gain(reveiver_gain, 0)
        self.rtlsdr_source_0.set_bb_gain(reveiver_gain, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        self._resampler_decimation_range = Range(1, 20, 1, 4, 200)
        self._resampler_decimation_win = RangeWidget(self._resampler_decimation_range, self.set_resampler_decimation, 'resampler_decimation', "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._resampler_decimation_win)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=[],
                fractional_bw=0)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            main_sample_rate*2, #bw
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            base_band_freq, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(True)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                LPF_CUTOFF_FEQ/2,
                20e3,
                1e6,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=500e3,
        	audio_decimation=10,
        )
        self._VOLUME_range = Range(0.5, 2, 0.1, 0.7, 200)
        self._VOLUME_win = RangeWidget(self._VOLUME_range, self.set_VOLUME, 'VOLUME', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._VOLUME_win)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rational_resampler_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "nfbm_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_0(self):
        return self.variable_0

    def set_variable_0(self, variable_0):
        self.variable_0 = variable_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.base_band_freq, self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_reveiver_gain(self):
        return self.reveiver_gain

    def set_reveiver_gain(self, reveiver_gain):
        self.reveiver_gain = reveiver_gain
        self.rtlsdr_source_0.set_gain(self.reveiver_gain, 0)
        self.rtlsdr_source_0.set_if_gain(self.reveiver_gain, 0)
        self.rtlsdr_source_0.set_bb_gain(self.reveiver_gain, 0)

    def get_resampler_decimation(self):
        return self.resampler_decimation

    def set_resampler_decimation(self, resampler_decimation):
        self.resampler_decimation = resampler_decimation

    def get_main_sample_rate(self):
        return self.main_sample_rate

    def set_main_sample_rate(self, main_sample_rate):
        self.main_sample_rate = main_sample_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.main_sample_rate*2)

    def get_input_decimation(self):
        return self.input_decimation

    def set_input_decimation(self, input_decimation):
        self.input_decimation = input_decimation

    def get_base_band_freq(self):
        return self.base_band_freq

    def set_base_band_freq(self, base_band_freq):
        self.base_band_freq = base_band_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.base_band_freq, self.samp_rate)
        self.rtlsdr_source_0.set_center_freq(self.base_band_freq, 0)

    def get_VOLUME(self):
        return self.VOLUME

    def set_VOLUME(self, VOLUME):
        self.VOLUME = VOLUME

    def get_LPF_CUTOFF_FEQ(self):
        return self.LPF_CUTOFF_FEQ

    def set_LPF_CUTOFF_FEQ(self, LPF_CUTOFF_FEQ):
        self.LPF_CUTOFF_FEQ = LPF_CUTOFF_FEQ
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.LPF_CUTOFF_FEQ/2, 20e3, 1e6, window.WIN_HAMMING, 6.76))




def main(top_block_cls=nfbm_rx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
