store = {}
store['timestamp']=1622158119
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=27']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=27
store['worker_id']=27
store['num_workers']=40
store['config']={'seed': 1264, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.6338701248168945})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.453017473220825})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.331414222717285})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 4.04849910736084})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.894496440887451})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 4.011068820953369})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.211768627166748})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.207343101501465})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5943, 'crossentropy': 4.01021953125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.4202439785003662})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3776862621307373})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3326075077056885})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4188871383666992})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4821536540985107})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5005223751068115})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 27430], ['ood', 6434], ['ood', 4797], ['ood', 23178], ['id', 52147]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.2684127065751132, 2.1223675266634956, 2.6507163366324793, 2.914201227981277, 3.008794440010819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.258380651473999})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.655806541442871})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0584702491760254})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9626641273498535})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.191718816757202})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.492284059524536})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.7995688915252686})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.9363889694213867})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.421491861343384})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.424617052078247})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.7522835731506348})
store['active_learning_steps'][1]['training']['best_epoch']=8
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6435, 'crossentropy': 3.09168828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1365575790405273})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2081656455993652})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2335221767425537})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1821870803833008})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 5250], ['ood', 56746], ['id', 57276], ['id', 801], ['id', 30661]], 'labels': [-1, -1, 8, 8, 8], 'scores': [1.1385542639298882, 2.0680826369069623, 2.613602357897622, 2.846279343075235, 2.9316873797771477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.098764181137085})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.5017170906066895})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.8772382736206055})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.025289535522461})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7548394203186035})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6343, 'crossentropy': 2.6203296875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.180746078491211})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2268491983413696})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1748032569885254})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1686475276947021})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 4719], ['ood', 36557], ['id', 29211], ['ood', 13226], ['id', 56684]], 'labels': [-1, -1, 3, -1, 4], 'scores': [1.221406953354085, 2.1190503472005244, 2.6509773275222264, 2.9896457903381544, 3.1567909461283366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.9252287149429321})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.298889636993408})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.165501594543457})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.292296886444092})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.027984619140625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0539708137512207})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.558303117752075})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.290830612182617})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6363, 'crossentropy': 3.3283421875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2002155780792236})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1733372211456299})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.158797264099121})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1544971466064453})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2065421342849731})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 3848], ['ood', 45630], ['id', 4380], ['ood', 52131], ['id', 42214]], 'labels': [-1, -1, 0, -1, 4], 'scores': [1.271984505914645, 2.164534698292605, 2.72554555135714, 2.987190304912269, 3.082281503115844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.995502233505249})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.82450008392334})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0957345962524414})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.4049975872039795})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.9953737258911133})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.4290308952331543})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.8394103050231934})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 4.116347312927246})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.73789119720459})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6121, 'crossentropy': 3.45892734375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2599788904190063})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.261343240737915})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.292185664176941})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3104562759399414})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2531023025512695})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 33478], ['ood', 17252], ['ood', 49438], ['id', 49194], ['id', 48855]], 'labels': [-1, -1, -1, 2, 3], 'scores': [1.2410308218344346, 2.073091675792583, 2.649291674332888, 2.914705007246366, 3.034612998266253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.8803062438964844})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4020633697509766})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.866671323776245})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.108882427215576})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.262650728225708})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6251, 'crossentropy': 2.433435546875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2705020904541016})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.187699317932129})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.24530029296875})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2547554969787598})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 17317], ['ood', 16309], ['ood', 58788], ['ood', 4071], ['ood', 51610]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1305416787469174, 1.8801968020002793, 2.4310531651187626, 2.7840673628401715, 2.956454948461862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.8933194875717163})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.676037073135376})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.718339443206787})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.0260958671569824})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6345, 'crossentropy': 2.1053431640625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2267320156097412})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.172184705734253})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1635847091674805})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 22806], ['ood', 39129], ['ood', 42699], ['ood', 57459], ['id', 52498]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.0403828574870309, 1.7837992534025218, 2.328528661756743, 2.6568965838174465, 2.866501743563063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9200701713562012})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4972548484802246})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.051535129547119})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1597907543182373})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.4601941108703613})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.748565196990967})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.231485366821289})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.642528533935547})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6336, 'crossentropy': 3.497940234375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2257814407348633})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1552610397338867})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2747633457183838})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.308706521987915})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2706146240234375})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2262729406356812})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.359107255935669})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 17568], ['ood', 46600], ['ood', 29766], ['id', 28380], ['ood', 48323]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.2832052606422246, 2.169917948140962, 2.760098847948721, 3.043972356956119, 3.170558061596269]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6903072595596313})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3532700538635254})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9050793647766113})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.9103479385375977})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.2705464363098145})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.2608232498168945})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.2115659713745117})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.0664327144622803})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.1916942596435547})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6409, 'crossentropy': 3.1517015625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1850621700286865})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.228438377380371})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1273560523986816})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1624265909194946})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1897672414779663})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2540661096572876})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.187211036682129})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.199094295501709})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 48379], ['ood', 40249], ['ood', 35138], ['ood', 17902], ['ood', 742]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2271156813694315, 2.1061801050983067, 2.647085456651931, 2.922372770903734, 3.0519314275371006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.916448712348938})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.931100606918335})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0545058250427246})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.336601972579956})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6164, 'crossentropy': 2.2078048828125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2644685506820679})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1982545852661133})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2139527797698975})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 39046], ['ood', 40547], ['ood', 9383], ['id', 59115], ['ood', 44477]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.0418900017856565, 1.7117477839945288, 2.214410572787581, 2.538728958262948, 2.7428912551925997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.805354118347168})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.452209949493408})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0695011615753174})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.046260356903076})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.765119791030884})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.964311122894287})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.082470178604126})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.3142287731170654})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.3618502616882324})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.2456436157226562})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.5601601600646973})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6275, 'crossentropy': 3.457841015625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2550246715545654})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2064487934112549})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.240535855293274})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2956522703170776})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.239850401878357})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.357627272605896})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2097675800323486})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 36235], ['ood', 32074], ['ood', 44265], ['ood', 20932], ['ood', 8619]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2571087594565356, 2.2644394179829703, 2.844652577390168, 3.13962250469766, 3.2709969816899935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9733911752700806})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.3840649127960205})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6797802448272705})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7630255222320557})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9115118980407715})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.2193245887756348})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6299, 'crossentropy': 2.910112890625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.2544889450073242})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2512037754058838})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2508292198181152})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1891297101974487})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3094842433929443})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 48379], ['ood', 29132], ['ood', 20783], ['id', 59116], ['ood', 39668]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.171236624585637, 1.9913259074899652, 2.5496432210190623, 2.849154608980582, 2.9806254759998803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.7787911891937256})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.413400173187256})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6051688194274902})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.5763559341430664})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.825437068939209})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6406, 'crossentropy': 2.3670291015625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1553997993469238})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1152522563934326})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1055831909179688})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.138667345046997})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 15668], ['ood', 34189], ['ood', 24193], ['id', 39750], ['ood', 59453]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.1447968500624128, 1.963651274964909, 2.5421631983526733, 2.8780349603457136, 3.049719468540002]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.727931261062622})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.5520386695861816})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6793770790100098})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8505101203918457})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9306998252868652})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.092301845550537})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.4190924167633057})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6259, 'crossentropy': 2.87363203125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1820958852767944})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2046812772750854})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1684688329696655})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1888835430145264})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1479864120483398})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1628272533416748})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 54431], ['ood', 47488], ['ood', 19931], ['id', 16061], ['id', 3764]], 'labels': [-1, -1, -1, 4, 4], 'scores': [1.304731682991117, 2.2181688968768674, 2.8270494679079112, 3.1612573843596765, 3.2946334136925675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6759300231933594})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.090712785720825})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.411241054534912})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.5823097229003906})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.996320962905884})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9877591133117676})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6695, 'crossentropy': 2.4671701171875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1413674354553223})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0651748180389404})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0666985511779785})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0842251777648926})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0853674411773682})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 28742], ['ood', 32043], ['ood', 13096], ['ood', 21325], ['id', 25677]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.2406583923143495, 2.265115978820033, 2.9176502863376204, 3.167904206606063, 3.28768818544778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.5854650735855103})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.259944200515747})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.5793678760528564})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.66344952583313})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.1483824253082275})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0683915615081787})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.086585521697998})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.6296513080596924})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6606, 'crossentropy': 3.0551443359375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2226226329803467})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.2230470180511475})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1908433437347412})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1786539554595947})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2143566608428955})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2195560932159424})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 19577], ['ood', 15604], ['ood', 42414], ['id', 31627], ['id', 29183]], 'labels': [-1, -1, -1, 3, 2], 'scores': [1.2258230529655694, 2.060401553102158, 2.5921634825865496, 2.862697167691427, 2.963311979089143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9294304847717285})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.441734790802002})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8699288368225098})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.9353513717651367})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.4561901092529297})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6345, 'crossentropy': 2.415948828125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1515740156173706})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2141246795654297})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1989476680755615})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1993029117584229})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 33711], ['ood', 20081], ['ood', 12430], ['ood', 6936], ['id', 5319]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.0696484726026056, 1.85642846075296, 2.4230758848427607, 2.7498555939320593, 2.910670654844428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.628660798072815})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.1691389083862305})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1324217319488525})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.4914236068725586})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6459689140319824})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8753929138183594})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.241361379623413})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6548, 'crossentropy': 2.4982126953125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1811275482177734})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.163745641708374})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0879921913146973})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2064154148101807})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1911101341247559})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0961021184921265})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 34200], ['ood', 29132], ['ood', 42125], ['ood', 54034], ['ood', 11374]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1779079632550595, 2.0423184041279576, 2.616996410003244, 2.905851527544404, 3.013166357436223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.6485862731933594})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.2672054767608643})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6361405849456787})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7828307151794434})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.9551897048950195})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.8510894775390625})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6481, 'crossentropy': 2.5880126953125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1812973022460938})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1864817142486572})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1217232942581177})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.138563871383667})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.185011625289917})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 25662], ['ood', 54656], ['ood', 58973], ['ood', 2206], ['id', 23161]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.0654909149216727, 1.8995530363372675, 2.512969452870255, 2.8334187495258396, 2.960953373101699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.8209035396575928})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.2520408630371094})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2229180335998535})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.736764430999756})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.8243026733398438})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.4345788955688477})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.662, 'crossentropy': 2.37580546875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.170702576637268})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1624776124954224})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0878682136535645})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1136457920074463})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0988961458206177})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 13937], ['ood', 55034], ['ood', 25572], ['id', 32759], ['ood', 29975]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.1779592280867537, 2.088771967495722, 2.665184936508039, 2.9358724088788772, 3.0377982961057235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.6831388473510742})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.320858955383301})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.337523937225342})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.9899983406066895})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.217683792114258})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.02651309967041})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6598, 'crossentropy': 2.5205998046875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1427433490753174})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.099400520324707})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.100458025932312})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1156367063522339})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1263415813446045})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 11796], ['ood', 45840], ['ood', 14085], ['ood', 10391], ['ood', 2661]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1641101624180827, 2.060803387823635, 2.6340473252964918, 2.9625683113084635, 3.1305465714905196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.7119545936584473})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0039875507354736})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.411350965499878})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.627849578857422})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.680168628692627})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9732038974761963})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.773951530456543})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6639, 'crossentropy': 2.6318044921875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1405341625213623})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.173722743988037})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1768450736999512})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0954148769378662})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1845945119857788})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1860120296478271})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 57114], ['ood', 3200], ['ood', 45223], ['ood', 43478], ['id', 17027]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.170970919610075, 2.038207370619933, 2.66712688400258, 3.016770891929675, 3.164190763562809]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.5486440658569336})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.158597469329834})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.282688617706299})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.79536771774292})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.968937873840332})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.7749533653259277})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 2.479196484375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0833430290222168})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1824918985366821})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.165480375289917})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1066069602966309})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1742818355560303})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 33376], ['ood', 7556], ['ood', 15036], ['ood', 28931], ['id', 14930]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.0436352458479334, 1.8448923649462143, 2.391612637778456, 2.6601128134590972, 2.8116530983391375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.521416425704956})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.096123218536377})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.666553258895874})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.634148597717285})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.70703125})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 3.1240522861480713})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.184332847595215})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.9588699340820312})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 3.027163028717041})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.786264419555664})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 3.34735107421875})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 3.096802234649658})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 3.3111038208007812})
store['active_learning_steps'][23]['training']['best_epoch']=10
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6674, 'crossentropy': 2.9410259765625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2395305633544922})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2000651359558105})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1826791763305664})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1926095485687256})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2371481657028198})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2426857948303223})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1617517471313477})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2025344371795654})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2169101238250732})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2416253089904785})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 17886], ['ood', 30002], ['ood', 36152], ['id', 16245], ['id', 3895]], 'labels': [-1, -1, -1, 8, 8], 'scores': [1.1042176067989655, 1.9670545852627894, 2.5656165821145933, 2.877682292557262, 3.0176424814652565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.5319302082061768})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9041218757629395})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.448965072631836})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.741236686706543})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.7202110290527344})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.7503437995910645})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 3.087022066116333})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.891669273376465})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.651123523712158})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 3.1636009216308594})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 3.1295461654663086})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 3.0457401275634766})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 3.0392062664031982})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 3.572042226791382})
store['active_learning_steps'][24]['training']['best_epoch']=11
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6746, 'crossentropy': 3.0918109375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1982951164245605})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2474232912063599})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2263578176498413})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.166211485862732})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1916606426239014})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1719884872436523})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.206826090812683})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2272943258285522})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2553012371063232})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1380646228790283})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 6339], ['ood', 30740], ['ood', 8658], ['ood', 28599], ['id', 32878]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.2965312041612151, 2.2927590387794337, 2.9090645020425026, 3.1919946281031972, 3.2940651390162987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.6250860691070557})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.1513938903808594})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.511519432067871})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.6844499111175537})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 3.0120463371276855})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.1902880668640137})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6576, 'crossentropy': 2.4870314453125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2262723445892334})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1579644680023193})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2761366367340088})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1272220611572266})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.220172643661499})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 36599], ['ood', 25714], ['ood', 56481], ['id', 33207], ['ood', 1845]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.0331606521770467, 1.8423537576845472, 2.429226305799647, 2.767965964328649, 2.9151580836416695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5570127964019775})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.086106061935425})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.5886826515197754})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.615722179412842})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.865934133529663})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.7377352714538574})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.9053244590759277})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.8945279121398926})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5717201232910156})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6774, 'crossentropy': 2.8590173828125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1589528322219849})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3303766250610352})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3147287368774414})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.40720796585083})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.22508704662323})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.3545255661010742})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.441664695739746})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3140695095062256})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 50894], ['ood', 36842], ['ood', 56385], ['id', 6274], ['id', 765]], 'labels': [-1, -1, -1, 7, 9], 'scores': [1.0622688608516717, 1.9921145681988932, 2.5834286206880073, 2.8944900012131027, 3.0287130604186014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3286733627319336})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.7225675582885742})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.076082468032837})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.533768653869629})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.536923408508301})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.5561399459838867})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6885, 'crossentropy': 2.0894884765625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1135263442993164})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0884227752685547})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1277899742126465})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0750126838684082})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.165708065032959})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 36629], ['ood', 35746], ['id', 18773], ['ood', 22673], ['ood', 35242]], 'labels': [-1, -1, 4, -1, -1], 'scores': [1.1562785232652781, 1.9452972239988742, 2.566506936778059, 2.9032967111466954, 3.0312282409105986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.4461934566497803})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.8575358390808105})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.0052502155303955})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.2386622428894043})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.539381504058838})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.884913682937622})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.5675647258758545})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.772219181060791})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.8455452919006348})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.6242117881774902})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6942, 'crossentropy': 2.5355447265625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0834628343582153})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0628060102462769})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.119718074798584})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0784423351287842})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.057174801826477})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.089677333831787})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.081714153289795})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1252777576446533})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1003910303115845})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 1383], ['ood', 512], ['ood', 8675], ['ood', 33030], ['id', 51101]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.2301636978222235, 2.1740348123020854, 2.7712415384041664, 3.095951709679345, 3.2254286507993264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.3702564239501953})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.706648588180542})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.9393452405929565})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.38800048828125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.436729669570923})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.2965893745422363})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6943, 'crossentropy': 2.047113671875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0672399997711182})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0292277336120605})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.042184829711914})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0157675743103027})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.065529227256775})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 48300], ['ood', 18767], ['ood', 47722], ['id', 30457], ['id', 40321]], 'labels': [-1, -1, -1, 3, 4], 'scores': [1.0048271690512727, 1.7821865397029981, 2.3772356361199956, 2.7780489387287854, 2.9765540970937945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.5142475366592407})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.627002239227295})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8975672721862793})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.0600547790527344})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.9518601894378662})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.41461443901062})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1066038608551025})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.6696367263793945})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7045, 'crossentropy': 1.968024609375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0722262859344482})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0640757083892822})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9795535802841187})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0534088611602783})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9764493703842163})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9940351843833923})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0172337293624878})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 41497], ['ood', 21197], ['ood', 31070], ['id', 13317], ['ood', 21304]], 'labels': [-1, -1, -1, 3, -1], 'scores': [1.0674543247281907, 1.9341991947435693, 2.5443955549133968, 2.8852307386751583, 3.0326877396001075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.429439902305603})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7533318996429443})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.126098871231079})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.370253562927246})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.407470941543579})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.70416259765625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 3.081997871398926})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.8890178203582764})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 3.051229476928711})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6979, 'crossentropy': 2.738157421875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1984916925430298})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1517404317855835})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1666300296783447})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1156079769134521})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2760488986968994})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2437777519226074})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1851952075958252})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 19501], ['ood', 48853], ['ood', 28579], ['id', 45156], ['id', 59846]], 'labels': [-1, -1, -1, 2, 0], 'scores': [1.1655943543034661, 2.0395790026051217, 2.6310491539473118, 2.934230615526781, 3.0694384282258422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4384608268737793})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.6209731101989746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9135050773620605})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.0744004249572754})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.2432079315185547})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.4334287643432617})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6989, 'crossentropy': 1.8635736328125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0600051879882812})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0133912563323975})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0285121202468872})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9884243011474609})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9501016139984131})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 8857], ['ood', 27459], ['ood', 58851], ['ood', 39301], ['id', 7125]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9890780965113652, 1.7833363860314728, 2.3306485214488806, 2.638319025079845, 2.8164345333064524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3078895807266235})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7491405010223389})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9610323905944824})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.035050868988037})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.467989683151245})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.508033275604248})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.807887554168701})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6939, 'crossentropy': 2.19298046875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1331467628479004})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0483900308609009})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0513732433319092})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.080847978591919})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0850920677185059})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1052651405334473})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 21151], ['ood', 8755], ['ood', 45245], ['ood', 17502], ['id', 35340]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0885318498655983, 1.978233272020577, 2.5878106549986324, 2.936890041440609, 3.059734307188326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4454197883605957})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.7864160537719727})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.048952102661133})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.370114326477051})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5396673679351807})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.7186479568481445})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.9741628170013428})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.9978528022766113})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.9360461235046387})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6942, 'crossentropy': 2.56618203125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.137476921081543})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1349248886108398})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1685585975646973})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1438963413238525})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1578104496002197})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.148850679397583})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2475796937942505})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1535804271697998})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 18417], ['ood', 36280], ['ood', 44436], ['id', 2518], ['id', 32302]], 'labels': [-1, -1, -1, 1, 6], 'scores': [1.073608213193662, 1.9451641112649747, 2.593716217950222, 2.937036534608623, 3.1048793089141586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2780102491378784})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7542023658752441})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8881360292434692})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.1972432136535645})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.429551124572754})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3918681144714355})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.769181251525879})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.537734031677246})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.89573073387146})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.618765354156494})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6889, 'crossentropy': 2.62168515625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.151883602142334})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1898490190505981})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1164720058441162})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2022773027420044})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1514310836791992})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1802380084991455})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1975858211517334})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 23631], ['ood', 45602], ['ood', 54507], ['ood', 1578], ['id', 49604]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.0919129752612626, 1.9685832502866671, 2.5906656746052947, 2.9652437279277484, 3.1096629871044508]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.384913682937622})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4745092391967773})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.8143088817596436})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.9785634279251099})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.2386531829833984})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.2046916484832764})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2458977699279785})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.4144558906555176})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.7279052734375})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.924692153930664})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7022, 'crossentropy': 2.3717748046875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1467232704162598})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.044249415397644})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.035602331161499})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.05097496509552})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0326156616210938})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.1168038845062256})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0677720308303833})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0712414979934692})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0717287063598633})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 37233], ['ood', 13719], ['ood', 27195], ['ood', 3692], ['id', 18684]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.2210612976027175, 2.211592054439736, 2.89359461195584, 3.1810294591249164, 3.2732458239267874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2102913856506348})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5941834449768066})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.918900489807129})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.114635467529297})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.203760862350464})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.638808488845825})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.3405003547668457})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.504861831665039})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.7032, 'crossentropy': 2.2043640625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1142349243164062})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1542730331420898})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.090228796005249})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.066442847251892})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1330840587615967})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.146645188331604})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1132588386535645})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 12069], ['ood', 56466], ['ood', 47572], ['ood', 34144], ['ood', 35970]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.152629484671674, 1.975937806698941, 2.5478790252665604, 2.835776812737971, 2.9595735300363266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2571765184402466})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.464379072189331})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7499802112579346})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.042166233062744})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.189724922180176})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6966, 'crossentropy': 1.51295791015625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0552257299423218})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9425452947616577})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9385097622871399})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 0.940388560295105})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 49485], ['ood', 39638], ['id', 8628], ['ood', 15328], ['ood', 49760]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.0592967750757454, 1.8114684752789771, 2.366427716371877, 2.71707870048499, 2.9098111471237953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2036128044128418})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.4116662740707397})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7838115692138672})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.8122279644012451})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.2222914695739746})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.0685477256774902})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.1106762886047363})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.4075520038604736})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.5905239582061768})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7081, 'crossentropy': 2.1484771484375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.112455129623413})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0456398725509644})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.071136713027954})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0705182552337646})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0335450172424316})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0970981121063232})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.077069640159607})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0737605094909668})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 43909], ['ood', 9346], ['ood', 24632], ['id', 40946], ['id', 22116]], 'labels': [-1, -1, -1, 2, 6], 'scores': [1.1789254743777167, 2.0844491862191625, 2.705505372459008, 3.0036737027568607, 3.150242578124751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.272151231765747})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.3994977474212646})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8607053756713867})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.8206548690795898})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.205815315246582})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6938, 'crossentropy': 1.3959814453125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0033999681472778})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9651150703430176})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9383406043052673})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.8932071328163147})
store['active_learning_steps'][40]['eval_training']['best_epoch']=4
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 18473], ['ood', 47747], ['ood', 35590], ['ood', 49896], ['id', 12009]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1053257595390136, 1.9544171743280474, 2.550933958681555, 2.8725359508464816, 2.978075319406843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2108497619628906})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5371346473693848})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7984678745269775})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8613970279693604})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.9988515377044678})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.2478833198547363})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4902658462524414})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7056, 'crossentropy': 1.857105078125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0761713981628418})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9645630121231079})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0019233226776123})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9971363544464111})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9449679255485535})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9668729305267334})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 22549], ['ood', 58], ['ood', 3158], ['id', 33716], ['ood', 29303]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.1133738451144082, 1.999695048260747, 2.585540274304485, 2.907697379379721, 3.0534906850165715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2670971155166626})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.439660906791687})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9778577089309692})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.149069309234619})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.346229076385498})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.364123821258545})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.4264869689941406})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.663893699645996})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.7018, 'crossentropy': 2.24368515625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1008222103118896})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.125774621963501})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1467297077178955})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1014844179153442})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1147069931030273})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1447808742523193})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0934666395187378})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 24731], ['ood', 54507], ['ood', 36597], ['ood', 51262], ['id', 57593]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1335602989544167, 1.932164461419652, 2.564149966408614, 2.912883641172737, 3.089998599474681]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3792603015899658})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.376279354095459})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8027968406677246})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.9883928298950195})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.053724765777588})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2932381629943848})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.1287403106689453})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7014, 'crossentropy': 2.0128166015625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.079694151878357})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9888594746589661})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.014670491218567})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0027616024017334})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9980290532112122})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0125446319580078})
store['active_learning_steps'][43]['eval_training']['best_epoch']=6
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 14400], ['ood', 19215], ['ood', 31091], ['ood', 39983], ['ood', 2891]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0776745199134004, 1.96523307121277, 2.5333047691876898, 2.821339345114742, 2.959456102829223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2946717739105225})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5618760585784912})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.9691743850708008})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.0445430278778076})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.150857925415039})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6882, 'crossentropy': 1.51171689453125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.0946319103240967})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0294885635375977})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0016374588012695})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0005074739456177})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 6254], ['ood', 41528], ['ood', 38376], ['ood', 10235], ['id', 41852]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.1234914818332435, 1.9262192654674042, 2.4681160497813828, 2.806365393025164, 2.9763627799471237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3734383583068848})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5794041156768799})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.839465618133545})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.014564037322998})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.08467960357666})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.093736410140991})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.554975986480713})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.381481647491455})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.282275915145874})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6933, 'crossentropy': 2.15998125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0932979583740234})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0651366710662842})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.045030117034912})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0489732027053833})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0619945526123047})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.042249321937561})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0390894412994385})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0344977378845215})
store['active_learning_steps'][45]['eval_training']['best_epoch']=8
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 54616], ['ood', 9422], ['ood', 18841], ['id', 20982], ['id', 58380]], 'labels': [-1, -1, -1, 5, 6], 'scores': [1.0714326185387226, 2.020007080569614, 2.6985565749790528, 2.9797211788495437, 3.1010440441148974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.279111623764038})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4918639659881592})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.7125144004821777})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.0436019897460938})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.258279800415039})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.3466835021972656})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.7115652561187744})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.523135185241699})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.5053651332855225})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.6022353172302246})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.570343017578125})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.7661924362182617})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6943, 'crossentropy': 2.4115095703125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0504016876220703})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.004719614982605})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0239927768707275})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9927601218223572})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.035294771194458})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0418665409088135})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0113261938095093})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.01377534866333})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0410425662994385})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0191397666931152})
store['active_learning_steps'][46]['eval_training']['best_epoch']=7
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 10771], ['ood', 21550], ['ood', 44644], ['ood', 3194], ['id', 59555]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.2474262236497793, 2.17734629551391, 2.805839665532041, 3.1295165290457874, 3.2579706759464715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2278003692626953})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4404301643371582})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.863777756690979})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0886218547821045})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.1610605716705322})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.3061232566833496})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.338129997253418})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.3869214057922363})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.4868431091308594})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.4405059814453125})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.591905117034912})
store['active_learning_steps'][47]['training']['best_epoch']=8
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6884, 'crossentropy': 2.4143669921875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0786840915679932})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0513081550598145})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.062149167060852})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0556073188781738})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0576376914978027})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1671521663665771})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0987600088119507})
store['active_learning_steps'][47]['eval_training']['best_epoch']=4
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 44640], ['ood', 4801], ['ood', 23799], ['id', 19037], ['id', 20284]], 'labels': [-1, -1, -1, 6, 2], 'scores': [1.128091558145993, 2.0788716843320416, 2.660572475643944, 2.9766088002085596, 3.0877653332544517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.212472677230835})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.5016207695007324})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.847496509552002})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.916163444519043})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.966888189315796})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.1511495113372803})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.3071818351745605})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.5653069019317627})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.7243573665618896})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.3952746391296387})
store['active_learning_steps'][48]['training']['best_epoch']=7
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.7014, 'crossentropy': 2.197730078125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0687756538391113})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0140327215194702})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.994361400604248})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9948787093162537})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9872963428497314})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9778923392295837})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9565190076828003})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0101351737976074})
store['active_learning_steps'][48]['eval_training']['best_epoch']=5
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 16224], ['ood', 17179], ['ood', 40859], ['ood', 35242], ['id', 16858]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1326205431951557, 2.0723565776818824, 2.715870432857596, 3.043839109213393, 3.160747895788342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.178658366203308})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.3335702419281006})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6210006475448608})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.0215911865234375})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.1771085262298584})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.3142356872558594})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6953, 'crossentropy': 1.65550859375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0786932706832886})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0428917407989502})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9890140295028687})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0096409320831299})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0272407531738281})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 45198], ['ood', 36900], ['ood', 19923], ['id', 51071], ['ood', 19032]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.1621558063000514, 2.115320166575044, 2.7171483511240577, 3.0719431640884016, 3.26749384585343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2933177947998047})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.53389573097229})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.8090832233428955})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.9535753726959229})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.0458760261535645})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.20086669921875})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.2642083168029785})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.4837281703948975})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.314201831817627})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.5412049293518066})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6945, 'crossentropy': 2.3729765625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0796785354614258})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0129209756851196})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9659889936447144})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0419821739196777})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0667839050292969})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0456352233886719})
store['active_learning_steps'][50]['eval_training']['best_epoch']=3
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 34646], ['ood', 43211], ['ood', 16925], ['id', 15243], ['id', 47085]], 'labels': [-1, -1, -1, 2, 4], 'scores': [1.1755370124950622, 2.0887365240979254, 2.6978935598309457, 2.975878185605378, 3.0954917414080603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2852613925933838})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5184528827667236})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.8292689323425293})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.234208106994629})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.1326522827148438})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.4571380615234375})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.313572883605957})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.5180678367614746})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.6085405349731445})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6239585876464844})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.577914237976074})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.5730104446411133})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.7525973320007324})
store['active_learning_steps'][51]['training']['best_epoch']=10
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6933, 'crossentropy': 2.498262890625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0865600109100342})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0363218784332275})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0194460153579712})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.087610125541687})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9969074130058289})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.081525206565857})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0018806457519531})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0368086099624634})
store['active_learning_steps'][51]['eval_training']['best_epoch']=5
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 41718], ['ood', 20572], ['ood', 22151], ['id', 24383], ['id', 20990]], 'labels': [-1, -1, -1, 6, 6], 'scores': [1.2501916869628837, 2.1716021866954045, 2.7836650365864646, 3.114396203738428, 3.2247884554479986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1856825351715088})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5873665809631348})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.683164358139038})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.0498762130737305})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.148575782775879})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.3412959575653076})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.4174890518188477})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.5435099601745605})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6919, 'crossentropy': 2.1203275390625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0792880058288574})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0539774894714355})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0807042121887207})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0253385305404663})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0176461935043335})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.045727252960205})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1028223037719727})
store['active_learning_steps'][52]['eval_training']['best_epoch']=6
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 21664], ['ood', 38710], ['id', 45824], ['id', 55037], ['id', 1254]], 'labels': [-1, -1, 0, 5, 0], 'scores': [1.1175113800012542, 2.0039555998224325, 2.5271781176081367, 2.796548474160712, 2.949499046926338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1924362182617188})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5209332704544067})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.831845760345459})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.9099855422973633})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0770819187164307})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.1900506019592285})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.267047882080078})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.4041507244110107})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.42441463470459})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.7031, 'crossentropy': 2.101752734375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0841302871704102})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9834864139556885})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9957018494606018})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0021780729293823})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0422320365905762})
store['active_learning_steps'][53]['eval_training']['best_epoch']=2
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 28924], ['ood', 12929], ['ood', 21859], ['ood', 34540], ['id', 9425]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.1842786395533222, 2.220305975471838, 2.8530864178209274, 3.1019140465548514, 3.1880939024254573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.221235990524292})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3704705238342285})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.711208701133728})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7358946800231934})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9464850425720215})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.1621100902557373})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.2395310401916504})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.7013, 'crossentropy': 1.7899876953125}
