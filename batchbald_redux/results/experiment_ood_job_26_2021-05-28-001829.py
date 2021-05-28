store = {}
store['timestamp']=1622157509
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=26']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=26
store['worker_id']=26
store['num_workers']=40
store['config']={'seed': 1263, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1439337730407715})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.5714516639709473})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.727630138397217})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.665046453475952})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.192782402038574})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.86637544631958})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.135683536529541})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6832, 'crossentropy': 2.4033880859375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1291041374206543})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1526284217834473})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1339421272277832})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1353135108947754})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 46036], ['id', 36792], ['id', 16624], ['id', 35464], ['ood', 44]], 'labels': [2, 6, 8, 9, -1], 'scores': [1.095605316542502, 1.8907007874638575, 2.4823203643022724, 2.848109570860646, 3.0684934786980245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.1792192459106445})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.1249563694000244})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.274313449859619})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.2791659832000732})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.684664249420166})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6606674194335938})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.714, 'crossentropy': 2.19805078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0175235271453857})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9770294427871704})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9893064498901367})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0186996459960938})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 47825], ['id', 3445], ['id', 6096], ['id', 47599], ['id', 5947]], 'labels': [5, 6, 5, 0, 5], 'scores': [1.012102824395348, 1.8552493060018418, 2.439116686606045, 2.7993958482594676, 2.987148202649217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.167080879211426})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.599090099334717})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.478062629699707})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.7958617210388184})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.8715248107910156})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.8295340538024902})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6872, 'crossentropy': 2.188474609375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0665433406829834})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0797557830810547})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0766758918762207})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.032672643661499})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 23347], ['id', 13190], ['id', 8339], ['id', 22429], ['id', 49257]], 'labels': [8, 3, 5, 0, 7], 'scores': [0.9007113870421166, 1.6815508845818687, 2.2625868989637485, 2.6409135324203517, 2.8786912103038125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4571079015731812})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.9180200099945068})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8482962846755981})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.0882747173309326})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.680318832397461})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.992967128753662})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.441293239593506})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.1912922859191895})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7711, 'crossentropy': 1.556069921875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8936432003974915})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.8432036638259888})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.8443118929862976})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.8610475063323975})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 42529], ['id', 35864], ['id', 53517], ['id', 2376], ['id', 48323]], 'labels': [9, 5, 8, 7, 2], 'scores': [0.9729442153125716, 1.7815382941729738, 2.3471676793307443, 2.6920554243801975, 2.8562885009297387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7015151977539062})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.6294095516204834})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.8906890153884888})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.7072157859802246})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.118013858795166})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7727, 'crossentropy': 1.47151865234375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.8668956160545349})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.8126422166824341})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.8312718272209167})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.8102936744689941})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 44149], ['id', 4066], ['id', 24408], ['id', 22677], ['id', 9098]], 'labels': [2, 1, 5, 4, 2], 'scores': [0.8918301330306899, 1.6493662869882604, 2.191081063174085, 2.5299673498263244, 2.7365699340279477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.345432996749878})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.565117359161377})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.9094083309173584})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.7936522960662842})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 2.0108253955841064})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7917, 'crossentropy': 1.4393544921875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8996840715408325})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8639843463897705})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.786422610282898})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8121391534805298})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 729], ['id', 53029], ['id', 40688], ['id', 57510], ['id', 32129]], 'labels': [4, 2, 5, 5, 1], 'scores': [1.0236942407145846, 1.8325880675100046, 2.492463118554358, 2.9405991420585167, 3.1774029474395693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1679847240447998})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.472198247909546})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5957098007202148})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.5388622283935547})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.6592812538146973})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5995328426361084})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.773102045059204})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8216, 'crossentropy': 1.3502470703125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8045339584350586})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7160727381706238})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.6936898231506348})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.6838245987892151})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.6801201105117798})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.6648434400558472})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 15066], ['id', 41286], ['id', 9081], ['id', 3367], ['ood', 51018]], 'labels': [5, 0, 9, 0, -1], 'scores': [1.004052897726819, 1.7944294874406141, 2.442386661624159, 2.8256338713334364, 3.061206691875846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1332597732543945})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3612912893295288})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.3864072561264038})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.6128790378570557})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6475226879119873})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.6570570468902588})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6958777904510498})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.1132593154907227})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.7729403972625732})
store['active_learning_steps'][7]['training']['best_epoch']=6
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8192, 'crossentropy': 1.4792943359375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8184841871261597})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.763264536857605})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.722191333770752})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.7271072864532471})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.6638150215148926})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.7273299694061279})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.6732687950134277})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.693064272403717})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 19276], ['id', 29791], ['id', 42585], ['id', 28371], ['id', 38382]], 'labels': [6, 3, 3, 3, 8], 'scores': [1.140632549857995, 2.026110690575975, 2.665939360570233, 3.0613475486545916, 3.244760782345776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1402093172073364})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0618956089019775})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.306188941001892})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.337803840637207})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3515071868896484})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.852, 'crossentropy': 0.9404474609375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.791235625743866})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6771979331970215})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6495492458343506})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6502386331558228})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 30487], ['id', 59101], ['id', 13161], ['id', 31576], ['ood', 10939]], 'labels': [2, 8, 3, 7, -1], 'scores': [0.8242878337291328, 1.5366690678688784, 2.1017083595164365, 2.4708511111778595, 2.7063538208805644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0845484733581543})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.006547212600708})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0284998416900635})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2142640352249146})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2018177509307861})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.228201150894165})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8717, 'crossentropy': 0.900744921875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7064498662948608})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.620956540107727})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.5802096128463745})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.5775047540664673})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.5657281875610352})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 41497], ['id', 17756], ['id', 40079], ['id', 33150], ['id', 13081]], 'labels': [9, 8, 3, 8, 0], 'scores': [0.8597279531704975, 1.629817046423995, 2.211406583281371, 2.600090107501855, 2.7980633645418935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0843251943588257})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0980148315429688})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.284988284111023})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3817803859710693})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2699527740478516})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.333472728729248})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3584619760513306})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.43236243724823})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.474910020828247})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.5277067422866821})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.5532783269882202})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8531, 'crossentropy': 1.2042974609375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7317087650299072})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.6726884841918945})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.6520841121673584})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.6450679302215576})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.5867321491241455})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.5922091007232666})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.5766283273696899})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.5809872150421143})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5440099239349365})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.5562626719474792})
store['active_learning_steps'][10]['eval_training']['best_epoch']=9
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 19549], ['id', 27044], ['id', 14830], ['id', 24329], ['id', 55970]], 'labels': [3, 4, 8, 1, 9], 'scores': [1.0308503228706871, 1.9275472457498317, 2.5850148738334457, 2.959128723120447, 3.1817301132645497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.93434077501297})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0261163711547852})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3284679651260376})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.377871036529541})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3034086227416992})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8501, 'crossentropy': 0.9536146484375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8018107414245605})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7009901404380798})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6589738726615906})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6279972791671753})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59390], ['id', 19344], ['id', 2803], ['id', 32173], ['id', 27429]], 'labels': [2, 7, 3, 7, 0], 'scores': [0.8493420103820428, 1.5560735749323418, 2.1335372367832415, 2.5065128986152345, 2.736240964015238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8801058530807495})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9706215858459473})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.019930362701416})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0413578748703003})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8589, 'crossentropy': 0.800688525390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8175251483917236})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7816140651702881})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7050507068634033})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 11208], ['id', 13030], ['id', 14367], ['id', 31926], ['id', 34481]], 'labels': [9, 0, 3, 5, 3], 'scores': [0.6450554823308359, 1.204930131700133, 1.6856118668503033, 2.066480336935662, 2.3477372610315257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.993585467338562})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9535658359527588})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1078492403030396})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1491036415100098})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1555544137954712})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3364057540893555})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.3078289031982422})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8626, 'crossentropy': 1.04981513671875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.822471559047699})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6963014602661133})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6194483041763306})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.6162952780723572})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6167846918106079})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6069637537002563})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37397], ['ood', 16162], ['id', 48055], ['id', 44480], ['ood', 43150]], 'labels': [3, -1, 8, 5, -1], 'scores': [0.9496929558197174, 1.7284286047031654, 2.36372463923165, 2.7546786642889156, 2.9563648063282564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9349330067634583})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1000092029571533})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1641650199890137})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1501579284667969})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2672452926635742})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.3774288892745972})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1012167930603027})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1492631435394287})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2787930965423584})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.495226263999939})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2387981414794922})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8751, 'crossentropy': 1.0060587890625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7779215574264526})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6146450042724609})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.5976517200469971})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.5664114952087402})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.5323309302330017})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.5524225234985352})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5316288471221924})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.5290000438690186})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5033041834831238})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.5207550525665283})
store['active_learning_steps'][14]['eval_training']['best_epoch']=9
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 38627], ['id', 59900], ['id', 26733], ['id', 39925], ['id', 15981]], 'labels': [3, 4, 2, 7, 4], 'scores': [1.0085308265588544, 1.9027926093036092, 2.5866165595052344, 2.9762516625296875, 3.1634899061057746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9009568095207214})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7871090173721313})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8448643684387207})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.820419430732727})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.983946681022644})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0228654146194458})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9967710971832275})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8926, 'crossentropy': 0.734648046875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.6752534508705139})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5478466749191284})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5149945616722107})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.48325034976005554})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.4988504648208618})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.48679882287979126})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 1535], ['id', 44973], ['id', 27241], ['id', 37161], ['id', 50695]], 'labels': [1, 9, 8, 3, 2], 'scores': [0.8684173733333604, 1.5881443230292391, 2.150479577090648, 2.551097921163982, 2.8110716839998435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9063647389411926})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7829811573028564})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7763304710388184})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8084822297096252})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.738035261631012})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8451117277145386})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.810222864151001})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.987744927406311})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8959336280822754})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8130192756652832})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.692529638671875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6476924419403076})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5110083222389221})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.47528791427612305})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4303898215293884})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4011177122592926})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4121847450733185})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4230691194534302})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4142506718635559})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 12493], ['id', 13986], ['id', 7768], ['id', 24630], ['ood', 43952]], 'labels': [8, 4, 8, 5, -1], 'scores': [1.0599172864004416, 1.8770981121711836, 2.483865413400605, 2.838321333489712, 3.0263051080131085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8593317270278931})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7436336278915405})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.727548360824585})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6962889432907104})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8084326386451721})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7981860637664795})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7644152641296387})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.848279595375061})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8073921203613281})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.951919436454773})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8401303291320801})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0389821529388428})
store['active_learning_steps'][17]['training']['best_epoch']=9
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.752479345703125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7168378829956055})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5213434100151062})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.47520825266838074})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4391266107559204})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4479702115058899})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4267916679382324})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 28194], ['id', 38609], ['id', 49895], ['ood', 54376], ['ood', 43952]], 'labels': [9, 2, 5, -1, -1], 'scores': [0.9412213582079167, 1.7525957783014054, 2.40515973225353, 2.7944415458808685, 2.99713755911192]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0275743007659912})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6811169385910034})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.671269953250885})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6550493240356445})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.767417311668396})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9367791414260864})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.742276668548584})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.570420654296875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6231308579444885})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.49622607231140137})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.46783411502838135})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.44497108459472656})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.45835167169570923})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.42861583828926086})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 38391], ['id', 134], ['id', 9472], ['ood', 18584], ['ood', 26288]], 'labels': [8, 1, 2, -1, -1], 'scores': [0.7690899642985773, 1.4470434262802057, 1.982486334834447, 2.3715755041253903, 2.62202902418964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9200743436813354})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6484795808792114})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6385850310325623})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7104978561401367})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7171425819396973})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.826641321182251})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.58875615234375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6866788268089294})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5003109574317932})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4697117805480957})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4775664210319519})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43967825174331665})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 27131], ['id', 21335], ['id', 12655], ['ood', 38890], ['id', 48360]], 'labels': [2, 7, 9, -1, 3], 'scores': [0.7636841738287877, 1.481581029391294, 2.03924227782141, 2.4710336411535927, 2.765835752172878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7850362062454224})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5949037671089172})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5545564889907837})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5826950073242188})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.617047131061554})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.587647557258606})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.645717978477478})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6732755899429321})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7425206899642944})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6951526403427124})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6887428760528564})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.61860810546875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.63431715965271})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4836912155151367})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42897504568099976})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4127741754055023})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.38441383838653564})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3717048764228821})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3755287230014801})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3554205298423767})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3580318093299866})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 50343], ['id', 5062], ['id', 58249], ['ood', 55394], ['ood', 10281]], 'labels': [6, 9, 3, -1, -1], 'scores': [0.89220251844741, 1.6806503550746084, 2.282919897179374, 2.672450395953345, 2.905425818500591]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9184567332267761})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5883692502975464})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5845333337783813})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6636688709259033})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6427066326141357})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6163845062255859})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9142, 'crossentropy': 0.5864283203125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6352282762527466})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49271413683891296})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4632783532142639})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4478709101676941})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.42703378200531006})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 49064], ['id', 5600], ['id', 24145], ['id', 14337], ['id', 26756]], 'labels': [8, 6, 3, 7, 7], 'scores': [0.8424262674450747, 1.562516095540253, 2.1337544348339392, 2.526145978405191, 2.7835629286792436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8348116874694824})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5951189994812012})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.520671010017395})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.547324538230896})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5561810731887817})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5304142236709595})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5696803331375122})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6738376617431641})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6917694807052612})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.52136357421875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6581826210021973})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4664286971092224})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39233702421188354})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3756135106086731})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3717273473739624})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3204136788845062})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3535224199295044})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 33596], ['ood', 7847], ['id', 18130], ['ood', 25688], ['ood', 47364]], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.9436870535912174, 1.7794305425130306, 2.4094794168596705, 2.8547521803621656, 3.1158179641965837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9949538707733154})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6985812187194824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.659733235836029})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.661666989326477})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6618695855140686})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.650124192237854})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7466713190078735})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6599403619766235})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7505438327789307})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.69130539894104})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6112281680107117})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6980052590370178})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8163812756538391})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6771798133850098})
store['active_learning_steps'][23]['training']['best_epoch']=11
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.620168359375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6574647426605225})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4809255003929138})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4097842574119568})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.3971867263317108})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.3870760202407837})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.37648022174835205})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.38056766986846924})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3740984797477722})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.37010979652404785})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.33592498302459717})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.35029685497283936})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.36444443464279175})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3398021459579468})
store['active_learning_steps'][23]['eval_training']['best_epoch']=10
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 51710], ['ood', 13195], ['ood', 56414], ['id', 50889], ['ood', 43952]], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.8816000399859654, 1.6764728085464586, 2.31168421166302, 2.7698264512055264, 3.034119733234715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9133473038673401})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5747290849685669})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6588495969772339})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5748461484909058})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6031203269958496})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.617123007774353})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5903974771499634})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6382403373718262})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6645906567573547})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.567537248134613})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6016316413879395})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5673278570175171})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6452029347419739})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6139512062072754})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6977821588516235})
store['active_learning_steps'][24]['training']['best_epoch']=12
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9353, 'crossentropy': 0.56412080078125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.643858790397644})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4631856083869934})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3960391879081726})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3770831227302551})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3512740135192871})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3418081998825073})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.33787697553634644})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3257080316543579})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.31175512075424194})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3162938356399536})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3130871057510376})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3409388065338135})
store['active_learning_steps'][24]['eval_training']['best_epoch']=9
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 42632], ['ood', 30306], ['id', 43745], ['id', 35112], ['id', 9558]], 'labels': [0, -1, 8, 2, 4], 'scores': [0.8842436384203793, 1.6504412909317399, 2.275714675188601, 2.7220428347628705, 2.987436022574376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8975334167480469})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6391879320144653})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5774049758911133})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6298879981040955})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5825362205505371})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.585294246673584})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5789593458175659})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6196972131729126})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6595476865768433})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6243711709976196})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.50752080078125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6244763731956482})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4857255220413208})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.41627323627471924})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3845677673816681})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3799465298652649})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3622930645942688})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.37134307622909546})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3710380792617798})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3322467803955078})
store['active_learning_steps'][25]['eval_training']['best_epoch']=9
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 59674], ['id', 42317], ['id', 41107], ['id', 24990], ['ood', 36581]], 'labels': [4, 5, 3, 7, -1], 'scores': [0.8645873904082708, 1.594357133886053, 2.20196268240507, 2.6339935921267887, 2.8968863761190207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0688068866729736})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6829627752304077})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6855558156967163})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6666401624679565})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6463379263877869})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7167415618896484})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8279386758804321})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7925088405609131})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7827584743499756})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.6425615234375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6396932601928711})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.47412705421447754})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4181830883026123})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.39197635650634766})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4125591218471527})
store['active_learning_steps'][26]['eval_training']['best_epoch']=2
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 13928], ['id', 47260], ['id', 51004], ['ood', 38613], ['ood', 14060]], 'labels': [2, 6, 7, -1, -1], 'scores': [0.9011664875746312, 1.672643358202483, 2.2806735144595507, 2.655668398986573, 2.869442112215964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0128772258758545})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6657126545906067})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6256288886070251})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7179599404335022})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7163712978363037})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7193311452865601})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.715989351272583})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9142, 'crossentropy': 0.5913169921875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6767446994781494})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.48623019456863403})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4714331030845642})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4320846199989319})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43449094891548157})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.41603633761405945})
store['active_learning_steps'][27]['eval_training']['best_epoch']=3
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 43906], ['id', 18398], ['id', 54994], ['id', 1740], ['id', 39373]], 'labels': [4, 4, 6, 9, 8], 'scores': [0.7861916244497384, 1.4886381040536678, 2.109339160326474, 2.4907510735252867, 2.723216763404384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8858285546302795})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5722454190254211})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.566832959651947})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5884546041488647})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5484398603439331})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6765100359916687})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6463515758514404})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.642958402633667})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.457522607421875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6226811408996582})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4817374348640442})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4051380455493927})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3788940906524658})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38993334770202637})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.36019280552864075})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.34455162286758423})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 55496], ['id', 8116], ['id', 59701], ['id', 1281], ['ood', 43952]], 'labels': [9, 0, 5, 7, -1], 'scores': [0.8993992802498518, 1.6314987926922195, 2.1705189880395377, 2.5322610370045284, 2.7618755571461273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8944224715232849})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5855498909950256})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5853546857833862})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7099197506904602})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.610758364200592})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5914499759674072})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6904211044311523})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6142735481262207})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.497765087890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6638526916503906})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.49552953243255615})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4411592185497284})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4087750315666199})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38904035091400146})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.40418440103530884})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3799619674682617})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 1674], ['id', 51508], ['id', 13538], ['id', 18501], ['ood', 43952]], 'labels': [9, 6, 5, 4, -1], 'scores': [0.8097161701697619, 1.520695987388755, 2.1049537716904965, 2.4874141879850695, 2.7147226313095185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9968702793121338})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5999017953872681})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5381258726119995})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.573788046836853})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5531164407730103})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6031243801116943})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6249924898147583})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6326247453689575})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.49411259765625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6328076124191284})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.49331796169281006})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4088551998138428})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39001208543777466})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40966543555259705})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3650397062301636})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3647559881210327})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 27026], ['id', 53266], ['id', 53873], ['ood', 43952], ['id', 10690]], 'labels': [2, 2, 4, -1, 4], 'scores': [0.8840687182894935, 1.6607160395377676, 2.2410865466295533, 2.642038467563978, 2.8821489927677337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9249517321586609})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5788373947143555})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5683525204658508})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6027452945709229})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5830052495002747})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.614580512046814})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.49260986328125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6952925324440002})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4921695590019226})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4666896462440491})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.42289745807647705})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.41957128047943115})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 24172], ['id', 52358], ['id', 47409], ['id', 25823], ['ood', 11446]], 'labels': [-1, 2, 2, 0, -1], 'scores': [0.7978012600349276, 1.4556582100284183, 2.002169206626962, 2.4106677165016324, 2.6741937821055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9703245162963867})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5886316299438477})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5124193429946899})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5493170022964478})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5397921204566956})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6029025316238403})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5971304178237915})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.50256806640625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6405405402183533})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.46395429968833923})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43038877844810486})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.38715144991874695})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3788960874080658})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3603414297103882})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 2406], ['id', 59339], ['id', 40224], ['id', 622], ['id', 17019]], 'labels': [4, 1, 4, 5, 9], 'scores': [0.7760125382814422, 1.4524073230116414, 2.000664240803241, 2.4083112193411527, 2.6549013694437145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0451327562332153})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5712157487869263})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5655280947685242})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5929580926895142})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5642262697219849})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5845246315002441})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.541744589805603})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5553971529006958})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.608648419380188})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6313869953155518})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6958534121513367})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.941, 'crossentropy': 0.50211572265625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6275920867919922})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46211862564086914})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41474512219429016})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36615854501724243})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36091721057891846})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3617691397666931})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3317602276802063})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3537635803222656})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33453354239463806})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3509095013141632})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 9601], ['id', 5370], ['id', 42384], ['id', 4243], ['ood', 33298]], 'labels': [8, 3, 8, 6, -1], 'scores': [0.8460290347679786, 1.6271906596100854, 2.226830981179445, 2.6019770127002184, 2.810452941391878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1066559553146362})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6158016324043274})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5347028970718384})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5614443421363831})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.566195011138916})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5306001305580139})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5453910827636719})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.604896605014801})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6013151407241821})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5842862129211426})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5358465313911438})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5956200361251831})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5744768977165222})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5850688219070435})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6085476875305176})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.625740647315979})
store['active_learning_steps'][34]['training']['best_epoch']=13
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.50438515625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5814625024795532})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4578495919704437})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3814328908920288})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.35641714930534363})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3409974277019501})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.31673485040664673})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3306981921195984})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31479597091674805})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3075364828109741})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3071020245552063})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.30862367153167725})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 52086], ['ood', 18584], ['id', 27653], ['ood', 8877], ['ood', 38941]], 'labels': [5, -1, 6, -1, -1], 'scores': [0.8712396191304046, 1.6437708170722702, 2.299387481338284, 2.7100037699889983, 2.9365396810921016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9731028079986572})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5728520750999451})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5269870758056641})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5550059080123901})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5596139430999756})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5553945302963257})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5803225040435791})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9392, 'crossentropy': 0.44916953125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6316542029380798})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.49171769618988037})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4049836993217468})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4490956664085388})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3786115348339081})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3804216980934143})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 28362], ['id', 27406], ['id', 5743], ['id', 370], ['ood', 30893]], 'labels': [7, 7, 8, 7, -1], 'scores': [0.7517514718234064, 1.4276929982097646, 1.9389983021594812, 2.302104583611704, 2.5476590389486278]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0501668453216553})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5424246191978455})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5134708881378174})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4890899658203125})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49538618326187134})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5542410612106323})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5428167581558228})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.570940375328064})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6121186017990112})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5659181475639343})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.431238134765625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6260392665863037})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.46567922830581665})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4225936532020569})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39442113041877747})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36857888102531433})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34433093667030334})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33092713356018066})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32770952582359314})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3454785943031311})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 1518], ['ood', 29018], ['id', 39516], ['id', 49573], ['id', 16488]], 'labels': [9, -1, 5, 2, 9], 'scores': [0.8564833836222274, 1.5921262363095243, 2.181980730426866, 2.5692084901108903, 2.8073757344791375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9639842510223389})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5550516247749329})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46079739928245544})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46818703413009644})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44116708636283875})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46285638213157654})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4754164218902588})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5233083963394165})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5430324077606201})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5216611623764038})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.422234130859375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6484416127204895})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4708995223045349})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4131031930446625})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37570124864578247})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3783925771713257})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.33648616075515747})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34443581104278564})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35548973083496094})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32268235087394714})
store['active_learning_steps'][37]['eval_training']['best_epoch']=9
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 49149], ['id', 59314], ['id', 32335], ['id', 26300], ['ood', 9582]], 'labels': [3, 9, 1, 0, -1], 'scores': [0.9847944273046001, 1.7017306884267787, 2.262815772189729, 2.6323706052315554, 2.859242366245109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0345196723937988})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6429188847541809})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.534288763999939})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49422937631607056})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5219547748565674})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4942788779735565})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.509234607219696})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5602865219116211})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5476454496383667})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5520487427711487})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.425192138671875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5426613092422485})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.41091763973236084})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4124164879322052})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34199434518814087})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3548508584499359})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32233670353889465})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28587982058525085})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2947719693183899})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30162352323532104})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 42703], ['id', 13831], ['id', 19942], ['id', 4976], ['id', 51200]], 'labels': [-1, 3, 5, 1, 9], 'scores': [0.8310362212639681, 1.5677919942347964, 2.178342617963385, 2.5548860553382964, 2.779166540210972]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.101880431175232})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5116487741470337})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4601410925388336})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4666503667831421})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43826496601104736})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44890713691711426})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5060169100761414})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4999445676803589})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9529, 'crossentropy': 0.392567626953125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5820248126983643})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47408074140548706})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.37781059741973877})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3486780524253845})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3498287796974182})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3366546034812927})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30612295866012573})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 48102], ['id', 14062], ['ood', 57069], ['id', 2542], ['id', 16376]], 'labels': [7, 8, -1, 4, 1], 'scores': [0.9318784334194423, 1.71880163296174, 2.2681921580365145, 2.648723116391139, 2.843129086828892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0451722145080566})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.493192195892334})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4743744134902954})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4755573570728302})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.538652241230011})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.536038875579834})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9461, 'crossentropy': 0.432833740234375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6410488486289978})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5150282382965088})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4619295597076416})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44399866461753845})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39609837532043457})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 36818], ['id', 54950], ['id', 48681], ['id', 38920], ['id', 57718]], 'labels': [7, 8, 2, 7, 7], 'scores': [0.7041578080636008, 1.3172482266322785, 1.8158936248988233, 2.2143671295860443, 2.4901375293282637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9529701471328735})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5169634819030762})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4546620845794678})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5017451047897339})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4886047840118408})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5222141742706299})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5032856464385986})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.49460214376449585})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5590798258781433})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5249906182289124})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.582298994064331})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9544, 'crossentropy': 0.4091429931640625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5853430032730103})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4135268032550812})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36886996030807495})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33577871322631836})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3499996066093445})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3182920813560486})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30505579710006714})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3083919882774353})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.28993135690689087})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2916014790534973})
store['active_learning_steps'][41]['eval_training']['best_epoch']=10
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 46289], ['id', 23642], ['ood', 3916], ['id', 56292], ['id', 11616]], 'labels': [0, 2, -1, 9, 7], 'scores': [0.8225003848838108, 1.5559957158090154, 2.1312909597657184, 2.541673371958753, 2.8047999716103105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0648157596588135})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5974507331848145})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46435821056365967})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4254983067512512})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5055267810821533})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.516735851764679})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5063823461532593})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5504897236824036})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5499478578567505})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6408578753471375})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9501, 'crossentropy': 0.41014638671875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6088682413101196})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.45479780435562134})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38942983746528625})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3540240526199341})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30857163667678833})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3512423038482666})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.325626015663147})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.303189218044281})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2880617380142212})
store['active_learning_steps'][42]['eval_training']['best_epoch']=9
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 5035], ['id', 24887], ['ood', 46795], ['id', 16025], ['ood', 14146]], 'labels': [7, 5, -1, 2, -1], 'scores': [0.9061384312802394, 1.6615401723660659, 2.2472681292833157, 2.6611081335814006, 2.8937768216783937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1785006523132324})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5949612855911255})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4872593283653259})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.48202288150787354})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4712715446949005})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4712836444377899})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4750797152519226})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4859551787376404})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.47929298877716064})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44868987798690796})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49055588245391846})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5135729312896729})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.3988295654296875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5966804027557373})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47935643792152405})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.38393956422805786})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34308671951293945})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34486615657806396})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3277287185192108})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31510767340660095})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3133591413497925})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34571415185928345})
store['active_learning_steps'][43]['eval_training']['best_epoch']=6
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 42703], ['id', 14655], ['id', 42711], ['id', 15699], ['id', 56286]], 'labels': [0, 3, 4, 2, 8], 'scores': [0.9528509944767225, 1.7526271821873394, 2.331269581296948, 2.700807749627021, 2.897153876155346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9610269069671631})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5228875875473022})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4449671506881714})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4211527705192566})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4120142161846161})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4446624517440796})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5300136208534241})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.46285414695739746})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9571, 'crossentropy': 0.3598087158203125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6419030427932739})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4862730801105499})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40937966108322144})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3811998963356018})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.365047812461853})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35919028520584106})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.322751522064209})
store['active_learning_steps'][44]['eval_training']['best_epoch']=7
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 7726], ['id', 36234], ['ood', 6846], ['id', 4729], ['ood', 43603]], 'labels': [4, 7, -1, 0, -1], 'scores': [0.7320931984544696, 1.4077983496408026, 1.9755621037520585, 2.384790161803651, 2.6657586879625725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1462860107421875})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.540148138999939})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5102834105491638})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4571104645729065})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5232012271881104})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4218578636646271})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4779333174228668})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5179433822631836})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.499600887298584})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.375150634765625}
