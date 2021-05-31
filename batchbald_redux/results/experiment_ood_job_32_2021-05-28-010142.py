store = {}
store['timestamp']=1622160102
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=32']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=32
store['worker_id']=32
store['num_workers']=40
store['config']={'seed': 1270, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.9167261123657227})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.3811326026916504})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3278021812438965})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0156688690185547})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7158, 'crossentropy': 1.8141203125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0835151672363281})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.005325198173523})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0429811477661133})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 49149], ['id', 46707], ['id', 259], ['id', 16033], ['id', 4873]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1125951367951004, 1.8893945097120897, 2.4419918430611487, 2.8129639654720204, 3.053690203007257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.0405752658843994})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.080897331237793})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.614964008331299})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.3595616817474365})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.5480520725250244})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.6985116004943848})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.6197686195373535})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7473, 'crossentropy': 2.109180859375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9947553873062134})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0077062845230103})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.9538293480873108})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.014925241470337})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.012589454650879})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9895690679550171})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 917], ['id', 12943], ['id', 20283], ['id', 4758], ['ood', 26462]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0472911519467034, 1.9078547629087699, 2.579844681199205, 2.9939343231243534, 3.220190185437283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5224933624267578})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.6002439260482788})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.7469091415405273})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.953836441040039})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.9933747053146362})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7789, 'crossentropy': 1.4544517578125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.9758996963500977})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.9357701539993286})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9033791422843933})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.879133939743042})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 20273], ['id', 16936], ['id', 21182], ['id', 28040], ['id', 26842]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9296097294528711, 1.7160343260333293, 2.3254573466397694, 2.749772076688787, 3.0303475268697984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.3206087350845337})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.416629672050476})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.6541699171066284})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7051918506622314})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.8199864625930786})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8059, 'crossentropy': 1.31086083984375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8816571235656738})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8171115517616272})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8095388412475586})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8082504272460938})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 57808], ['id', 6520], ['id', 31415], ['id', 14669], ['id', 45761]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.894970341240596, 1.7264331241083308, 2.358509999377193, 2.7428128551962994, 2.9623347022344335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.368579387664795})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.5530322790145874})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.7170512676239014})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.9057362079620361})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.8198647499084473})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8148, 'crossentropy': 1.285973046875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8888707756996155})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.7887468338012695})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.7620553970336914})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.7879981994628906})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 26412], ['id', 10038], ['id', 20820], ['id', 18682], ['id', 2328]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8321570912672158, 1.5033663291867967, 2.058914754209585, 2.4058622134771106, 2.6398535747323937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2814888954162598})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4899303913116455})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.5059623718261719})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.6654691696166992})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7384276390075684})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.8305209875106812})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.7138607501983643})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.813659429550171})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.072448968887329})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.7181968688964844})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8115, 'crossentropy': 1.49367529296875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8316843509674072})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8256620168685913})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.8054563403129578})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.7781597375869751})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.7992621660232544})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 20486], ['id', 46336], ['id', 40786], ['id', 50930], ['id', 33611]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8750626817101625, 1.6633357937137232, 2.2603205287287995, 2.610364818700692, 2.7961687998899762]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0123852491378784})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2018136978149414})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2779505252838135})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.3128283023834229})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.39655601978302})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3079259395599365})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4181594848632812})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.5546879768371582})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.8276808261871338})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8149, 'crossentropy': 1.1875701171875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8170734643936157})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.7225669026374817})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.6961145401000977})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.6978703737258911})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.6976610422134399})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.6873345971107483})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.6918559670448303})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.6754143238067627})
store['active_learning_steps'][6]['eval_training']['best_epoch']=8
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 19590], ['id', 58073], ['id', 22229], ['id', 21566], ['id', 5422]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9895800770599383, 1.7824851635070398, 2.4189090077871134, 2.7822759042473084, 2.9725104667606743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1315994262695312})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2037584781646729})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3574247360229492})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.4554784297943115})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.7242588996887207})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6161892414093018})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8154, 'crossentropy': 1.1799673828125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8225363492965698})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7185355424880981})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7127037048339844})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7354393005371094})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7188311815261841})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 17673], ['id', 6152], ['id', 52169], ['id', 11364], ['id', 26344]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7317517369076605, 1.3986088969985513, 1.9560200799387095, 2.3277139080930045, 2.5412971639623443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0425560474395752})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1866086721420288})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.2174439430236816})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3753972053527832})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8162, 'crossentropy': 0.96872607421875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.930935263633728})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8262227177619934})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.8562782406806946})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 35274], ['id', 29462], ['id', 36421], ['id', 9442], ['id', 45180]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6903546559164677, 1.2707750572000793, 1.7773211319256896, 2.173497574377011, 2.4613260048539853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.956608772277832})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0127161741256714})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1671292781829834})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.310471534729004})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4918357133865356})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.51531982421875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.4417304992675781})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8355, 'crossentropy': 1.0740166015625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.834226667881012})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.7182286381721497})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.691968560218811})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.6619176864624023})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.691521942615509})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.6852198839187622})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 41468], ['id', 52729], ['id', 58341], ['id', 5000], ['id', 20171]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8254985185176387, 1.5479681571006494, 2.1522957388089043, 2.578108374053304, 2.8103199586690435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0361294746398926})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9614051580429077})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0441633462905884})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1657968759536743})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1382631063461304})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8524, 'crossentropy': 0.811659765625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.7993717193603516})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6906739473342896})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6780401468276978})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.6587129235267639})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 17756], ['id', 3543], ['id', 42329], ['id', 1423], ['id', 51154]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8426935017161408, 1.5598247059328392, 2.1508224573521018, 2.5526901824019923, 2.796965883838036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0848513841629028})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0184171199798584})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9368926882743835})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1047933101654053})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0809736251831055})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.208858609199524})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2660670280456543})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2942173480987549})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8702, 'crossentropy': 0.9056810546875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7823252081871033})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5940374135971069})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.5970276594161987})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6044762134552002})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.5707063674926758})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 5062], ['id', 18324], ['id', 9789], ['id', 7229], ['id', 8202]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8894330906744874, 1.6878260306198625, 2.28735901518883, 2.663940480156249, 2.866090813523055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1051945686340332})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9155830144882202})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.121252179145813})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0334248542785645})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1134074926376343})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1882493495941162})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1811599731445312})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2502710819244385})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8625, 'crossentropy': 0.90450302734375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.7755928039550781})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6310744285583496})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.602555513381958})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.5763627886772156})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.5644571781158447})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5431251525878906})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.5462633967399597})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 24479], ['id', 43648], ['id', 26785], ['id', 52679], ['id', 50352]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9230025635667285, 1.71246653654716, 2.3162524335274686, 2.673151412275165, 2.8500792708878775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1017557382583618})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.917163074016571})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9135704040527344})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.947198748588562})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0145169496536255})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0566675662994385})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1974666118621826})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1364456415176392})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8821, 'crossentropy': 0.82654248046875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6960396766662598})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5888686180114746})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5519709587097168})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.522620439529419})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5281939506530762})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5094075202941895})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 9118], ['id', 497], ['id', 42774], ['id', 15759], ['id', 36491]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8505267629231039, 1.5897805798415234, 2.1935436743441086, 2.619624758569822, 2.8873459915470523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9600950479507446})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8112916350364685})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8812367916107178})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.898604154586792})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9279959201812744})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8777, 'crossentropy': 0.7093736328125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7511279582977295})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6541868448257446})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6107305288314819})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.549022376537323})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 21880], ['id', 45073], ['id', 47949], ['id', 28512], ['id', 49515]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6918004069218338, 1.3085135272445472, 1.8374627777362296, 2.238981511591019, 2.4862745664462915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.836208701133728})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7058486938476562})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7835179567337036})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6730117797851562})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7509613633155823})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7568892240524292})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9591776132583618})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8294358253479004})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.66328193359375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6177785396575928})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.524459958076477})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.47337478399276733})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4735557734966278})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4499939978122711})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.46046966314315796})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.45308423042297363})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 42078], ['id', 20641], ['id', 42703], ['ood', 12689], ['id', 38543]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8105303952699279, 1.5480198910180127, 2.140342204505746, 2.5332958743553444, 2.7602970811690595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8837205171585083})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8055530786514282})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7234472036361694})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6942390203475952})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7218612432479858})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7586764097213745})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.586372412109375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6686948537826538})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5657737255096436})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5269184112548828})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4689292311668396})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4576382040977478})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 57728], ['id', 2765], ['id', 14367], ['id', 49034], ['id', 39827]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8060951647268744, 1.4709805725689629, 2.010086826122378, 2.3813139411868534, 2.5908384875211556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0495208501815796})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7283811569213867})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7739040851593018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7265618443489075})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7556277513504028})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.771979808807373})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8314577341079712})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8305603861808777})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8948518633842468})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9364524483680725})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.71384140625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6883878111839294})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5165126323699951})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4859824776649475})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5009177327156067})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4896848797798157})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.47775328159332275})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 33224], ['id', 30451], ['ood', 14563], ['id', 22083], ['ood', 38890]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8830555513865834, 1.6071367032852075, 2.1981148076482624, 2.6024113223302736, 2.8513155466920264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0814265012741089})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8007740378379822})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8314917087554932})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7577602863311768})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8826280832290649})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8094931840896606})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9605015516281128})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8837, 'crossentropy': 0.695958154296875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7219016551971436})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.5629310607910156})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.563712477684021})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.531566858291626})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5315183997154236})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.502343475818634})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 14825], ['id', 47260], ['id', 31293], ['id', 48824], ['id', 5003]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7212777917960249, 1.382400486810305, 1.9116399519988478, 2.292431376405615, 2.5719458746007344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9251693487167358})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6352531909942627})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6565548181533813})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5890550017356873})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6671409606933594})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6659733057022095})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6707398891448975})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7680670022964478})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6991581916809082})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6734912991523743})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7320887446403503})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8388180732727051})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8519388437271118})
store['active_learning_steps'][19]['training']['best_epoch']=10
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.6325314453125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6666916608810425})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.528648853302002})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4688217341899872})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.45803335309028625})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.41358593106269836})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4097881317138672})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.41577792167663574})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3904164433479309})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.3930061459541321})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.3873811364173889})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.37996554374694824})
store['active_learning_steps'][19]['eval_training']['best_epoch']=8
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 45488], ['id', 2148], ['id', 34946], ['id', 11789], ['id', 39074]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.825262621702472, 1.5771762646407401, 2.1772608248751926, 2.5994630474358384, 2.841348960168262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0825127363204956})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.709203839302063})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6144697666168213})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6447773575782776})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6107460260391235})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5988866090774536})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5769239068031311})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6177490949630737})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6891772747039795})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.5429177734375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6668210029602051})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5269063711166382})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4521571099758148})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43846040964126587})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.39961081743240356})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4103786051273346})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3900642395019531})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 32519], ['id', 16190], ['id', 10050], ['id', 35494], ['id', 40639]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7400147565724321, 1.3516211998891423, 1.8621167509547494, 2.273432282829278, 2.546493883395182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9848262071609497})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6335839033126831})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6296219825744629})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6385892629623413})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6350306272506714})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6286567449569702})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6820816993713379})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.5577490234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6912199258804321})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5210282802581787})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.49107521772384644})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.45857182145118713})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46254047751426697})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4460009038448334})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 8847], ['id', 27964], ['id', 5315], ['id', 25783], ['id', 20190]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7121540963481996, 1.3579278224826443, 1.9128423728802861, 2.3174272962812985, 2.5947316824377005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9249467849731445})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5955307483673096})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5806264877319336})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5827865600585938})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6088899374008179})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5601323843002319})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.646247386932373})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6785005331039429})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6885135173797607})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6532273292541504})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.720106840133667})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6839144229888916})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7298579216003418})
store['active_learning_steps'][22]['training']['best_epoch']=10
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.598722314453125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6155420541763306})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.46486780047416687})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43787992000579834})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4202137589454651})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.41382455825805664})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.3898535370826721})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 5470], ['id', 21304], ['id', 54647], ['id', 10184], ['id', 21900]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9592636140606734, 1.7557794100561752, 2.303875051791951, 2.6569355678231013, 2.8614419015632313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0320361852645874})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6398037672042847})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5728110671043396})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5676184296607971})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5151053667068481})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.543755829334259})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6008284091949463})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6640543937683105})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.474103857421875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7207560539245605})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4890108108520508})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4375338554382324})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.40296509861946106})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3952510356903076})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.41539227962493896})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.37763452529907227})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 30298], ['id', 27793], ['id', 25330], ['id', 40944], ['id', 35086]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7396457756600112, 1.4347836875320237, 1.9915172348738475, 2.4110685008303383, 2.6814189858102653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9150357246398926})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5562676787376404})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5584225058555603})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5753791332244873})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6201092600822449})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6011582016944885})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5931746363639832})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.519105908203125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6477237939834595})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.522412896156311})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4825249910354614})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.44299745559692383})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.431546688079834})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.40190553665161133})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 55442], ['id', 29289], ['id', 12257], ['ood', 4379], ['ood', 7444]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7048621154638834, 1.3126105427715524, 1.8550167664641926, 2.254751751303937, 2.5314117881315665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9116629362106323})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6036019325256348})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5821895599365234})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5275508165359497})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5033645629882812})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5377820730209351})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6068820953369141})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6253800392150879})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6687619686126709})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9246, 'crossentropy': 0.49349228515625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6270897388458252})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45749449729919434})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4513328969478607})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4250785708427429})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.38862326741218567})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3702693581581116})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4091116189956665})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3854430317878723})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 1282], ['id', 59466], ['id', 4983], ['id', 59701], ['id', 42810]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7609476862130562, 1.3888646640725182, 1.9485788591828008, 2.328632193845775, 2.568547380689063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0390708446502686})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5566348433494568})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.49396848678588867})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4935591518878937})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.491090327501297})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5185829401016235})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.524397611618042})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4851982593536377})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9346, 'crossentropy': 0.42265087890625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6170313358306885})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.46243926882743835})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4301111698150635})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39954161643981934})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3640592694282532})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3488473892211914})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.3659626245498657})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 59294], ['id', 1357], ['id', 46187], ['id', 50317], ['id', 30932]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6821758306005266, 1.2907799866796887, 1.8119233069111615, 2.197637608792161, 2.417231840233381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.085006833076477})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5834101438522339})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5389413237571716})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5707809925079346})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5081967115402222})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5757626295089722})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5959510803222656})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6129171848297119})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.46476943359375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6455153226852417})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5048161745071411})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.43916648626327515})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4744061231613159})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.41726478934288025})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.37744003534317017})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39951154589653015})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 40437], ['id', 26072], ['id', 34610], ['id', 38275], ['id', 11598]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7621058995290255, 1.4481240218830052, 2.0052574383742012, 2.3963153638551775, 2.619051193534494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1277832984924316})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.572848916053772})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48886048793792725})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4850853681564331})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5217053890228271})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5367524027824402})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5233296751976013})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.41722001953125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6544846296310425})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5194424986839294})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46971049904823303})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.411628395318985})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4073435664176941})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35313430428504944})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 9390], ['id', 29834], ['id', 509], ['id', 12190], ['id', 49064]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6875206109795455, 1.2971915291244698, 1.8168059711642144, 2.21718884060809, 2.4903419081721534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9935103058815002})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5797920227050781})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.47918808460235596})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47118037939071655})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.488827109336853})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4874289333820343})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48341870307922363})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.430626953125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6948828101158142})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5557982325553894})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4440910816192627})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4668155312538147})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4208224415779114})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4122992753982544})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 49543], ['id', 30900], ['id', 18598], ['id', 24943], ['id', 14201]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6420859254917792, 1.2252996856536544, 1.7176783137313096, 2.10152415145728, 2.3781753783383497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0855486392974854})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.655413031578064})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5122666358947754})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5197465419769287})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4988304376602173})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5070114135742188})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5354753136634827})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5105447769165039})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5148433446884155})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5363101959228516})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5672659873962402})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6332024931907654})
store['active_learning_steps'][30]['training']['best_epoch']=9
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.468064892578125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6469429731369019})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.46514108777046204})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.47948843240737915})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4136483669281006})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3511277437210083})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36812904477119446})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3478038012981415})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.34907418489456177})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3318087160587311})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3175486922264099})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3458123803138733})
store['active_learning_steps'][30]['eval_training']['best_epoch']=10
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 11342], ['id', 5227], ['id', 45777], ['id', 34968], ['id', 31710]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8475259282327008, 1.5732164418308288, 2.16702412310163, 2.6134700764993237, 2.857039783422283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0983362197875977})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5558090209960938})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4976327419281006})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4413471221923828})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44265902042388916})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46567195653915405})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5125585794448853})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5183054208755493})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.41152978515625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6261253356933594})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5023473501205444})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43220484256744385})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4339748024940491})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.41423696279525757})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4168999195098877})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39611995220184326})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 11536], ['id', 16809], ['id', 48382], ['id', 36818], ['id', 56366]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6319293385605191, 1.2151967179627814, 1.721292806500255, 2.1095458913763867, 2.377076937535283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0163182020187378})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5341929197311401})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47290387749671936})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45759573578834534})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44379884004592896})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4610871374607086})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46314147114753723})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4504276514053345})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9428, 'crossentropy': 0.415188818359375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6517418622970581})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5039749145507812})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3919892907142639})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3942831754684448})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.35505151748657227})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3903888463973999})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 50461], ['id', 39208], ['id', 51652], ['id', 27323], ['id', 53957]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6811999111741405, 1.2946814006920322, 1.8125955434043375, 2.1834651657142095, 2.438004373772702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1893796920776367})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6090199947357178})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5019362568855286})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4714106619358063})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4444164037704468})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.459449827671051})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45977434515953064})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4934486150741577})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.42747373046875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.634059488773346})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49355509877204895})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.41880279779434204})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3867867887020111})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34925907850265503})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.36958861351013184})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.33692070841789246})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 30884], ['id', 43796], ['id', 4110], ['id', 49890], ['id', 21066]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7984968692388845, 1.4540709411559418, 1.9729974465480007, 2.3594375993048153, 2.593630586242414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1613024473190308})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5873334407806396})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5112357139587402})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4185008406639099})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.42098715901374817})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4218071401119232})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4394826889038086})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9401, 'crossentropy': 0.4040141845703125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7090606689453125})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5058050155639648})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43145912885665894})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40318962931632996})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37717556953430176})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37000221014022827})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 50403], ['id', 29530], ['id', 16196], ['id', 26958], ['id', 11795]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6395239328368238, 1.2133942298534897, 1.7140239644227568, 2.101079794494165, 2.3768133070135615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.228225588798523})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.625370979309082})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4997524619102478})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4321616291999817})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4192001223564148})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38903191685676575})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4043067693710327})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4380829930305481})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4605170488357544})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4314476549625397})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9425, 'crossentropy': 0.41019384765625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.685551106929779})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.42698970437049866})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4181673526763916})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36565402150154114})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33818209171295166})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36945095658302307})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31605225801467896})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3041835427284241})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.321905255317688})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 31941], ['id', 47513], ['id', 48775], ['id', 12236], ['id', 18674]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6924875514520319, 1.313494652212185, 1.8114300442703808, 2.1916152938382805, 2.444771633869286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1842281818389893})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5764062404632568})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44542717933654785})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4133216440677643})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38533815741539})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4633290767669678})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41394340991973877})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42820876836776733})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.369240625}
