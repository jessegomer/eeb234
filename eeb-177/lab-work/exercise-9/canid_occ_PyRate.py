#!/usr/bin/env python
from numpy import * 


data_1=[array([15.241364,15.733916,15.127927,12.243007,13.899549,11.182424,13.621403,14.289296,13.712188,14.153795,15.001585,10.67711,11.232342]),
array([17.022197,16.772562,14.778913,14.417196,13.807826,15.904279,13.709917,13.670765,14.168402,15.958971,14.255448]),
array([14.877912,17.921,15.052582,14.998214,11.978158,11.651499,14.861715,15.636208,15.820413,15.11008,5.125333,13.368961,13.798957,15.557287,14.648419,12.117727,16.13283,14.97462,15.562005,15.761185,12.280757,13.52509,15.159345,13.25279,15.473479,14.936094,10.661381,13.218938,17.526152,15.651608,14.55859,10.663859,15.216477,14.258521,14.877158,15.775255,10.126924,15.414471,12.309465,14.045319,14.501828,12.282885,15.739127,10.557041,5.783739,9.462059,14.894101,15.584024,13.228964,21.322723,15.179333]),
array([14.523978,14.044243,14.724956,11.616045,15.551464,15.868211,14.682291,13.69434,14.405954]),
array([14.271904]),
array([10.457836,14.427921,12.920714,11.01938,12.247062,12.39033,12.966354,19.263011,15.209178]),
array([12.026606,12.794174,11.914058,12.340511,17.783248,11.172898,7.274749,20.923592,13.42899,10.490036,10.976994,11.356101,11.599632,20.836199,10.973339,11.512006,10.464218,21.362063,8.650724,10.420829,7.596102,13.085636,12.300246,11.996387,13.137411,10.970018,12.838982,11.538946,5.775248,12.629527,11.918309,8.504505,11.939959,21.185696,11.171617,10.594649,12.174714,11.90899,7.295835,11.768549,11.514427,12.302811,11.409843,10.974285,11.730073,12.331547,10.925387,13.425695,10.347033,10.670737,13.047907,11.266887,10.993519,9.316971,11.469926,10.963306,11.981254,12.666282,12.229727,12.75007,12.244916,10.843378]),
array([19.252473]),
array([4.692255]),
array([0.332771,0.631832,0.012389,0.067233,0.014374,0.088322,0.008497,0.108258,0.003749,0.003709,0.006453]),
array([29.53759]),
array([31.051302,31.817881,26.277552,20.811654,26.127088,29.500507,21.417903,30.219879,26.329581,25.412834,28.313409,21.271728,29.435567,28.145032,29.144808,27.05397,28.027182,28.343952,26.707338,28.085719,29.885082,30.093221,28.367012,30.53604,24.401157,28.467074,25.011299]),
array([31.025751,33.240804,31.19362,32.792624,33.246743,33.081848,32.513402,22.120805,26.557769]),
array([21.867066,22.801806,22.886405,17.060269,16.586759,14.615499,15.302959,7.444797,12.588051,11.188676,13.637128,12.666368,15.430427,11.451411,15.516232,12.927365,13.149266,13.22465,6.32009,13.213027,20.472132,14.913978,13.29336,10.661625,17.471821,14.002936,12.589711,11.225447,20.926811,20.73839,5.405566,12.971061,12.358941,18.572584,20.044122,17.182791,5.992161,17.926464,18.366367,20.261133,19.37343,18.82825,16.005901,19.528799,7.105674,14.372576,13.862347,12.180655,13.108435,11.949769,12.420989,11.934175,12.731169,11.023846,13.65581,14.755583,15.910267,16.019353]),
array([8.408511,10.043806,5.992297,7.269606,5.100521,10.149655,5.228563,10.260911,2.664328,9.53558,7.228638,8.34474,8.52007,8.310135,19.607456,8.013071,8.048774,5.552597,10.193006,10.239795,8.296169,7.380389,4.446075,4.32943,4.597359,2.858966,3.334814,4.415165,3.125463,2.672888,2.461354,3.987042,7.905033]),
array([2.581189,3.977091,4.208867,2.687039,3.241109,4.679686,3.389994,4.891063,2.735791,4.601026,2.116322,4.781238,2.6035,3.511881,2.43242,4.146591,2.544409,4.2795,4.347834,2.801078,2.52787,2.55811,3.275115,2.103206,3.682345,4.642005,4.416459,3.594063]),
array([3.768669]),
array([9.643769,8.394218,8.79642,13.235638,7.471024,7.356121,7.679762,4.757554,7.550106,2.317355,4.542679,1.890077,3.081878,4.646798,1.954708,2.674829]),
array([12.632799,16.861764,10.859069,10.555561,11.287213,13.060334,17.733713,10.306817]),
array([5.253829,5.390767,5.004757]),
array([9.790073,4.918521,5.809938]),
array([5.588786,7.27661,6.246611,6.940014,9.317666,6.70273,9.152976,21.015634,16.586277,8.760011,11.987763,8.433984,11.143686,7.891046,8.629706,6.765474,13.257351,13.558964]),
array([6.882511,10.079891,9.57301,7.967025,9.015875,5.32571,9.406087,9.682213,6.106376,8.203585,6.343343,17.010297,7.432487,5.380179,15.243807,6.679055,18.680912,9.296176,21.800806,9.604441,11.067298,4.931727,9.08476,6.671206,7.83318,9.431083,8.335394,5.032279,9.103658]),
array([25.472187]),
array([36.904588,34.172673,36.018149,33.535946,31.995292,23.74625,26.233058,25.356999,26.559799,20.439022,23.613042,25.535662,25.999166,30.089097,29.060619,28.889364,21.509911,19.557105,19.732361,19.780088,12.846139,14.870222,7.612407,21.60579,14.538445,11.101003,10.543422,6.449103,12.952701,11.157599,14.460638,13.619735,6.056847,14.770458,6.754281,8.354461,15.369667,14.99511,15.791464,12.268379,13.780889,6.111574,17.393823,13.89149,14.498418,5.72488,7.060853,3.638415,3.093104,3.49636,3.45035,4.884559,2.84163,2.677529,4.700455,3.727354,4.490606,1.223942,1.761998,0.809102,1.324733,1.534502,0.610465,1.636815,3.988179,7.643403,7.140942,13.181953,5.20241,0.915386,0.321613,3.501804,2.805552,1.85151,0.395945,1.745675,0.376361,1.759647,2.444924,2.790657,0.298806,0.346096,8.59038,7.046067,17.181607,3.275459,14.235925,8.106243,0.674284,1.171153,4.513043,2.692111,26.815801,5.109551,2.662907,8.558169,3.807513,0.537653,17.310316,0.334126,8.479724,0.354249,2.307526,3.725471,0.085397,0.044533,0.116986,0.214748,0.058973,0.047886,0.104208,0.063584,0.102902,4.612871,0.401176,2.866358,0.040482,0.068261,0.016217,24.778018,23.728139,22.455792,28.332718,5.981291,1.621749]),
array([26.190158,6.665743,6.979611,11.576686,11.070694,12.685212,12.744557,5.041223,15.715868,5.895962,13.596575,13.456533,11.491826,9.207796,11.765186,16.188469,4.955979,11.599995,13.25664,12.393292,11.145412,11.679028,13.077891,13.28216,11.304238,3.444445,0.01998,0.070219,1.92496]),
array([9.181187,7.052029,9.083416,4.229367,2.272717,3.563462,4.710607,3.740233,4.099415,4.214499]),
array([10.26064,2.657374,4.931986,4.66401,2.760421,2.154593,2.667524,3.085488,3.151556,2.467048,1.061425,0.602731,0.435228,0.901308,0.717859,0.93642,0.890629,1.706942,0.292169,0.41305,0.90028,1.364158,0.701273,0.017146,3.300712,3.207258,3.409444,2.725257,2.195268,2.708445,3.3773,3.458492,3.419992,3.042601,2.879738,0.841709,0.001549,1.05879,1.858508,4.846564,4.110962,1.945305,0.010922,0.00791,0.011559,2.01681,0.002302,0.009439,0.007888,0.605624,0.339084,2.307602,1.607321,1.798044,0.004842,0.003782,0.010779,0.006277,2.573854,0.002261,1.095969,2.165434,0.002378,19.709871,3.228461,3.213724,1.068524,1.934132,3.64564,2.28107,2.492239,1.8249,2.072127,1.605528,2.12725,0.649141,0.725058,1.747361,5.276218,0.034026,0.517353,2.880751,2.833671,0.968564,1.173267,1.495735,2.327779,1.089753,0.816096,1.733982,1.915807,0.938972,1.581352,0.829951,1.050731,1.808315,2.545927,1.257091,2.402034,1.960641,0.657114,0.578985,2.724953,0.374013,0.42423,0.350775,2.112154,2.743066,2.956941,2.987777,3.119698,1.902955,2.00507,0.975172,2.077213,0.314557,0.24256,3.765396,3.83345,0.778931,0.03541,1.689843,2.16191,0.896489,2.003449,0.065855,0.025549,2.301559,4.878243,3.425159,3.192619,1.603729,2.086301,3.414492,5.218435,3.885663,3.919736,1.891718,0.820097,1.899664,0.483397,2.823123,0.606845,7.941832,2.616942,2.483497,1.835914,1.983682,1.381485,1.94071,1.910103,0.757785,2.380104,0.577066,0.489049,0.704683,0.314642,0.381041,1.204354,0.324755,0.313136,0.392136,2.473361,0.842933,1.913485,2.825392,2.736401,3.155021,2.167101,0.843773,2.196539,1.699899,0.819116,0.617178,0.515112,0.169931,0.276513,0.236243,0.448914,0.671565,0.189342,0.141229,4.208222,4.65381,2.325556,1.707302,2.049256,2.51716,2.250497,0.705813,2.096806,0.758367,4.646573,4.71403,3.81428,3.955588,3.200708,3.241576,3.855648,4.871239,4.856626,1.893935,1.387645,1.780505,0.304879,0.100382,0.02553,0.120213,2.573476,1.65918,0.090988,0.110591,0.003834,0.118111,1.547936,2.603491,3.505193,0.91949,2.27685,1.129626,0.033164,0.082652,0.125947,0.06423,0.122577,0.10683,0.183958,1.510314,6.963136,4.742899,0.05887,0.026014,1.172546,0.09179,3.91287,0.078187,0.007963,0.741988,0.464566,0.002911,0.008585,0.002439,0.001971,2.851844]),
array([0.543998,0.620276,0.30585,0.033834,0.102234,0.672424,1.360065]),
array([0.009434,0.004917,0.673221,2.032184,2.707664,1.871903,0.680892,0.496594,0]),
array([0.083365,1.218199,0]),
array([1.260778]),
array([1.296823,1.121853,0.876103,0.776535,1.552359,0.564727,0.667512,0.31706,1.482732,1.678734,0.496869,1.279436,1.185052,0.065721,0.671083,0.403402,1.451484,0.837632]),
array([0.003773,1.135899,1.273052,2.415257,1.573123,0.003846,1.332595,2.467372,2.107886,2.721149,0.637993,0.401745,0.614585,0.005527,0]),
array([0.506516]),
array([0.762363,1.338886,0.502663,1.461348,1.55562,0.692736,0.762438,1.018043,1.512285,0.018801,0.353397,0.248144,0.886641,1.679838,1.645063,0.119293,0.080457,0.091995,0.085979,0.087363,0.050615,0.034652,0.225188,0.041598,0.09235,0.114736,0.112044,0.032903,0.069782,2.356166,0.039574,0.957868,0.03216,0.071302,0.08375,0.060276,0.102659,0.764181,0.119769,0.049309,0.1177,0.044605,0.220483,0.084141,0.212379,0.06498,0.053949,0.057139,0.068727,0.039686,1.144556,0.021867,0.092499,0.058424,0.070996,0.09928,0.036526,0.04644,0.04565,0.243699,0.023345,0.024988,0.024961,0.121928,0.120076,0.08167,0.09595,0.064507,0.019047,0.888171,0.452178]),
array([2.235614,2.076774,1.45568,1.369633,1.469289,1.204247,2.85681,1.600184,1.337717,1.551573,1.567069,0.892135,4.347157,0.647433,1.634634,1.173287,0.526053,1.658565,2.202107,3.873915,2.118142,1.917661,1.283571,0.880386,0.370465,0.972414,1.44271,0.633208,0.415198,15.971383,2.561599]),
array([0.003331,0.336758,0.006152,0.002151,0.006457,0.002805,0.007113,0.010896,0.009737,0.040724,0.001084,0.007246,0.001186,0.008817,0.005193,0.002965,0]),
array([7.349873,7.322064,8.138259,8.477323,2.370401,2.333642,2.880206,2.159295,4.452906,4.700786,3.220674,4.679152,7.060662,4.954883,7.689069,9.214255,3.104739]),
array([0.737749,4.691236,3.654055,4.113032,3.751805,2.220496,2.510055,4.359275,3.549949,3.407722,0.645759,0.800185,1.186295,1.773404,1.781563,0.552732,1.522302,0.98263,1.500652,0.769071,0.951626,0.409065,1.601935,0.516811,0.432082,1.39855,1.161103,1.030966,1.797136,1.189881,1.660545,1.118386,1.723792,1.612074,0.3917,0.937844,1.736584,0.489653,0.190878,1.622161,1.679994,0.871837,0.396688,1.072852,1.239713,0.096443,0.032311,0.049136,0.028369,0.030333,0.015041,0.034377,0.103238,0.111414,0.122004,0.073887,0.106085,0.024575,0.066534,0.054694,0.01131,0.091952,0.121756,0.038188,0.00828,1.598598,0.103247,0.085385,0.101466,0.015806,0.110272,0.091042,0.093724,0.094976,0.084923,0.065424,0.001884,0.055356,0.077605,0.062806,0.027042,0.042661,0.251538,0.270845,0.013522,0.089374,0.061843,0.118589,0.108811,0.631222,0.332985,2.304774,0.966196,1.493294,0.001318,0]),
array([9.188986,3.894267,3.854574,2.17283,4.252539,1.810688,4.304903,1.947356,3.46026,3.665573,3.46103,2.207497,1.996212,2.053472,2.615752,3.601602,3.755139,3.917502,4.015667,2.979621,2.919924,2.088452,3.824924,3.393126,3.656328,3.139947,2.253887,4.420147,4.429716,2.23528,4.478375,2.369167,2.922239,2.631828,4.11009,0.099941]),
array([0.366419,0.993765,0.870004,1.743847,0.048584,0.12043,0.117807,0.014899,2.141469,2.051822,1.019824,0.946267,0.703904,0.351124,2.806458,1.958655,0.231363,0.304773,0.366178,0.71274,0.657312,0.603103,0.42304,2.08634,1.904492,1.997271,0.07992,0.382366,0.146739,0.621545,0.036421,0.035399,0.116477,0.051978,0.075624,2.090594,0.673768,0.267912,0.463598,0.245161,0.297199,0.51946,0.775899,0.116266,0.463075,0.115602,0.420937,2.124817,0.05489,0.504616,0.622056,0.688361,0.725263,0.762468,0.585057,0.454535,1.729967,0.508003,0.29254,0.147106,1.515337,0.440046,0.006775,0.006064,2.403032,0.264518,3.385334,0.084797,0.078108,0.084285,0.119067,0.080344,0.05231,0.047223,0.069779,0.066691,0.095598,0.05902,0.069981,0.123557,0.10814,0.078907,0.012721,0.017205,0.08754,0.042144,0.083379,0.051579,0.040062,0.082501,0.1685,0.029136,0.035367,0.081489,0.001859,0.001078,0.008998,0.918464,0.091249,0]),
array([1.448753,4.208221,1.510805,0.009838,0.006316,3.47194,2.039113,1.16541,2.771508,2.2464,0.842849,0.00874,2.029715,0.651801,0.009363,0.3508,1.245043,1.291132,2.315169,2.530839,0.22868,0.355322,1.43632,2.04732,5.308482,1.315624,2.586198,1.297144,2.00228,2.106793,3.92858,1.274734,0.876085,0.11835,0.57709,2.365181,2.249533,5.261044,0.700849,4.099618,1.572268,1.636961,0.009749,0.064375,0.10456,1.786224,0.950361,0.087681,0.086532,0.195629,0.491909,1.662441,0]),
array([2.345809]),
array([3.105546,2.268256,3.173375,0.856303,2.048997,0.41251,0.107224,0]),
array([2.802991]),
array([15.725679,22.021729,15.035737]),
array([12.186541,11.896,15.811383,14.026335,15.721688,14.926457,14.192038,14.796179,14.30711,15.505846,14.693887,14.498717,15.56112,15.924146,9.309611,15.259345,15.900732]),
array([4.93405,6.658076,7.71301]),
array([12.934067,10.388043,11.443513,11.989537,10.387176,12.017116,11.397379,12.671287,13.010859,17.571865,16.019006,12.796528]),
array([11.509968,11.553415,11.631245,13.166767,11.00983,11.920012,13.230818,13.029164,5.318527,14.938212,15.710959]),
array([2.634327,3.253712]),
array([6.034695,3.822986]),
array([0.009082,0.120617,0.029283]),
array([44.675224]),
array([2.470851]),
array([0.99597,1.690574]),
array([3.02147,2.701546]),
array([30.154833]),
array([27.842942,20.797177,28.557229,22.268173,23.556904,12.848472,21.659339,21.017692,25.950204,25.15655]),
array([25.275948,20.975877,22.030657,22.867606,21.71885]),
array([1.813749]),
array([0.263451,0.739733,0.693561,0.667285,0.705273,0.443533,0.310656,0.772066,0.176647,0.224941,0.633724,0.049113,0.273701]),
array([0.051051,0.231495,0.067625]),
array([25.99657,21.982467,22.840285,22.153568,21.696288,21.638979,18.997609,18.789391,18.344498,16.11142,16.616234,16.411068,18.180141,16.451851,19.456333,17.804438,17.549181,18.747934,17.123033,16.34189,19.328526,20.226384,18.819194,19.22661,17.80028,19.540338,18.010253,16.323944,13.717222,19.84673,18.679504,18.856883,16.614248,16.540683,16.741135,16.29294,19.859289,16.385791,16.428038,17.624246,18.891143,17.726117,13.919995,14.960378,15.864894,14.595655,20.534003]),
array([18.696689,18.648686]),
array([10.557633,18.566927]),
array([23.037228]),
array([21.271072,21.756664,26.507805,30.56893,28.042688,22.242968]),
array([22.555931,20.912486,22.660323,22.862308]),
array([29.359201,29.602375,27.913249,28.922095,29.980551,26.891763,26.540558,30.713776,30.14525]),
array([20.240149,20.100945]),
array([12.602119,14.912895,19.185508]),
array([13.093667,11.938301,18.089209,12.289453,10.697001,11.82865,11.158871,11.094113,10.514595,10.969287,13.687396,11.808349,11.126845,13.109789,11.03941,10.049721]),
array([14.223406,14.7897,14.261859]),
array([14.632111,20.280328]),
array([15.584758,14.734565,14.39299,13.779551,15.464279,14.997214,15.03999]),
array([10.763965,11.873146,11.986293]),
array([14.524477]),
array([23.523829]),
array([31.797542,31.636459,31.981417,31.737025,32.6629,31.272756,31.718118,31.480812,23.28891,27.321917,25.535483,25.872687,30.211064,30.63336]),
array([29.158611,30.974936,33.295418,37.834025,36.234693,34.920454,36.288119,53.367317,32.400672]),
array([35.370649,33.944899,37.210667,36.807957,37.506075]),
array([1.928521,0.256657,0.734522,0.1272,0.05191,1.072649]),
array([0.093529,0.241105,0.830945,0.084667]),
array([20.986736]),
array([18.675337,18.447257,18.547206,16.308739,18.264798,20.188758,18.242623,19.158413]),
array([22.38012,22.649783,23.595696,22.352008,24.665511,22.158573,22.571046,20.819263,29.823754,24.068108,22.3088,23.291994,23.783546,23.056024,22.995766,23.845696,21.396575,21.167064,24.676016,23.798932,23.492615,18.342947,18.264268,18.207813,17.375107,18.887001,17.568197,19.048716,16.873739,17.266673,29.158987,16.085115,19.058293]),
array([0.008034,0.008785,0.113929,0.933519,0.011024,0.002738,1.589927,0.03356]),
array([0.071077,0.04137,0.102248,0.055157,0.025896,0.096062,0.281913]),
array([0.014409]),
array([0.747046]),
array([33.016551,20.645077]),
array([30.705729]),
array([19.271693,17.72194,16.48842]),
array([31.394151,28.514861,25.389667,20.472098,23.889848,25.597503]),
array([20.78383]),
array([25.803341,22.479289,25.041205,26.724252,22.185651,23.739797,24.266257,22.364471]),
array([28.452142,29.777871,30.693336,25.578543,24.851285,29.412392,28.686888,25.285416,20.582922,25.012909]),
array([23.994622,25.367273]),
array([5.905847,6.224319,11.405481,9.690089,5.684142]),
array([5.00278]),
array([17.23554,6.062467,8.050231,16.580529,9.729977,7.421755,9.45721,11.448582,12.843982,10.484565,7.289136,9.198115,8.775495,12.712462,12.098603,10.520509,10.162265,12.221971,11.164752,12.602421,8.174982,12.812473,12.741781,8.82995,4.973138,11.015642,10.577678,14.707685,8.343804,7.695249,13.597993,14.784851,12.641783,11.750263,12.939332,8.825112,12.492811,9.57453,12.28654,7.024672,6.25491,7.174759,10.981917,6.969959,6.548635,5.010615,11.270358,21.897366,14.249727,12.701607,7.395165,11.630716,4.957262,8.834313,11.639007,11.852931,8.906316,12.311881,14.225172,12.290867,7.654003,22.302941,11.55251,10.489249,14.37076,10.059736,13.609628]),
array([12.425571,8.338048,6.814171,10.770574,13.302454,13.333777,11.987324,7.580702,8.053785,10.24603,11.863253,10.65978,13.480216,11.724635,13.452154,11.741836,11.372796,12.167583,12.540495,10.465906,12.454172,11.00682,11.134975,10.92802,12.969696,13.498593,13.32236,5.273107,8.962301,15.632065,10.061979,10.321519,12.044122,16.61589,11.165768,6.379157,11.560397,10.883987,12.424212,4.926077,12.931105,10.505981,10.995015,11.077808,14.86954,8.253484,21.914484,10.555478,10.977567,10.562292,12.408417,13.138405,11.49806,8.519389,10.227518,15.018077,14.72669,14.878516,14.805668,13.712701,15.016813,11.02441,18.465602,11.094556,8.4259,9.260693,12.086707,13.538203,8.440649,11.382034,11.769419,12.07477,11.723083,13.858876,9.855842,14.001376]),
array([9.377778,5.110111,10.575186]),
array([8.536359,5.441422,5.661311,6.832112,8.340903,5.825077,6.687338,9.006958,7.987654,11.631117,7.907764,9.789505,6.0571,9.490882,5.084372,7.218335,5.463272,4.186509,5.328867,7.3415,7.941841,8.844442,6.894429,5.211533,8.826028,9.996646,7.242103,7.085857]),
array([10.811563]),
array([14.131836,17.479117,16.268852,13.977981,14.307936,14.405979]),
array([16.486369]),
array([8.764581,13.106893]),
array([43.96772,36.629011,37.046221,35.009494,37.150066,34.903513,34.057398,35.346999,36.951899,36.123251,35.280587,35.000009,35.174221,34.971807,34.733209,35.227219,35.636715,33.516731,33.615736,33.709499,33.527016,33.642168,33.444442,33.887717,33.322759,33.771838,33.791727,29.204584,30.855271,31.410791,32.832067,32.089631,31.330225,28.275711]),
array([33.847439,33.357226]),
array([37.878864,34.541956,36.003478,36.394203,36.759627,36.604231,35.911689,36.29859,35.007878,35.071825,34.253174,36.523143,36.713425,35.093543,36.798971,36.091437,34.801784,34.086843,35.269687,36.780121,35.874232,37.15016,35.782448,36.607749,34.848895,36.886118,36.388693,35.529559,37.041187,35.835213,34.793602,34.391504,34.35113,33.93073,37.10338,34.180399,36.509508,35.211085,33.442323,33.61618,33.611709,33.605192,33.768778,33.574654,33.540011,33.413233,33.433733,33.362325,33.535278,33.759814,33.454193,33.62414,33.874572,33.470344,33.390598,33.416929,33.382746,33.496659,33.854933,33.670375,33.792115,33.37778,33.524517,33.786353,33.543779,33.595734,33.790983,33.813317,33.71602,33.798999,33.337877,33.616705,33.808317,33.82694,33.774974,33.567136,33.471948,33.425264,33.742376,33.605813,33.777703,33.365747,33.45573,33.787579,33.347884,33.558518,33.359532,33.352179,33.804602,33.609769,33.744143,33.671225,33.705163,33.564807,33.705938,33.621843,33.645085,33.60053,33.612477,33.54452,33.378508,33.803436,33.482788,33.694142,33.5103,33.717739,33.698428,33.417787,33.595109,33.511851,33.467617,33.331912,33.777742,33.859138,33.310551,33.460427,33.671968,33.394289,33.7648,33.873224,33.586678,33.870418,33.540307,32.356626,32.162776,33.238282,31.404276,32.293626,32.538007,32.159864,35.589251,35.986723,33.874865]),
array([29.522788,22.971059]),
array([22.85382,24.064217,14.484766,15.164419,15.624309,12.872391,12.088826,19.023246,14.017699,10.551946,16.250463,30.32363,14.684793]),
array([24.988856]),
array([28.643808,23.675032,26.860662,27.455033,27.685596]),
array([24.347099,22.830136,22.00339,21.315569,23.027787,24.547551]),
array([13.739851,19.154349,18.318708,18.600071,19.077906,21.170889,18.522636,18.778685,17.278968,18.78019,17.797851,19.735103,19.734871,18.343371,15.020924,14.167318,13.71428,14.40851,14.942508,15.298406,15.750225,14.39687,15.449832,15.762193]),
array([11.927845,11.810595,11.672825,13.001834,12.84756,10.353266,10.516809,13.593608,12.758812,6.405377,10.748038,11.910008,13.538529,12.504711,12.461422,11.775608,13.39804,13.577108]),
array([27.40082]),
array([11.632114]),
array([13.692029,14.379228,16.000597,12.363781,14.884737,15.548445,12.817266,15.449574,13.634186,14.555156,14.533277,14.820956,15.918014,13.826082,14.836038,14.534468,14.581781,11.144182,14.660806,14.476027,14.726888,11.832633,15.898144,12.722647,12.319099,13.853635,10.914545,13.083937,11.987701,14.277207,15.888096,14.244929,15.935376,15.420871,15.46277,12.090088,12.738927,12.879082,11.264084,13.074741,12.136111,13.353832,14.963028,11.976819,14.799374,9.077327,10.886103,16.01572,7.661252,11.843988,11.624226]),
array([22.533217,16.396182,27.434104,19.518708,17.808932,23.927809]),
array([1.782915,2.573108,1.557526,1.421211,2.080201,0.369963,3.168903]),
array([0.005651,1.547816,1.050145,0.675023,2.381777,2.020317,0.28829,1.0302,0.0971,0.099648]),
array([21.889755]),
array([29.440273,21.930038,22.486922,25.348926,23.847946]),
array([21.128594,22.245605]),
array([33.358101,31.618805,32.717107,31.949889,31.250636,31.929616,31.985067,31.921146,31.185867,32.03098,32.303989,33.237059,30.91652,30.962993,26.774363,27.380411,26.438713,27.778722,29.393852,23.215549,23.532889]),
array([5.08095]),
array([13.013672,9.295285,12.29627]),
array([8.794286,6.221469,8.06922,8.25871,12.7026,20.757918]),
array([20.387368]),
array([18.276758,20.105464,16.225602,20.12875,16.97551,18.665711,19.505744,19.6682,19.771186,18.406632,17.919802,19.694723,16.812666,19.001334,16.156488,17.933191,18.300584,17.915556,19.379862,18.475926,16.35662,17.292403,18.319034,20.090661,16.88335]),
array([17.896982,13.76319,17.468473,17.420003,18.172769,16.485506,18.422294,17.742084,13.846388,15.438783,11.364892,22.495121,14.301393,19.49599,13.757416,13.549338,13.949284,15.303666,15.172607,15.21959,15.262768,15.890076,15.141387,15.697868,15.843805,14.175294,6.958847,14.161446,15.172489,15.538327,15.245762,14.102827,14.77584,15.589587]),
array([40.404007]),
array([4.607133,0.450682,3.977193,3.516458,0.180644,2.770989,2.589301,0.932892,3.604597,5.028525,4.582327,2.658156,0.992231,3.671111,4.102293,4.874167,2.170724,3.006205,8.223789,5.061613,3.816179,3.648595,2.397186,2.955586,2.199744,2.039773,2.162411,2.018656,3.172409,2.554703,4.028829,1.931612,1.419921,4.651269,3.858116,2.593267,2.14999,1.059855]),
array([2.62773,2.740597]),
array([0.029747,0.032972,0.090323]),
array([22.047586,18.741562]),
array([15.125521,18.254377,17.134973,18.621712,17.099259,18.622652,16.127857,19.505748,19.063503,15.452666,15.562395,14.822759,13.913061,15.79688]),
array([16.93039,19.161108,21.954375,17.872347]),
array([33.591699,32.94494]),
array([19.137646,19.17873,20.155091]),
array([32.895016,31.398336,21.774576]),
array([27.617989]),
array([26.146589,24.152616,20.704949,23.438123,29.569443,26.396469]),
array([33.662702,33.651455]),
array([0.4979,0.222054,2.925466,1.309374,0.125088]),
array([0.001432,0.001443,0.051115,2.16199,2.518233,2.410232,0.113644]),
array([32.349274,33.054087]),
array([33.214557,31.696522,32.85238,31.883448]),
array([18.767701,17.860923,6.761241,19.0866,18.431699,22.68203,16.619909,18.043565,19.976482,20.414097,15.562845,14.762666,8.848373,7.508271,13.702854,14.669478,15.803503,15.580052]),
array([16.305192,19.380657,19.944327,15.5445,20.161888]),
array([24.930181,26.709112,26.461079,24.360818,27.985784,23.100326,22.128177,21.290381,23.797976,22.916952,24.617022,25.179259]),
array([23.468772,22.602525]),
array([22.509665,23.817531,21.792474,23.025009,22.520599,20.476161,20.961011,24.792787]),
array([10.501341,12.565183,13.036384,6.103815,12.937145,13.166451,10.971456,12.195992,10.465936,12.571321,13.05335,11.8458,10.911421,12.798915,10.462876,11.26317,12.902897,17.991135,13.051871,11.570125,11.456813,12.638602,13.329891,12.27637,12.58765,11.464654]),
array([15.500054,14.696282,15.889014,15.072893,15.609512,14.578361,13.627925,14.37731,13.841458,13.653065,14.798893,15.368077,13.67742,14.714957,15.453398,7.114342,13.755874,15.757755,18.352041,14.875237,15.836231,15.010498,15.217526,15.057684,14.22648,20.817845,14.749198,14.345108,15.352349,15.277769,14.008444,14.748403,15.763042,14.658536,13.628108,22.499483,19.307995,13.812911,15.955937,15.20376,15.945413,14.000591,14.230337,15.878139]),
array([24.061289,29.782855,28.885315,28.026643,27.395068,30.486571,28.802041,22.995549]),
array([24.409236,23.744309,17.918537,17.119768,24.360965,17.723825,19.049457,19.628804,20.861384]),
array([21.732977]),
array([20.644818,20.961244,22.631698,20.928475,23.394347,22.950107,21.811373,24.074185]),
array([31.783506,29.690686,25.308102]),
array([23.810828,21.711964,15.97549,19.645475,18.90228,16.286826,17.317919,19.651928,16.136585]),
array([16.666839]),
array([16.895593,18.431789,20.3736,20.055735,17.00706]),
array([30.626162,25.712334,22.524645,24.344405,23.747826,20.537226,21.473935,24.430141,23.759257,23.56164,23.789436,16.609069]),
array([23.500793]),
array([26.550463,27.294018,27.516533,22.353567]),
array([16.546333]),
array([33.643066]),
array([13.864054,14.821133,15.340931,15.068531,14.560481]),
array([0.328052,0.696031,2.03678,0.085593,0.813927,0.039673,0.095345]),
array([0.28547]),
array([1.713484]),
array([0.364512,0.110213,0.039745,0.094961,2.022961,0.355585,0.018708,0.095588]),
array([18.968178,17.139603,15.994839,17.645988,16.461281,16.510281,16.74357,18.927188,17.099648,19.721,19.731455,18.751588,18.149807,18.8024,16.250197,17.831498,16.019727,18.248374,17.872983,19.535884,14.708029,16.839602,17.912704,19.302938,14.977089,14.327274,6.931298]),
array([15.322399,18.748982,19.178903,14.671733]),
array([0.001693,2.486726,0.416555,0.556159,0]),
array([21.589868,30.735203,23.065319]),
array([1.231741]),
array([0.010253]),
array([29.869133,26.885781,29.341053,27.334339,26.453118]),
array([15.859566,15.819538,7.39168]),
array([0.112297,0.896687,0.505625]),
array([4.269048,3.929674]),
array([14.790585,15.913279,14.492439,15.208855,10.907789]),
array([18.372154,16.263756,16.543621,20.025974,14.80255,20.385785,19.680152,20.29608,20.187735,17.630956,17.756471,14.414647,13.914305,22.438214,22.044787,15.505958,14.465226,19.237412,19.899295,15.355516]),
array([16.00217,16.716184,19.425758,15.063201,19.20919,19.275482,17.470971,18.767449,19.930149,19.990766,16.753055,15.326572,16.944839,18.371164,20.282786,17.11489,14.608421,15.668192,15.883631,14.359176,15.94355,15.252386,13.609406,15.008659,14.722939,15.747065,14.721609,15.635778,15.282367,15.151068,13.760608,14.452708,14.984369,20.260725,14.259047]),
array([1.939579,1.320304,1.705818,1.414266,0.037007,0.04519,0.099834,0.086546,0.159125,10.985738]),
array([4.710067,1.736602,1.2409,1.168467,1.527035,1.701835,1.158441,0.232023,1.389392,0.01634,0.032639,0.112168,0.120058,0.117147,0.477842,0.029789,0.0288,0.082826,0.118801,0.044183,0.031991,0.084223,0.046553,0.025624,1.485278,0.054638,0.010426,0.020798,0.056268,0.041764,0.02605,0.083047,0.121927,0.097912]),
array([3.758091]),
array([1.843765,4.104986,2.350589,2.939742,1.940123]),
array([0.498629,1.452759]),
array([2.055885]),
array([6.790288]),
array([7.88771,6.948678,6.702564,9.385978,1.811766,1.746702,1.575271,0.532515,1.132742,1.797973,1.324752,0.917305,0.310414,0.416948,0.028993,0.678507,4.515824,4.891859,0.645111,0.997489,1.472469,3.078106,1.215989,0.034231,3.437521,4.767996,3.380282,1.29415,2.505561,1.81745,0.47847,0.676174,4.380169,2.909706,2.713296,2.797338,2.232318,2.314607,1.716304,0.609619,0.815201,0.824562,0.357688,2.032751,1.299804,1.084054,2.61477,2.208934,3.178781,3.039822,3.132818,3.163387,2.717219,5.218041,2.383749,1.939444,1.061402,1.040906,0.37096,0.426837,1.504027,2.389973,0.206611,1.386396,2.39689,4.692489,0.089046,2.299056,1.811642,1.008365,1.627256,1.9561,3.50013,7.051393,5.056779,1.851209,2.34411,0.408297,4.343734,0.118204,0.049065,0.031326,0.762572,0.182647,2.380953,0.491718,0.414474,1.058253,3.887821,2.752139,2.088002,1.017932,0.721257,0.258263,0.345712,2.384233,0.636369,3.501553,3.834331,0.025404,1.586796,0.035429,0.058637,0.085985,3.644598,0.81154,3.464634,0.099709,0.07402,0.025455,2.036052,4.213738,2.228384,0.369333,0.098868,0.011373]),
array([0.110447]),
array([0.009565,0.846922,0.009956,0.451274,0.008157,0.005408,0.002348,2.295137,0.011635,0.009745,0.001918,1.006278,1.892333,1.842894,1.136739,0.298786,0.08269,0.787348,1.210864,0.799388]),
array([13.385246]),
array([4.79002]),
array([7.910832,7.151903,5.70234,8.914701,13.214134,5.121805,10.058918,8.038942,8.555183,7.694462,5.720708,1.185508,8.215536,6.883988,6.905123,5.438188,8.685102,9.196745,9.562892,10.172882,15.322341]),
array([2.915344,1.67782,0.469047,1.150335,1.348456,1.234013,0.825338,1.477343,0.90077,0.050349,0.117171,0.041023,0.032917,0.095722,0.076748]),
array([1.23013,1.067393,1.00642,1.723425,0.088555,0.097731,0.081581,2.232559,0.823875,0.576726,0.172892,0.449732,0.022133,0.603382,0.059867,0.588123,0.434011,0.199181,0.568553,2.792028,1.22317,0.112253,0.179225,0.650058,0.084497,0.517601,0.890936,0.718517,0.066794,0.544057,0.392155,0.275812,2.555288,2.04721,0.958928,0.04508,2.114181,0.731779,0.665288,0.287468,1.512671,0.333962,0.083857,0.092851,2.086151,0.037424,0.107526,0.054963,0.018576,0.016266,0.019877,0.036269,0.10866,0.070666,0.111936,0.047952,0.079748,0.109877,0.111181,0.876125,0.083786,0.004149,0.001851,0.0027,0.023617,1.386742,0.101388]),
array([0.119523]),
array([0.110994]),
array([0.332584,1.734127,0.329093]),
array([0.511486,1.348691,0.436797,2.582174,0.272372,1.241167,0.332377,1.529976,0.241335]),
array([0.576757])
]

d=[data_1]
names=[ 'canid_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aelurodon','Aelurodon_asthenostylus','Aelurodon_ferox','Aelurodon_mcgrewi','Aelurodon_montanensis','Aelurodon_stirtoni','Aelurodon_taxoides','Aelurodon_wheelerianus','Alopex','Alopex_lagopus','Archaeocyon_falkenbachi','Archaeocyon_leptodus','Archaeocyon_pavidus','Borophaginae','Borophagus','Borophagus_diversidens','Borophagus_dudleyi','Borophagus_hilli','Borophagus_littoralis','Borophagus_orc','Borophagus_parvus','Borophagus_pugnator','Borophagus_secundus','Caedocyon_tedfordi','Canidae','Caninae','Canini','Canis','Canis_(Pseudalopex)','Canis_adustus','Canis_anthus','Canis_apolloniensis','Canis_armbrusteri','Canis_aureus','Canis_cedazoensis','Canis_dirus','Canis_edwardii','Canis_familiaris','Canis_ferox','Canis_latrans','Canis_lepophagus','Canis_lupus','Canis_mesomelas','Canis_proplatensis','Canis_rufus','Canis_thooides','Carpocyon','Carpocyon_compressus','Carpocyon_limosus','Carpocyon_robustus','Carpocyon_webbi','Cerdocyon_avius','Cerdocyon_texanus','Cerdocyon_thous','Chailicyon_crassidens','Chrysocyon','Chrysocyon_brachyurus','Chrysocyon_nearcticus','Cormocyon','Cormocyon_copei','Cormocyon_haydeni','Cubacyon_transversidens','Cuon','Cuon_alpinus','Cynarctoides_acridens','Cynarctoides_emryi','Cynarctoides_gawnae','Cynarctoides_harlowi','Cynarctoides_lemur','Cynarctoides_luskensis','Cynarctoides_roii','Cynarctoides_whistleri','Cynarctus','Cynarctus_crucidens','Cynarctus_galushai','Cynarctus_marylandica','Cynarctus_saxatilis','Cynarctus_voorhiesi','Cynarctus_wangi','Cynodesmus_martini','Cynodesmus_thooides','Cynodictis','Cynodictis_lacustris','Cynotherium','Cynotherium_sardous','Desmocyon','Desmocyon_matthewi','Desmocyon_thomsoni','Dusicyon','Dusicyon_avus','Dusicyon_culpaeus','Dusicyon_sechurae','Ectopocynus_antiquus','Ectopocynus_intermedius','Ectopocynus_simplicidens','Enhydrocyon','Enhydrocyon_basilatus','Enhydrocyon_crassidens','Enhydrocyon_pahinsintewakpa','Enhydrocyon_stenocephalus','Epicyon','Epicyon_aelurodontoides','Epicyon_haydeni','Epicyon_saevus','Eucyon','Eucyon_davisi','Eucyon_skinneri','Euoplocyon_brachygnathus','Euoplocyon_spissidens','Gobicyon','Hesperocyon','Hesperocyon_coloradensis','Hesperocyon_gregarius','Hesperocyoninae','Leptocyon','Leptocyon_delicatus','Leptocyon_douglassi','Leptocyon_gregorii','Leptocyon_leidyi','Leptocyon_matthewi','Leptocyon_mollis','Leptocyon_tejonensis','Leptocyon_vafer','Leptocyon_vulpinus','Lycaon','Lycaon_pictus','Mesocyon','Mesocyon_brachyops','Mesocyon_coryphaeus','Mesocyon_temnodon','Metalopex_bakeri','Metalopex_macconnelli','Metalopex_merriami','Metatomarctus','Metatomarctus_canavus','Microtomarctus_conferta','Neovulpavus_washakius','Nyctereutes','Nyctereutes_abdeslami','Nyctereutes_procyonoides','Osbornodon_brachypus','Osbornodon_fricki','Osbornodon_iamonensis','Osbornodon_renjiei','Osbornodon_scitulus','Osbornodon_sesnoni','Osbornodon_wangi','Otarocyon_cooki','Otarocyon_macdonaldi','Otocyon','Otocyon_megalotis','Oxetocyon','Oxetocyon_cuspidatus','Paracynarctus_kelloggi','Paracynarctus_sinclairi','Paraenhydrocyon_josephi','Paraenhydrocyon_robustus','Paraenhydrocyon_wallovianus','Paratomarctus_euthos','Paratomarctus_temerarius','Philotrox_condoni','Phlaocyon','Phlaocyon_achoros','Phlaocyon_annectens','Phlaocyon_latidens','Phlaocyon_leucosteus','Phlaocyon_mariae','Phlaocyon_marslandensis','Phlaocyon_minor','Phlaocyon_multicuspus','Phlaocyon_taylori','Phlaocyon_yatkolai','Protemnocyon_inflatus','Protepicyon_raki','Protocyon','Protocyon_orcesi','Protocyon_tarijensis','Protocyon_troglodytes','Protomarctus_optatus','Psalidocyon_marianae','Pseudalopex_gymnocercus','Rhizocyon_oregonensis','Speothos','Speothos_venaticus','Sunkahetanka_geringensis','Tephrocyon_rurestris','Theriodictis','Theriodictis_floridanus','Tomarctus','Tomarctus_brevirostris','Tomarctus_hippophaga','Urocyon','Urocyon_cinereoargenteus','Urocyon_citrinus','Urocyon_galushai','Urocyon_minicephalus','Urocyon_progressus','Urocyon_webbi','Vulpes','Vulpes_cascadensis','Vulpes_chama','Vulpes_kernensis','Vulpes_mathisoni','Vulpes_stenognathus','Vulpes_velox','Vulpes_vulpes','Vulpes_vulpes_macroura','Vulpini','Xenocyon','Xenocyon_lycaonoides','Xenocyon_texanus']
def get_taxa_names(): return taxa_names
