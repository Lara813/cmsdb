# coding: utf-8

"""
Higgs process definitions.
"""

__all__ = [
    "h",
    "h_ggf", "h_ggf_tautau",
    "h_vbf", "h_vbf_tautau",
    "vh", "zh", "zh_tautau", "zh_llbb", "zh_qqbb", "wph", "wph_tautau", "wmh", "wmh_tautau", "ggzh",
    "ggzh_llbb", "tth", "tth_tautau", "tth_bb", "tth_nonbb",
    "hh",
    "hh_ggf", "ggHH_kl_0_kt_1", "ggHH_kl_1_kt_1", "ggHH_kl_2p45_kt_1", "ggHH_kl_5_kt_1",
    "hh_vbf", "qqHH_CV_1_C2V_1_kl_1", "qqHH_CV_1_C2V_1_kl_0", "qqHH_CV_1_C2V_1_kl_2",
    "qqHH_CV_1_C2V_0_kl_1", "qqHH_CV_1_C2V_2_kl_1", "qqHH_CV_0p5_C2V_1_kl_1", "qqHH_CV_1p5_C2V_1_kl_1",
    "radion_hh_ggf", "graviton_hh_ggf", "radion_hh_vbf", "graviton_hh_vbf",
]

from order import Process
from scinum import Number

import cmsdb.constants as const


#
# Single Higgs
#

# preliminary Higgs cross sections at 13.6 TeV taken from here:
# https://cds.cern.ch/record/2886099/files/LHCHWG-2024-001.pdf?version=2
# Twiki of (currently outdated) 13.6 TeV Higgs cross sections (might be a useful source when updated):
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG136TeVxsec_extrap?rev=5
# TODO: h xsecs at 13 TeV

h = Process(
    name="h",
    id=10000,
    xsecs={
        13: Number(0.1),  # TODO
        13.6: Number(0.1),  # TODO
    },
)

h_ggf = h.add_process(
    name="h_ggf",
    id=11000,
    label=r"$H_{ggf}$",
    xsecs={
        13: Number(0.1),  # TODO
        13.6: Number(52.23, {  # value for mH=125 GeV
            "pdf": 0.032j,
            "th": (0.046j, 0.067j),
            "th_gaussian": 0.039,
        }),  # TODO: only preliminary
    },
)

h_ggf_tautau = h_ggf.add_process(
    name="h_ggf_tautau",
    id=11100,
    xsecs={ecm: h_ggf.get_xsec(ecm) * const.br_h.tt for ecm in (13, 13.6)},
)

h_vbf = h.add_process(
    name="h_vbf",
    id=12000,
    label=r"$H_{vbf}$",
    xsecs={
        13: Number(0.1),  # TODO
        13.6: Number(4.078, {  # value for mH=125 GeV
            "scale": (0.005j, 0.003j),
            "pdf": 0.021j,
        }),  # TODO: only preliminary
    },
)

h_vbf_tautau = h_vbf.add_process(
    name="h_vbf_tautau",
    id=12100,
    xsecs={ecm: h_vbf.get_xsec(ecm) * const.br_h.tt for ecm in (13, 13.6)},
)

vh = h.add_process(
    name="vh",
    id=13000,
    label="VH",
    xsecs={13: Number(0.1)},  # TODO
)

zh = vh.add_process(
    name="zh",
    id=13100,
    label="ZH",
    xsecs={
        13: Number(0.1),  # TODO
        13.6: Number(0.9439, {  # value for mH=125 GeV
            "scale": (0.037j, 0.032j),
            "pdf": 0.016j,
        }),  # TODO: only preliminary
    },
)

zh_tautau = zh.add_process(
    name="zh_tautau",
    id=13110,
    label=rf"{zh.label}, $H \rightarrow \tau\tau$",
    xsecs={ecm: zh.get_xsec(ecm) * const.br_h.tt for ecm in (13, 13.6)},
)

zh_llbb = zh.add_process(
    name="zh_llbb",
    id=13120,
    label=rf"{zh.label}, $H \rightarrow bb$, $Z \rightarrow ll$",
    xsecs={ecm: zh.get_xsec(ecm) * const.br_h.bb * const.br_z.clep for ecm in (13, 13.6)},
)

zh_qqbb = zh.add_process(
    name="zh_qqbb",
    id=13121,
    label=rf"{zh.label}, $H \rightarrow bb$, $Z \rightarrow qq$",
    xsecs={ecm: zh.get_xsec(ecm) * const.br_h.bb * const.br_z.qq for ecm in (13, 13.6)},
)

wph = vh.add_process(
    name="wph",
    id=13200,
    xsecs={
        13: Number(0.1),  # TODO
        13.6: Number(0.8889, {  # value for mH=125 GeV
            "scale": (0.004j, 0.007j),
            "pdf": 0.018j,
        }),  # TODO: only preliminary
    },
)

wph_tautau = wph.add_process(
    name="wph_tautau",
    id=13210,
    xsecs={ecm: wph.get_xsec(ecm) * const.br_h.tt for ecm in (13, 13.6)},
)

wmh = vh.add_process(
    name="wmh",
    id=13300,
    xsecs={
        13: Number(0.1),  # TODO
        13.6: Number(0.5677, {  # value for mH=125 GeV
            "scale": (0.004j, 0.007j),
            "pdf": 0.018j,
        }),  # TODO: only preliminary
    },
)
wmh_tautau = wmh.add_process(
    name="wmh_tautau",
    id=13310,
    xsecs={ecm: wmh.get_xsec(ecm) * const.br_h.tt for ecm in (13, 13.6)},
)

ggzh = vh.add_process(
    name="ggzh",
    id=14000,
    xsecs={13: Number(0.1)},  # TODO
)

ggzh_llbb = ggzh.add_process(
    name="ggzh_llbb",
    id=14100,
    xsecs={13: Number(0.1)},  # TODO
)

tth = h.add_process(
    name="tth",
    id=15000,
    label=r"$t\bar{t}H$",
    xsecs={
        13: Number(0.1),  # TODO
        13.6: Number(0.5700, {  # value for mH=125 GeV
            "scale": (0.060j, 0.093j),
            "pdf": 0.035j,
        }),  # TODO: only preliminary
    },
)

tth_tautau = tth.add_process(
    name="tth_tautau",
    id=15100,
    label=rf"{tth.label}, $H \rightarrow \tau\tau$",
    xsecs={ecm: tth.get_xsec(ecm) * const.br_h.tt for ecm in (13, 13.6)},
)

tth_bb = tth.add_process(
    name="tth_bb",
    id=15200,
    label=rf"{tth.label}, $H \rightarrow bb$",
    xsecs={ecm: tth.get_xsec(ecm) * const.br_h.bb for ecm in (13, 13.6)},
)

tth_nonbb = tth.add_process(
    name="tth_nonbb",
    id=15300,
    label=rf"{tth.label}, $H \rightarrow$ non-$bb$",
    xsecs={ecm: tth.get_xsec(ecm) * (1 - const.br_h.bb) for ecm in (13, 13.6)},
)


#
# Basic HH processes
#

hh = Process(
    name="hh",
    id=20000,
    label="HH",
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf = hh.add_process(
    name="hh_ggf",
    id=21000,
    label=r"$HH_{ggf}$",
    xsecs={13: Number(0.1)},  # TODO
)

# Naming conventions, cross sections and uncertainties are based on:
# https://gitlab.cern.ch/hh/naming-conventions
# Missing uncertainties are based on:
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGHH?rev=89

ggHH_kl_0_kt_1 = hh_ggf.add_process(
    name="ggHH_kl_0_kt_1",
    id=21001,
    xsecs={
        13: Number(0.069725, {
            "scale": (0.024j, 0.061j),
            "pdf": 0.03j,
            "mtop": (0.06j, 0.12j),
        }),
    },
)

ggHH_kl_1_kt_1 = hh_ggf.add_process(
    name="ggHH_kl_1_kt_1",
    id=21002,
    xsecs={
        13: Number(0.031047, {
            "scale": (0.022j, 0.050j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.18j),
        }),
        13.6: Number(0.03443, {  # value for mH=125 GeV
            "scale": (0.021j, 0.049j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.18j),
        }),
    },
)

ggHH_kl_2p45_kt_1 = hh_ggf.add_process(
    name="ggHH_kl_2p45_kt_1",
    id=21003,
    xsecs={
        13: Number(0.013124, {
            "scale": (0.023j, 0.051j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.22j),
        }),
    },
)

ggHH_kl_5_kt_1 = hh_ggf.add_process(
    name="ggHH_kl_5_kt_1",
    id=21004,
    xsecs={
        13: Number(0.091172, {
            "scale": (0.049j, 0.088j),
            "pdf": 0.03j,
            "mtop": (0.13j, 0.04j),
        }),
    },
)

hh_vbf = hh.add_process(
    name="hh_vbf",
    id=22000,
    label=r"$HH_{vbf}$",
    xsecs={13: Number(0.1)},  # TODO
)

qqHH_CV_1_C2V_1_kl_1 = hh_vbf.add_process(
    name="qqHH_CV_1_C2V_1_kl_1",
    id=22001,
    xsecs={
        13: Number(0.0017260, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
)

qqHH_CV_1_C2V_1_kl_0 = hh_vbf.add_process(
    name="qqHH_CV_1_C2V_1_kl_0",
    id=22002,
    xsecs={
        13: Number(0.0046089, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
)

qqHH_CV_1_C2V_1_kl_2 = hh_vbf.add_process(
    name="qqHH_CV_1_C2V_1_kl_2",
    id=22003,
    xsecs={
        13: Number(0.0014228, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
)

qqHH_CV_1_C2V_0_kl_1 = hh_vbf.add_process(
    name="qqHH_CV_1_C2V_0_kl_1",
    id=22004,
    xsecs={
        13: Number(0.0270800, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
)

qqHH_CV_1_C2V_2_kl_1 = hh_vbf.add_process(
    name="qqHH_CV_1_C2V_2_kl_1",
    id=22005,
    xsecs={
        13: Number(0.00142178, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
)

qqHH_CV_0p5_C2V_1_kl_1 = hh_vbf.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1",
    id=22006,
    xsecs={
        13: Number(0.0108237, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
)

qqHH_CV_1p5_C2V_1_kl_1 = hh_vbf.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1",
    id=22007,
    xsecs={
        13: Number(0.0660185, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
)

#
# Resonant BSM HH production
#

radion_hh_ggf = hh_ggf.add_process(
    name="radion_hh_ggf",
    id=23000,
    label=r"Radion $\rightarrow HH_{ggf}$",
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf = hh_ggf.add_process(
    name="graviton_hh_ggf",
    id=24000,
    label=r"Graviton $\rightarrow HH_{ggf}$",
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf = hh_vbf.add_process(
    name="radion_hh_vbf",
    id=25000,
    label=r"Radion $\rightarrow HH_{vbf}$",
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf = hh_vbf.add_process(
    name="graviton_hh_vbf",
    id=26000,
    label=r"Graviton $\rightarrow HH_{vbf}$",
    xsecs={13: Number(0.1)},  # TODO
)
