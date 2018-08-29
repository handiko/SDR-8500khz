#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HF FSK RX
# Author: Handiko Gesang
# Description: Implement Zeroth OSI Layer for Receiving HF FSK
# Generated: Wed Aug 29 23:17:05 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import sip
import sys


class hf_fsk_rx1(gr.top_block, Qt.QWidget):

    def __init__(self, filename='HDSDR_20140419_185856Z_8500kHz_RF.wav', samp_rate=1.028571e6):
        gr.top_block.__init__(self, "HF FSK RX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("HF FSK RX")
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

        self.settings = Qt.QSettings("GNU Radio", "hf_fsk_rx1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.filename = filename
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.vfo = vfo = 37.9e3
        self.rit = rit = 0
        self.low_cut = low_cut = 100
        self.intermediate_rate = intermediate_rate = 192e3
        self.hi_cut = hi_cut = 3000
        self.flip = flip = 1
        self.cfreq = cfreq = 8.5e6
        self.bb_rate = bb_rate = 24e3
        self.af_filter = af_filter = False

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Tab 0')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Tab 1')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Tab 2')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'Tab 3')
        self.top_grid_layout.addWidget(self.tab, 0,0,1,2)
        self._vfo_range = Range(-samp_rate/2, samp_rate/2, 500, 37.9e3, 200)
        self._vfo_win = RangeWidget(self._vfo_range, self.set_vfo, 'VFO', "counter_slider", float)
        self.top_grid_layout.addWidget(self._vfo_win, 1,0,1,1)
        self._rit_range = Range(-3e3, 3e3, 10, 0, 200)
        self._rit_win = RangeWidget(self._rit_range, self.set_rit, 'RIT', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rit_win, 1,1,1,1)
        self._low_cut_range = Range(100, 1400, 10, 100, 200)
        self._low_cut_win = RangeWidget(self._low_cut_range, self.set_low_cut, 'AF Filter Low Cut', "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._low_cut_win, 1,1,1,1)
        self._hi_cut_range = Range(1600, 3000, 10, 3000, 200)
        self._hi_cut_win = RangeWidget(self._hi_cut_range, self.set_hi_cut, 'AF Filter Hi Cut', "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._hi_cut_win, 2,1,1,1)
        _af_filter_check_box = Qt.QCheckBox('AF Filter')
        self._af_filter_choices = {True: 0, False: 1}
        self._af_filter_choices_inv = dict((v,k) for k,v in self._af_filter_choices.iteritems())
        self._af_filter_callback = lambda i: Qt.QMetaObject.invokeMethod(_af_filter_check_box, "setChecked", Qt.Q_ARG("bool", self._af_filter_choices_inv[i]))
        self._af_filter_callback(self.af_filter)
        _af_filter_check_box.stateChanged.connect(lambda i: self.set_af_filter(self._af_filter_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_af_filter_check_box, 0,1,1,1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	8192, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	cfreq+vfo+rit, #fc
        	intermediate_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.02)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
        if not False:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [3, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-160, -90)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_f(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	bb_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-90, -10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not False)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 0,0,3,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	cfreq+vfo+rit, #fc
        	intermediate_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.02)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -90)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
        	  bb_rate/samp_rate,
                  taps=None,
        	  flt_size=16)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(0)
        	
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  intermediate_rate/samp_rate,
                  taps=None,
        	  flt_size=16)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.complex_band_pass(2,bb_rate,low_cut,hi_cut,bb_rate/20,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source(filename, True)
        self.blocks_rotator_cc_2 = blocks.rotator_cc(1.5e3*2*math.pi/bb_rate)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(-(vfo+rit)*2*math.pi/samp_rate)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blks2_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=af_filter,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=af_filter,
        )
        self.audio_sink_0 = audio.sink(24000, '', True)
        self.analog_agc_xx_0 = analog.agc_cc(1e-1, 0.15, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.blks2_selector_0, 1), (self.blks2_selector_1, 1))    
        self.connect((self.blks2_selector_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.blks2_selector_1, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_rotator_cc_0, 0))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.pfb_arb_resampler_xxx_0, 0))    
        self.connect((self.blocks_rotator_cc_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))    
        self.connect((self.blocks_rotator_cc_2, 0), (self.analog_agc_xx_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 1), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.fft_filter_xxx_0, 0), (self.blks2_selector_1, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.blocks_rotator_cc_2, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hf_fsk_rx1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.bb_rate/self.samp_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.intermediate_rate/self.samp_rate)
        self.blocks_rotator_cc_0.set_phase_inc(-(self.vfo+self.rit)*2*math.pi/self.samp_rate)

    def get_vfo(self):
        return self.vfo

    def set_vfo(self, vfo):
        self.vfo = vfo
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)
        self.blocks_rotator_cc_0.set_phase_inc(-(self.vfo+self.rit)*2*math.pi/self.samp_rate)

    def get_rit(self):
        return self.rit

    def set_rit(self, rit):
        self.rit = rit
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)
        self.blocks_rotator_cc_0.set_phase_inc(-(self.vfo+self.rit)*2*math.pi/self.samp_rate)

    def get_low_cut(self):
        return self.low_cut

    def set_low_cut(self, low_cut):
        self.low_cut = low_cut
        self.fft_filter_xxx_0.set_taps((firdes.complex_band_pass(2,self.bb_rate,self.low_cut,self.hi_cut,self.bb_rate/20,firdes.WIN_BLACKMAN)))

    def get_intermediate_rate(self):
        return self.intermediate_rate

    def set_intermediate_rate(self, intermediate_rate):
        self.intermediate_rate = intermediate_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.intermediate_rate/self.samp_rate)

    def get_hi_cut(self):
        return self.hi_cut

    def set_hi_cut(self, hi_cut):
        self.hi_cut = hi_cut
        self.fft_filter_xxx_0.set_taps((firdes.complex_band_pass(2,self.bb_rate,self.low_cut,self.hi_cut,self.bb_rate/20,firdes.WIN_BLACKMAN)))

    def get_flip(self):
        return self.flip

    def set_flip(self, flip):
        self.flip = flip

    def get_cfreq(self):
        return self.cfreq

    def set_cfreq(self, cfreq):
        self.cfreq = cfreq
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.cfreq+self.vfo+self.rit, self.intermediate_rate)

    def get_bb_rate(self):
        return self.bb_rate

    def set_bb_rate(self, bb_rate):
        self.bb_rate = bb_rate
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.bb_rate)
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.bb_rate/self.samp_rate)
        self.fft_filter_xxx_0.set_taps((firdes.complex_band_pass(2,self.bb_rate,self.low_cut,self.hi_cut,self.bb_rate/20,firdes.WIN_BLACKMAN)))
        self.blocks_rotator_cc_2.set_phase_inc(1.5e3*2*math.pi/self.bb_rate)

    def get_af_filter(self):
        return self.af_filter

    def set_af_filter(self, af_filter):
        self.af_filter = af_filter
        self._af_filter_callback(self.af_filter)
        self.blks2_selector_1.set_input_index(int(self.af_filter))
        self.blks2_selector_0.set_output_index(int(self.af_filter))


def argument_parser():
    description = 'Implement Zeroth OSI Layer for Receiving HF FSK'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-f", "--filename", dest="filename", type="string", default='HDSDR_20140419_185856Z_8500kHz_RF.wav',
        help="Set Input Filename [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(1.028571e6),
        help="Set Input IQ Sample Rate [default=%default]")
    return parser


def main(top_block_cls=hf_fsk_rx1, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(filename=options.filename, samp_rate=options.samp_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
