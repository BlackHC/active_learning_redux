store = {}
store['timestamp']=1622148061
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=8']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=40
store['config']={'seed': 1243, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.247647285461426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.76430344581604})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5868282318115234})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.9454288482666016})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.716850757598877})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.7222719192504883})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.836822986602783})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6859, 'crossentropy': 2.5146662109375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1946697235107422})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1384592056274414})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.128141164779663})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.152341365814209})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.157041072845459})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 29361], ['id', 7979], ['id', 29273], ['id', 36475], ['ood', 33397]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.163661749422356, 1.9726869030260419, 2.557315353254385, 2.9552183841552413, 3.189659486388881]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6892011165618896})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.123745918273926})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4569344520568848})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4709043502807617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7307047843933105})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9938387870788574})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.953853130340576})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6885, 'crossentropy': 2.1683333984375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1639354228973389})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1071455478668213})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1892800331115723})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.140323281288147})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2302813529968262})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 30692], ['id', 37052], ['id', 13016], ['id', 31011], ['id', 10371]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9850815129550301, 1.7626220010516374, 2.327191015527342, 2.654369555955534, 2.8547871131169273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.9468015432357788})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.396056890487671})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8230831623077393})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.899785041809082})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.056692123413086})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0133559703826904})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6902, 'crossentropy': 2.3874591796875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2542717456817627})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2530878782272339})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.26556396484375})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2985025644302368})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12928], ['id', 26034], ['id', 23193], ['id', 10633], ['id', 8535]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8518269690872591, 1.6291514179610216, 2.252790472304169, 2.6011641963817667, 2.7919113734167045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.7541227340698242})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.9759266376495361})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.4685614109039307})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.502749443054199})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.4635438919067383})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7153, 'crossentropy': 1.741201171875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1167348623275757})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1022512912750244})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0615870952606201})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0463829040527344})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 51761], ['id', 53170], ['id', 48030], ['id', 37637], ['id', 52800]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9605197419642497, 1.680445421858666, 2.279576083217794, 2.689727232086822, 2.9314820432217648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.6688323020935059})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7768906354904175})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.13749361038208})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6358532905578613})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.5550403594970703})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7378, 'crossentropy': 1.5902837890625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1773266792297363})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1340327262878418})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1155779361724854})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.130717158317566})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 49202], ['id', 42504], ['id', 55834], ['id', 13760], ['id', 31667]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8346957287812422, 1.4805408806738787, 2.0129175903082377, 2.3816730505255252, 2.6281975150509673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5184284448623657})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.7807929515838623})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.9331483840942383})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.174785614013672})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.39312744140625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.53580904006958})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7622, 'crossentropy': 1.584441015625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.073165774345398})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9818602800369263})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9673407077789307})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9330266118049622})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9734314680099487})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 12514], ['id', 28422], ['id', 34708], ['id', 4851], ['id', 7207]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8065568969201391, 1.5195276731326692, 2.081100660738077, 2.496641750265092, 2.746832923688981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.7607300281524658})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2494208812713623})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.414548873901367})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.4432373046875})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.8055434226989746})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.5929813385009766})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.7470991611480713})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.907001495361328})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.839702844619751})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.546586513519287})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.914179563522339})
store['active_learning_steps'][6]['training']['best_epoch']=8
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7446, 'crossentropy': 2.2482078125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0750619173049927})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1094715595245361})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1480402946472168})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1791040897369385})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 18271], ['id', 29156], ['id', 30], ['id', 23588], ['id', 17309]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.892448943360026, 1.72064203276634, 2.321615368916971, 2.679160080032914, 2.8432607528114415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.435678482055664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.820797085762024})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.1508400440216064})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.998221516609192})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.1725993156433105})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.0983493328094482})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.434983491897583})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.346835136413574})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.513671875})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.409292221069336})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.193946361541748})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.648448944091797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.6504950523376465})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.7051305770874023})
store['active_learning_steps'][7]['training']['best_epoch']=11
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7817, 'crossentropy': 1.943797265625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.0486788749694824})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.8940331935882568})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9551520347595215})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9244505763053894})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.899837851524353})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 13448], ['id', 32878], ['id', 13515], ['id', 47057], ['ood', 1707]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0903248616252033, 1.8490631520546894, 2.4765157809142835, 2.8383296808351774, 3.0256744374276234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3270089626312256})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.5241775512695312})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.670262336730957})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.9064346551895142})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.8965120315551758})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.1637110710144043})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.1416704654693604})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.32735538482666})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7944, 'crossentropy': 1.5560392578125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.0094249248504639})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9012259244918823})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8753354549407959})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.8481907844543457})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.8626230955123901})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8262943029403687})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.8172284960746765})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 10925], ['id', 28189], ['id', 42338], ['id', 11054], ['id', 30996]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9622561729109078, 1.7512957751429195, 2.3349496186516845, 2.731035401585025, 2.963154697320231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9939261078834534})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1445932388305664})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3421051502227783})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3277029991149902})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4254639148712158})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4552788734436035})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.5068202018737793})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.501000165939331})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.620159387588501})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.790889859199524})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5224517583847046})
store['active_learning_steps'][9]['training']['best_epoch']=8
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.845, 'crossentropy': 1.164288671875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8061313033103943})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.6932167410850525})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7090250253677368})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.688709020614624})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.6676075458526611})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 19466], ['id', 53873], ['id', 52753], ['id', 2488], ['id', 57026]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8981672369802698, 1.6194547921856417, 2.1865195668225414, 2.563797189758498, 2.7586012841372654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9216582775115967})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.954990029335022})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.099294900894165})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.29804265499115})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1803838014602661})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8575, 'crossentropy': 0.7751421875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7668660879135132})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.6851215362548828})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7052162885665894})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.6825920939445496})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 38080], ['id', 23863], ['id', 23053], ['id', 49893], ['id', 43364]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6802688653751374, 1.2906369336249184, 1.8135772696713994, 2.2167057024150756, 2.489238672311579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9698265790939331})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9664599299430847})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0517175197601318})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0998458862304688})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3269155025482178})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.866, 'crossentropy': 0.799707373046875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7828506231307983})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6633802056312561})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6930338144302368})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6987332105636597})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 2765], ['id', 59314], ['id', 46250], ['id', 16997], ['id', 49647]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.624333964934646, 1.192580983288043, 1.6691633919758573, 2.0250799798544437, 2.2784727386565926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9214094877243042})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0176801681518555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9830523729324341})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.062833309173584})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1805212497711182})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1485066413879395})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1893320083618164})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2626986503601074})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.4111506938934326})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8746, 'crossentropy': 0.91699296875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7262084484100342})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6625146269798279})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6003557443618774})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6367748975753784})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.5946375131607056})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.5612925291061401})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.5822680592536926})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.5801782608032227})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 28182], ['id', 25910], ['id', 51614], ['id', 25782], ['ood', 14226]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9361004921816465, 1.7566701568093879, 2.373844779396771, 2.7793504898287393, 2.99276836815881]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0238471031188965})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9094070792198181})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9014334678649902})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0703232288360596})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0519006252288818})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.044698715209961})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8669, 'crossentropy': 0.801040087890625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7356311082839966})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.656670093536377})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6471290588378906})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6192549467086792})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6267573833465576})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 54106], ['id', 59447], ['id', 28944], ['id', 5773], ['id', 23486]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7238790719858605, 1.385737687435447, 1.9178727648605634, 2.3332229728460323, 2.61260363745801]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0102908611297607})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8879460096359253})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9168473482131958})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9867855310440063})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1056158542633057})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1156749725341797})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8739, 'crossentropy': 0.77429287109375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7468470335006714})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6295239925384521})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6023868322372437})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.587273359298706})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5468407869338989})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 52392], ['id', 44082], ['id', 7438], ['id', 48492], ['id', 51644]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7659724970411248, 1.4179065257622887, 1.977931016282131, 2.392191894532816, 2.682783584235125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8446884155273438})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.821475088596344})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8368955254554749})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9208188056945801})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9166910648345947})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0233495235443115})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1219000816345215})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0371050834655762})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0706062316894531})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.123866081237793})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.216341495513916})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2455945014953613})
store['active_learning_steps'][15]['training']['best_epoch']=9
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8854, 'crossentropy': 0.86428408203125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6803348064422607})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5736087560653687})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5572988986968994})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5382845401763916})
store['active_learning_steps'][15]['eval_training']['best_epoch']=1
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 59726], ['id', 36884], ['id', 19344], ['id', 10846], ['id', 12645]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.98091171828173, 1.8328039934792608, 2.472888857405972, 2.8339372795251734, 2.998935999422547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9054237604141235})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7487379312515259})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9392766952514648})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8734069466590881})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.903862714767456})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8837, 'crossentropy': 0.6578060546875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7711800336837769})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6645032167434692})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6372251510620117})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6386167407035828})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 55259], ['id', 57728], ['id', 49616], ['id', 42221], ['id', 7281]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6964760181157268, 1.2572095071895482, 1.715324035741503, 2.080792969439181, 2.3406868065965565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8590367436408997})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7578527331352234})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7174403667449951})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7390937805175781})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8179290294647217})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.872367262840271})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.87095046043396})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0506116151809692})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.972719669342041})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.755886669921875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6783721446990967})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.557976484298706})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.49840208888053894})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.4696478843688965})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.49058473110198975})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4515739977359772})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.44003668427467346})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.45073211193084717})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 38920], ['id', 26444], ['id', 3510], ['id', 52695], ['id', 4292]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8622035207735663, 1.5763876214888195, 2.1552900535959436, 2.5394432531606235, 2.8024279901935234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9389408826828003})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7304356098175049})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6903129816055298})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7844696640968323})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7985539436340332})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8771735429763794})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.608492724609375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6746305227279663})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5699195861816406})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5561286211013794})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.504321277141571})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5137312412261963})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 22272], ['id', 45048], ['id', 3056], ['id', 17879], ['id', 35956]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7296614843044056, 1.3422012128949978, 1.8754308652067513, 2.235809975889876, 2.4647793305722807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9527156352996826})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.743301510810852})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7914251089096069})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7665697336196899})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8005510568618774})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9746330976486206})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8298500776290894})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9071, 'crossentropy': 0.6462583984375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6991904973983765})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5671787858009338})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5185599327087402})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.49668562412261963})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4846729636192322})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4671702980995178})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 57276], ['id', 13729], ['id', 15024], ['id', 53864], ['id', 18302]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9289560600507119, 1.7345498470215812, 2.2619614493860807, 2.6166406692979614, 2.8244184735750544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9052779078483582})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6795413494110107})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.679084300994873})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7333180904388428})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7408733367919922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7846672534942627})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.822948694229126})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8251519799232483})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8495908379554749})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.688889404296875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6787973642349243})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.49493497610092163})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.48510199785232544})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4753299355506897})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4646793603897095})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4577358365058899})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.43675321340560913})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 14878], ['id', 4193], ['id', 57195], ['id', 12363], ['id', 23024]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.751067240129534, 1.457191857443739, 2.0496792705689035, 2.4638830421229434, 2.698910511241242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9870936870574951})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6037238240242004})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5535902976989746})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6205887794494629})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5913086533546448})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6248363256454468})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6940939426422119})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.673019289970398})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7582403421401978})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7458875775337219})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7740298509597778})
store['active_learning_steps'][21]['training']['best_epoch']=8
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.62330322265625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.621271014213562})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5072029232978821})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4394749402999878})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4621487259864807})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4195522367954254})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4039691686630249})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4029318690299988})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4224991202354431})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3800088167190552})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4051092267036438})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 49525], ['id', 35903], ['id', 43234], ['id', 40704], ['id', 13040]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8518299401846641, 1.5735320434795246, 2.1620700050080117, 2.5331975512263947, 2.742416701643352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9260164499282837})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6661537885665894})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6021708250045776})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6487280130386353})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7123340964317322})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6581259369850159})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6823018789291382})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7300183773040771})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.835771381855011})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8128182291984558})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7113714814186096})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7872371673583984})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8490168452262878})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7975713014602661})
store['active_learning_steps'][22]['training']['best_epoch']=11
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.612462744140625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6602505445480347})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5100775361061096})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4442943334579468})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4293646812438965})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4011417627334595})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.398682177066803})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3978448510169983})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3693803548812866})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3710240125656128})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.35304826498031616})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3552311956882477})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 16290], ['id', 19423], ['id', 26998], ['id', 27964], ['id', 27128]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9140455910060217, 1.7252119549738971, 2.363143440416655, 2.7673988254334265, 2.969236029786673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.788432240486145})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5894640684127808})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.550819993019104})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5582605004310608})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6098535656929016})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5913839340209961})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6679956912994385})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.51459716796875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6787301301956177})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4977731704711914})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4680810570716858})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.42111751437187195})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.414298951625824})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43533819913864136})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 10210], ['id', 41218], ['id', 21287], ['id', 35482], ['id', 45143]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.728416315745527, 1.333676316901807, 1.8281199528160377, 2.195961875674458, 2.4377633602408713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9208872318267822})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6436492204666138})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6499931812286377})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.666259765625})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6210280656814575})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6817046403884888})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6399326324462891})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7354656457901001})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.52877734375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6692485809326172})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.47628477215766907})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43288832902908325})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43000781536102295})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4211496114730835})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.3948087692260742})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 23086], ['id', 2250], ['id', 4068], ['id', 14501], ['id', 52086]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7542399545703806, 1.4161163304230127, 1.9679533736289683, 2.3931784282692785, 2.6641618158198987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9134960174560547})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6412107348442078})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5635534524917603})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5868615508079529})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.652786135673523})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6819872260093689})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6912186145782471})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6480832099914551})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.523379345703125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7088174819946289})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5096307396888733})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.45249050855636597})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4408917725086212})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3890122175216675})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4198334813117981})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.37973177433013916})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 20150], ['id', 3765], ['id', 56914], ['id', 19190], ['id', 16822]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8101556876521834, 1.527459999371371, 2.038722387910693, 2.405052793333863, 2.641691001243556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9315447807312012})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6797237396240234})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5730581879615784})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.581099808216095})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.684435248374939})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.603546142578125})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5989127159118652})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6445733308792114})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6497358083724976})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6353886723518372})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.653168797492981})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6411998271942139})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8530371189117432})
store['active_learning_steps'][26]['training']['best_epoch']=10
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.582416259765625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.624313473701477})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4634326994419098})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4376075565814972})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4226945638656616})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38959503173828125})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.38130468130111694})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4021385908126831})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39309486746788025})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 4784], ['id', 45944], ['id', 41622], ['id', 2835], ['id', 20097]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7867995439420885, 1.5020821796780335, 2.093969267070918, 2.5036764541557126, 2.7490117913690852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9172865152359009})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5912483930587769})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5774112939834595})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6368763446807861})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6332415342330933})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6526362895965576})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.52493203125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.668939471244812})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5500024557113647})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4752524495124817})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.47336268424987793})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4401831030845642})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 31637], ['id', 49064], ['id', 52582], ['id', 34481], ['id', 41572]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6986597421854441, 1.3481497234309794, 1.8853767343578545, 2.2889703328823803, 2.554243609526006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0739848613739014})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7208290100097656})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6352394819259644})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6107400059700012})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5846858620643616})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6060100793838501})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7004694938659668})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6499724388122559})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7056114673614502})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.687137246131897})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7337969541549683})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6906642913818359})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7192999124526978})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7930519580841064})
store['active_learning_steps'][28]['training']['best_epoch']=11
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.597876806640625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6552861332893372})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4517214000225067})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.45228731632232666})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4464848041534424})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3992321193218231})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.36808282136917114})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.36437487602233887})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3540108799934387})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.36894717812538147})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 33364], ['id', 52971], ['id', 24533], ['id', 23896], ['id', 13018]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9432611043525576, 1.6844657242975525, 2.2458305664038996, 2.597520362060096, 2.7834090368880053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0355172157287598})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5790970921516418})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6130483150482178})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5709810256958008})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.557309627532959})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.642417311668396})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5675817728042603})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6154779195785522})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6270184516906738})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6844339370727539})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.488021044921875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6377641558647156})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4909006357192993})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4510084390640259})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.39106670022010803})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.389889657497406})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40574613213539124})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3807050585746765})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.37885332107543945})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 33812], ['id', 31883], ['id', 25321], ['id', 51759], ['id', 31067]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7348291588357485, 1.408475602875495, 1.9745895258234079, 2.3390682350990843, 2.5687981736161234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0035094022750854})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7364110946655273})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7293269634246826})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6758506298065186})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6320306062698364})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6702464818954468})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6714613437652588})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7333670854568481})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.5490162109375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6624265313148499})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5477516055107117})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4977644681930542})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4055677056312561})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4508257508277893})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4111427664756775})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.414680540561676})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 5630], ['id', 50343], ['id', 27930], ['id', 5059], ['id', 20930]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7707948907419679, 1.4661419631062884, 2.0477855234484457, 2.4761901312773107, 2.7348232470872356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9930917024612427})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6200011968612671})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5271768569946289})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5365756750106812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6088685393333435})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6187481880187988})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.513598779296875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6833282113075256})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.554955005645752})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.487556129693985})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46816423535346985})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4501420259475708})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 41999], ['id', 9436], ['id', 30900], ['id', 13242], ['id', 51131]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6125250675205065, 1.1765502858317074, 1.651643301963543, 2.04944286714856, 2.3127173658180347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9678454399108887})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6409334540367126})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5606197118759155})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6244346499443054})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5881940126419067})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5521235466003418})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6339371204376221})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6093961000442505})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6450908184051514})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9246, 'crossentropy': 0.5342322265625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6945742964744568})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48955419659614563})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.45062506198883057})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4410128593444824})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4242159128189087})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.42172771692276})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 1357], ['id', 42538], ['id', 20161], ['id', 42703], ['id', 12314]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7159648756211305, 1.3892363807338013, 1.9521682706422236, 2.396215739996186, 2.665915384125616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9752164483070374})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6560521125793457})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5240005254745483})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5816526412963867})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5321893095970154})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5550041198730469})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.50437919921875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6956319212913513})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5490247011184692})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5317767858505249})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.490607351064682})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4843815565109253})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 30884], ['id', 11693], ['id', 41295], ['id', 9681], ['id', 20852]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.756783568712593, 1.3874279544257813, 1.8806810477172888, 2.2282247750593793, 2.465025240893744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9053611755371094})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6018558144569397})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49617499113082886})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49179086089134216})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.530642569065094})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5341007709503174})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5366100072860718})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.936, 'crossentropy': 0.448703759765625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6351062059402466})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5327595472335815})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4362853169441223})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4255600571632385})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3878011703491211})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39178329706192017})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 17079], ['id', 11534], ['id', 56457], ['id', 3273], ['id', 57281]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7445773184787483, 1.3899526751640132, 1.8839111880850368, 2.2357499571569193, 2.4875245143640967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0388264656066895})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.555797815322876})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5098539590835571})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5133492946624756})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5256412029266357})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5119409561157227})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5185151100158691})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5195965766906738})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5343392491340637})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5520642995834351})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.54319167137146})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5356507897377014})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5412724018096924})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6319699883460999})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5936211943626404})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5410120487213135})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5559982657432556})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6973811388015747})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6362853050231934})
store['active_learning_steps'][35]['training']['best_epoch']=16
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9457, 'crossentropy': 0.491344482421875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5930873155593872})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.427196741104126})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.38022398948669434})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.37736043334007263})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35548728704452515})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35291463136672974})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3108753561973572})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3274480700492859})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.339094877243042})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3199145793914795})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 16951], ['id', 49050], ['id', 12536], ['id', 30016], ['ood', 20011]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8394315078500287, 1.6005360894812535, 2.258432267008365, 2.7034441867222823, 2.9811388553801113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9481316804885864})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.573786735534668})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.492168664932251})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5333486795425415})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4868406653404236})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5005585551261902})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4970385432243347})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.534605860710144})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.538780152797699})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5322710275650024})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.645331859588623})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5317319631576538})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5800513029098511})
store['active_learning_steps'][36]['training']['best_epoch']=10
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9435, 'crossentropy': 0.4461046875}
