store = {}
store['timestamp']=1622161721
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=36']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=36
store['worker_id']=36
store['num_workers']=40
store['config']={'seed': 1274, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.509113073348999})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7940356731414795})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.4583423137664795})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0745673179626465})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.5141797065734863})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.562791347503662})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.6893839836120605})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6597, 'crossentropy': 2.869567578125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 29246], ['id', 12906], ['id', 47643], ['id', 19423], ['id', 57642]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.3192915026991576, 2.3858436596027093, 3.2654732604706327, 3.8338899946067784, 4.181823951150164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.7859394550323486})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.871624231338501})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2005248069763184})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9839072227478027})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.8844337463378906})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.6221044063568115})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.439427375793457})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6706, 'crossentropy': 2.797012890625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 7897], ['id', 55660], ['id', 41945], ['id', 30359], ['id', 49824]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2938460049781124, 2.4204236271990123, 3.295601781292712, 3.8705595230255545, 4.20816003650179]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.111600875854492})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.5194101333618164})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.757481575012207})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 3.001251697540283})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 3.0269665718078613})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.264439105987549})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 3.017742156982422})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.369197130203247})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.7045412063598633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.9527037143707275})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.820852041244507})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 3.2284743785858154})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.897541046142578})
store['active_learning_steps'][2]['training']['best_epoch']=10
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7272, 'crossentropy': 2.7716138671875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 20333], ['id', 56063], ['id', 15867], ['id', 2803], ['id', 23867]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.3504831383952907, 2.5086278683190613, 3.386963594464156, 3.9580473184201876, 4.27991824674284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9288413524627686})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7958711385726929})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.1205811500549316})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.405658721923828})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.2822160720825195})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5555171966552734})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7249, 'crossentropy': 1.933734765625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 4767], ['id', 40456], ['id', 45446], ['id', 24038], ['id', 48789]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.2216201746259145, 2.273913480975323, 3.1004113427019, 3.7094046089856176, 4.087752273089901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9571776390075684})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.1766982078552246})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.5160698890686035})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.4367504119873047})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.6540110111236572})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.4858038425445557})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7043, 'crossentropy': 2.3344435546875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 528], ['id', 51127], ['id', 45753], ['id', 54258], ['id', 57985]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2422911397867538, 2.3008563537833586, 3.1621654529649508, 3.7772729602027617, 4.153827621387022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.723755955696106})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.8498573303222656})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.9326303005218506})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.015533447265625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.2132349014282227})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.296757459640503})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.264267921447754})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7298, 'crossentropy': 1.9078328125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 23859], ['id', 27514], ['id', 36434], ['id', 23294], ['id', 30064]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2150434573746272, 2.260569470676178, 3.081892725227359, 3.676004638586468, 4.048118780091556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5497339963912964})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.5646250247955322})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.9013042449951172})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.0005509853363037})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.117176055908203})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7676, 'crossentropy': 1.3756392578125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 38615], ['id', 29803], ['id', 41544], ['id', 33358], ['id', 55628]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1289845358337387, 2.155174426086084, 2.971189707904272, 3.566574595100974, 3.9628621655848892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.1438820362091064})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.4409866333007812})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.5629273653030396})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.557222604751587})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8295680284500122})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.997633457183838})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.7266511917114258})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7985, 'crossentropy': 1.36785693359375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 3791], ['id', 16692], ['id', 52462], ['id', 7833], ['id', 42112]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.165524849887565, 2.2277295365295116, 3.0953791320229573, 3.7066370692867485, 4.0976009988376205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.138361930847168})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.3717715740203857})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.4462562799453735})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.5382534265518188})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.791, 'crossentropy': 1.03864248046875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 23211], ['id', 20832], ['id', 29591], ['id', 11304], ['id', 11877]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9434250046103445, 1.6946464131959562, 2.3373597018511294, 2.876612725011869, 3.3095294345617567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3849523067474365})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4549801349639893})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.609468936920166})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.7994917631149292})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.5981009006500244})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.596614122390747})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.7474238872528076})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.7101842164993286})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8015, 'crossentropy': 1.3650109375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 21420], ['id', 729], ['id', 42703], ['id', 42343], ['id', 59726]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0889332128031295, 2.065404904982361, 2.9190351422919445, 3.5704081528371674, 4.007892304052046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0816650390625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2982107400894165})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2628793716430664})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4838480949401855})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4570789337158203})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2977255582809448})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.5398051738739014})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.637972354888916})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.6453871726989746})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8297, 'crossentropy': 1.2652189453125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 12950], ['id', 13318], ['id', 45488], ['id', 33659], ['id', 12341]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.123244403874018, 2.1908932369323146, 3.0703002469634537, 3.7067744916443672, 4.1177126963838315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.093458652496338})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.247049331665039})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1154279708862305})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3843384981155396})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3873021602630615})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4406499862670898})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8343, 'crossentropy': 1.11157080078125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 30047], ['id', 13348], ['id', 9533], ['id', 24982], ['id', 25910]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0629068917069069, 2.0233085567852713, 2.8462061858221137, 3.44590013947251, 3.8899314830741734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0362548828125})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0146492719650269})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2187442779541016})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3094302415847778})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.247183084487915})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.4493191242218018})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.837, 'crossentropy': 0.9864673828125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 46727], ['id', 50505], ['id', 20072], ['id', 2034], ['id', 19719]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0552147447579014, 1.9839467429010593, 2.7711633950309578, 3.379829753122519, 3.813687150284083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9006506204605103})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9116120338439941})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8451591730117798})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0332478284835815})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0346115827560425})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.07020902633667})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8859, 'crossentropy': 0.799803955078125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 32323], ['id', 16951], ['id', 7879], ['id', 47068], ['id', 29611]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1134537477664752, 2.1474326307306493, 2.9571327165713797, 3.5685018419834886, 3.980109827439688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9422709941864014})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8306601047515869})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8858504891395569})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8712232112884521})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9054819941520691})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9259011149406433})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0935289859771729})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8979, 'crossentropy': 0.755821826171875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 9428], ['id', 46329], ['id', 39700], ['id', 41537], ['id', 49890]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1873052883544808, 2.20934964408113, 3.0186691292861436, 3.6093100031402647, 4.005359614518592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9886949062347412})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9702259302139282})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8827797770500183})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8656107783317566})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0562002658843994})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.929043173789978})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9761139154434204})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0722230672836304})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.0765085220336914})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.1925277709960938})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8877, 'crossentropy': 0.914112890625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 24457], ['id', 22513], ['id', 50858], ['id', 8443], ['id', 49202]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.24864020508662, 2.3594322584787952, 3.1933283148213674, 3.8012967181839965, 4.176525475635357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9768642783164978})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8037302494049072})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7940811514854431})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7549848556518555})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8196707963943481})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9648549556732178})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8363253474235535})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.9274078607559204})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9543266296386719})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9333152770996094})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.7751212890625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 47568], ['id', 52169], ['id', 274], ['id', 9180], ['id', 26184]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.203468525661191, 2.2598465711832016, 3.118666114394344, 3.733728507572775, 4.112260844538236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9447565078735352})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7016065120697021})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7865445613861084})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8291870355606079})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8481301069259644})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.6456701171875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 55153], ['id', 5129], ['id', 42078], ['id', 12211], ['id', 19942]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9410286987481826, 1.7686961047688645, 2.480659032727144, 3.072987148371917, 3.5257427190027215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9374959468841553})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7160915732383728})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7679627537727356})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7451958656311035})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7903308868408203})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8032180070877075})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9540834426879883})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8413386344909668})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8470879793167114})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.68086640625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 59314], ['id', 32276], ['id', 29132], ['id', 46832], ['id', 7768]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.137318649495779, 2.157466264962534, 3.005645059288401, 3.6342667425249324, 4.047315632684268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9770908355712891})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7214013338088989})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7391378283500671})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7040009498596191})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7650955319404602})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7782745361328125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8047287464141846})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8856908082962036})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.8552267551422119})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.9252417087554932})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8096604347229004})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.795222818851471})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.721248046875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 13263], ['id', 7182], ['id', 46878], ['id', 59380], ['id', 12934]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2537343180319729, 2.3376286603671064, 3.1921982900879655, 3.789618115392459, 4.157725844682917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0039644241333008})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6795425415039062})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.673094630241394})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6972769498825073})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6987717151641846})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6994331479072571})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7765798568725586})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7209067344665527})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7482642531394958})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.713788628578186})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7034690380096436})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6841592788696289})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.8411768078804016})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.8046215772628784})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7730174660682678})
store['active_learning_steps'][20]['training']['best_epoch']=12
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9282, 'crossentropy': 0.624601611328125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 22687], ['id', 48968], ['id', 32427], ['id', 17055], ['id', 36417]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.263623948454307, 2.315788866404869, 3.2119233230243127, 3.7992337080613936, 4.168710396597275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9931365251541138})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6083462238311768})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6797229051589966})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6056345701217651})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6229699850082397})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6721063852310181})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6899977326393127})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7129855155944824})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7269469499588013})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6868890523910522})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.606463330078125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 43008], ['ood', 50403], ['id', 19501], ['id', 2761], ['id', 45602]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1431215632332352, 2.212207626620275, 3.0803653530250896, 3.720410666289153, 4.117886020643459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0889356136322021})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6273935437202454})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5556535720825195})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6207329034805298})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6164649724960327})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5674779415130615})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6162909865379333})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5768907070159912})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6722139120101929})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6381487250328064})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.935, 'crossentropy': 0.52067275390625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 29300], ['id', 33812], ['id', 1239], ['id', 8704], ['id', 38598]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1574794848460852, 2.2483406783153086, 3.1440213994692403, 3.8035266037066595, 4.166075732910285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0237085819244385})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6208536624908447})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6271737813949585})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6282440423965454})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.580794095993042})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6723257303237915})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6128133535385132})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.5581484375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 12663], ['id', 50578], ['id', 43278], ['id', 11643], ['id', 10690]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0534263900286256, 1.981485668205622, 2.752333630959958, 3.36038369030656, 3.80416523739534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1225948333740234})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6135709285736084})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5807598829269409})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5028786063194275})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5168675184249878})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5097975730895996})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5505645275115967})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.457516064453125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 50370], ['id', 626], ['id', 19188], ['id', 11346], ['id', 28192]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0061579306053618, 1.8926978654345263, 2.663873688655758, 3.288208189064255, 3.733189233949208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0752551555633545})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6156190037727356})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6690424680709839})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5945557355880737})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6071662306785583})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6200507879257202})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6183827519416809})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6075780391693115})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.499440478515625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 41108], ['id', 55496], ['id', 27596], ['id', 30493], ['id', 14631]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1475234920738917, 2.123684971135446, 2.968237068762865, 3.557505334393949, 3.96623799148124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9462143182754517})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5815951824188232})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5131038427352905})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5140713453292847})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.518945574760437})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5481090545654297})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9396, 'crossentropy': 0.4395294921875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 49493], ['id', 24752], ['id', 1518], ['id', 50743], ['id', 1814]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9373252504897907, 1.8204282820630526, 2.606737560280573, 3.1888525921789563, 3.635165818735704]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0166540145874023})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5605980157852173})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5144163370132446})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5184592008590698})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5187557339668274})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5402102470397949})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.439530810546875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 46412], ['id', 22083], ['id', 8047], ['id', 21438], ['id', 6106]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9005112930318953, 1.7162837811441904, 2.409125853345044, 2.9870665158261076, 3.4448370147747616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0840377807617188})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5517975687980652})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5406144857406616})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5259299874305725})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5559230446815491})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5121506452560425})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5335615873336792})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.46701318359375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 48360], ['id', 43961], ['id', 14872], ['id', 57728], ['id', 41572]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.0009580011582861, 1.9231209760641415, 2.703131284570791, 3.3261709548122402, 3.7780607705349745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9655483365058899})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5033546090126038})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4850139915943146})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4514651894569397})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42829787731170654})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4673832654953003})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44170498847961426})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5248030424118042})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4730041027069092})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5467550754547119})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49753889441490173})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5060509443283081})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.46783143281936646})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5466121435165405})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5303755402565002})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6317781805992126})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.502681314945221})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5585696697235107})
store['active_learning_steps'][29]['training']['best_epoch']=15
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9505, 'crossentropy': 0.4797958984375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 40494], ['id', 23140], ['id', 37219], ['id', 37048], ['id', 13714]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1652415370469473, 2.2285439968893463, 3.1164093386273484, 3.7376398742256978, 4.134708536347826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1108189821243286})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5173963308334351})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5122539401054382})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46528008580207825})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47472506761550903})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48666322231292725})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4845730662345886})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4309109151363373})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5605145692825317})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5471266508102417})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5055288672447205})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.421326220703125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 340], ['id', 18003], ['id', 36818], ['id', 26072], ['ood', 52590]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1657075735981208, 2.1831441982624824, 3.0543037898064638, 3.7040750523325077, 4.117206796797558]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1306668519973755})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6327727437019348})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.488498330116272})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44629016518592834})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40350258350372314})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4450535774230957})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46479639410972595})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4961088001728058})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.412040234375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 32391], ['id', 207], ['id', 24491], ['id', 19159], ['ood', 9287]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0954604655690536, 2.006940750124163, 2.788606625357259, 3.402130806131142, 3.844559569589732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1729278564453125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5884091854095459})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4504593014717102})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4260972738265991})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.424607515335083})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42063599824905396})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4252868890762329})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4441980719566345})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4708191156387329})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40892356634140015})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47880858182907104})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4545097351074219})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9549, 'crossentropy': 0.429451513671875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 36982], ['id', 3010], ['id', 32776], ['id', 53736], ['id', 21880]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.142622741220296, 2.2095929734950186, 3.0698006167920067, 3.715714106507013, 4.104475585729515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1976356506347656})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6044265031814575})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5005229711532593})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46281003952026367})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4312306046485901})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4481596350669861})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4543073773384094})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4127078652381897})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4963163435459137})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4869239926338196})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.43915730714797974})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.951, 'crossentropy': 0.3947111083984375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 4646], ['id', 20172], ['id', 46368], ['id', 47741], ['id', 52086]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1664464305838524, 2.235606708278934, 3.097778206390295, 3.6963321717627835, 4.090191095293472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1113446950912476})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5833300352096558})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4921839237213135})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4323251247406006})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42665860056877136})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39577263593673706})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38215306401252747})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3755950331687927})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4328397512435913})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4045536518096924})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4387034475803375})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.43256688117980957})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45693111419677734})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.37724580078125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 11711], ['id', 22272], ['id', 57276], ['id', 17540], ['id', 19868]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2268331510561628, 2.2373637232176873, 3.0555696330851028, 3.662658818593907, 4.053904032302386]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2992258071899414})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6050889492034912})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5361331701278687})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44668513536453247})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4684281349182129})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.458667516708374})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4478113651275635})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5614449381828308})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5220063328742981})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5240926742553711})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.408442724609375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 12651], ['id', 29530], ['id', 39561], ['id', 36409], ['id', 31710]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0840964834906122, 2.0572398551612787, 2.8970678762872115, 3.5330432681497133, 3.954354076899362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.2270638942718506})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6029644012451172})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4992974102497101})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4888310432434082})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46404212713241577})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4514102637767792})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4520578384399414})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49391186237335205})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4558348059654236})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48290565609931946})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9437, 'crossentropy': 0.437407080078125}
