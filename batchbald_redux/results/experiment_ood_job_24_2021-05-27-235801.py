store = {}
store['timestamp']=1622156281
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=24']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=24
store['worker_id']=24
store['num_workers']=40
store['config']={'seed': 1261, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2005574703216553})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4250848293304443})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.841845989227295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6365866661071777})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6956, 'crossentropy': 2.0028982421875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1400738954544067})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1268329620361328})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0852060317993164})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47615], ['id', 57523], ['id', 10515], ['id', 29576], ['id', 39253]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0598080935002094, 1.86957573291539, 2.4546506529502263, 2.843688946849385, 3.0783868136619326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.332650899887085})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.9331517219543457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7833614349365234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.4000706672668457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.326930522918701})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.2548105716705322})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6592, 'crossentropy': 2.5532287109375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2656614780426025})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1688915491104126})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2071027755737305})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2150802612304688})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2652244567871094})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 51286], ['id', 36281], ['id', 39963], ['id', 13899], ['ood', 44317]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0283791336544104, 1.8375504017273045, 2.4423719820751266, 2.831794102076464, 3.0757879326160404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.7607996463775635})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0652198791503906})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.502897262573242})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.422513484954834})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.583216667175293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.8615610599517822})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.8924026489257812})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.8069095611572266})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7223, 'crossentropy': 2.319578515625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1160820722579956})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0753698348999023})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0966906547546387})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0666613578796387})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0665932893753052})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 5947], ['id', 35340], ['id', 59702], ['id', 43434], ['id', 37365]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0002889484409563, 1.8501370492880986, 2.4898924748675855, 2.8918236035226705, 3.0922397351374737]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.361304521560669})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7085239887237549})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.7298287153244019})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.8813289403915405})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7874, 'crossentropy': 1.19236171875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.9212838411331177})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.8579611778259277})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.7942759990692139})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 53116], ['id', 9037], ['id', 32387], ['id', 19638], ['id', 55643]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8276272345562128, 1.4976606749619328, 2.051805172848211, 2.4620235828260135, 2.742947256763684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1043550968170166})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4467580318450928})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.59065580368042})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5984352827072144})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8082, 'crossentropy': 1.02418974609375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8569128513336182})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.7880977392196655})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8115110397338867})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 20692], ['id', 45094], ['id', 25086], ['id', 44184], ['id', 50535]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.739544416418735, 1.3315305082329618, 1.8047195885091885, 2.1781783183426553, 2.434588585117547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1383028030395508})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.276202917098999})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.379406213760376})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.4774099588394165})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6738988161087036})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.6617848873138428})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8245, 'crossentropy': 1.1314921875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7846687436103821})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.7329864501953125})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7422930002212524})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.6977592706680298})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 40547], ['id', 22824], ['id', 29240], ['id', 30022], ['id', 19037]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8142313922538593, 1.5285311133498847, 2.1072197946680182, 2.4697706788833917, 2.684896190782103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.032126545906067})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1671462059020996})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5011039972305298})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.498020887374878})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4769493341445923})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8469, 'crossentropy': 1.006890625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7521486282348633})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.6893390417098999})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.6820197701454163})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6646308898925781})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 28391], ['ood', 21374], ['id', 13516], ['id', 15743], ['id', 3392]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8840698511135636, 1.645507576294225, 2.2322638618301767, 2.652590318089862, 2.90882604936988]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0565552711486816})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0226645469665527})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0590851306915283})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2475359439849854})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2502930164337158})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3978159427642822})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2803823947906494})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.4914367198944092})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8548, 'crossentropy': 1.08552314453125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.7193969488143921})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.6651554703712463})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6128553748130798})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6406923532485962})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6206244230270386})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.5894083976745605})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 18782], ['id', 56914], ['id', 30079], ['id', 59447], ['id', 1589]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9113617771517215, 1.6525139802466065, 2.2348928828727956, 2.614495919106422, 2.8385387026978695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9257800579071045})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9667651653289795})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.183805227279663})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1088885068893433})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3392711877822876})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8565, 'crossentropy': 0.87616181640625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7292882204055786})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7002580165863037})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6170967817306519})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6021096110343933})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 11668], ['id', 38512], ['id', 23859], ['id', 37039], ['id', 13647]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7842966873530566, 1.4869328458229547, 2.017772955981947, 2.4031796477866827, 2.639485166819373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9525846242904663})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9830532073974609})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9237304925918579})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9405549764633179})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8845561742782593})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0320866107940674})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1391462087631226})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.245131254196167})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8885, 'crossentropy': 0.81879892578125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6662440299987793})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5552850365638733})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5232143998146057})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5152705907821655})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.48437005281448364})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 52686], ['id', 30511], ['id', 2076], ['id', 32894], ['id', 17798]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.907989549437128, 1.73991393292403, 2.3008100209160363, 2.6626824984325186, 2.8602916043568944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8403251767158508})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8133269548416138})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8302313089370728})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8537891507148743})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.938368022441864})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9989221096038818})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0461716651916504})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9969745874404907})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.7930029296875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7265410423278809})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.5975095629692078})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5311581492424011})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5051610469818115})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5093294382095337})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.49122780561447144})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.47660815715789795})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 50648], ['id', 17714], ['id', 12903], ['id', 28929], ['id', 21814]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8695023183498702, 1.6669259084092802, 2.3105766141268305, 2.6882912166373645, 2.895021413770734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7918487787246704})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.728522777557373})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.83543860912323})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7826399803161621})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7811806797981262})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.621822705078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6803739666938782})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5773918032646179})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5533662438392639})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49965664744377136})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 39668], ['id', 1674], ['id', 48852], ['id', 29713], ['id', 25018]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7303940240943334, 1.348134072483993, 1.8754195632002029, 2.264831701297128, 2.536312632125431]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8306921720504761})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7490960359573364})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7095893621444702})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8160791397094727})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8288453221321106})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.902292013168335})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9046, 'crossentropy': 0.6286380859375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6798305511474609})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5519908666610718})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.48548921942710876})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.495058536529541})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.4830992817878723})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 15402], ['id', 7933], ['id', 29002], ['id', 19501], ['id', 38656]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7879935368124273, 1.4766982677006628, 2.0486786541904287, 2.4517443490535697, 2.6782543462429285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8886120319366455})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7778229713439941})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7679647207260132})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8266379833221436})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7694683074951172})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8304657340049744})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8958, 'crossentropy': 0.6965587890625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6409515142440796})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5417817831039429})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5126436948776245})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4874601364135742})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.46986064314842224})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 49734], ['id', 49545], ['id', 35344], ['id', 48486], ['id', 27829]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9113375091235201, 1.6345655670459789, 2.2277621853376797, 2.6212697559448994, 2.852557236272636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9160652160644531})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7504912614822388})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7107142210006714})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8119223117828369})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7845666408538818})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7044503688812256})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8089022636413574})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8756886720657349})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9001836180686951})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9113, 'crossentropy': 0.66553125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6461824178695679})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.557245135307312})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4753197431564331})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4682842791080475})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.43654894828796387})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.41862988471984863})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4275071322917938})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.41787949204444885})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 2092], ['id', 59887], ['id', 8763], ['id', 37483], ['id', 4058]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9086758402335762, 1.6368663276397313, 2.2338863357586165, 2.658465564683257, 2.8731874456843682]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8539009690284729})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7024838924407959})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6937217712402344})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7275740504264832})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6892900466918945})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7487514019012451})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.724126935005188})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7129660248756409})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7466179132461548})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8092195391654968})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.8296052813529968})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7893288135528564})
store['active_learning_steps'][15]['training']['best_epoch']=9
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.632685546875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6034308075904846})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5157443284988403})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4398678243160248})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4285205006599426})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4305151104927063})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.40211009979248047})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.39655613899230957})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.39635688066482544})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.37500429153442383})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.38978129625320435})
store['active_learning_steps'][15]['eval_training']['best_epoch']=7
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 45944], ['id', 45121], ['id', 20171], ['id', 31608], ['ood', 43592]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8576705763319168, 1.631000468219022, 2.216334489643482, 2.599674262365821, 2.795660264893825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9432929754257202})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6821471452713013})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6242353916168213})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5979673266410828})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7135522365570068})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6751261353492737})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7283673882484436})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7579448223114014})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.6072328125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6410958766937256})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5024738907814026})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4966895878314972})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.47675591707229614})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4587157964706421})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4274633526802063})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.407944917678833})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 27105], ['id', 4646], ['id', 27930], ['id', 18656], ['id', 5163]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8664516174930619, 1.6484678659553982, 2.287804035540403, 2.6781167515440494, 2.8774418687603758]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8789471387863159})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6354873180389404})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6088919639587402})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6209105849266052})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6274121999740601})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7090146541595459})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7023043632507324})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.53368330078125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6710148453712463})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4889683127403259})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.458264023065567})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4491555094718933})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4351044297218323})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4190216064453125})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 36658], ['id', 42886], ['id', 47597], ['id', 50236], ['id', 20648]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7243395792132137, 1.3797228789304263, 1.9056594464307066, 2.280449806893504, 2.5520396277543522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9187663793563843})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6354414224624634})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5785375237464905})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6525840163230896})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6555758714675903})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6687015295028687})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6947507858276367})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6978021860122681})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.5621005859375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.641579270362854})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5000871419906616})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4502145051956177})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.41975146532058716})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.42469727993011475})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.42398643493652344})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40423583984375})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 15679], ['id', 8458], ['id', 14295], ['id', 44206], ['id', 10393]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7771044911596376, 1.5086942280614513, 2.0924321564288997, 2.484852283188279, 2.678353099665779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9385755062103271})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6658892631530762})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6751483082771301})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7102640867233276})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7643885612487793})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7701590061187744})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7662524580955505})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7114493250846863})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7645092606544495})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7793631553649902})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7307741045951843})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8189619183540344})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8085678219795227})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8228815793991089})
store['active_learning_steps'][19]['training']['best_epoch']=11
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9196, 'crossentropy': 0.6298470703125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6315446496009827})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.503608226776123})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4412629008293152})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4089242219924927})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.40290647745132446})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.41565436124801636})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4095419645309448})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4054591655731201})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.37530940771102905})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.3735641837120056})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.38121533393859863})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3729668855667114})
store['active_learning_steps'][19]['eval_training']['best_epoch']=9
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 38068], ['id', 16823], ['id', 50366], ['id', 39543], ['id', 2061]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9294655822362787, 1.7006461902850218, 2.3160816316388777, 2.746216763420944, 3.019990680453594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9621363878250122})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6185726523399353})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5755401253700256})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6022924184799194})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5760869383811951})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6103441119194031})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6693727374076843})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6969690322875977})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.516617626953125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6524966955184937})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4738519787788391})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.40558385848999023})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4091099500656128})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3611169755458832})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37247613072395325})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3374277949333191})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 14063], ['id', 28215], ['id', 57377], ['id', 49202], ['id', 27403]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7749325738301835, 1.4321859849533594, 1.9930223561412754, 2.3993108026153367, 2.656201720217762]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9091556072235107})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6188533902168274})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5885136127471924})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6216217279434204})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6027264595031738})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6779731512069702})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6074472069740295})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6375495195388794})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.656631350517273})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6881746053695679})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.935, 'crossentropy': 0.510062890625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5655875205993652})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45147255063056946})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3984161913394928})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3742032051086426})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3809623122215271})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3624681234359741})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.34748977422714233})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 52169], ['id', 44065], ['id', 47140], ['id', 3193], ['id', 7207]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8312712986317952, 1.5862307678211298, 2.188472311503654, 2.6148299727531263, 2.8051057869076725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9695326685905457})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6462263464927673})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5754706263542175})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5471808314323425})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.587171196937561})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6223082542419434})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5653255581855774})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6017008423805237})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6463330388069153})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6587235331535339})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6231178045272827})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7752386331558228})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.670485258102417})
store['active_learning_steps'][22]['training']['best_epoch']=10
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.55287646484375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6051431894302368})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.47028809785842896})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40722590684890747})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4044903516769409})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3464808464050293})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3794071078300476})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.33589786291122437})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.33560413122177124})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.336638480424881})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.32598036527633667})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 23628], ['id', 38559], ['id', 37078], ['id', 35064], ['id', 39135]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9216851596369935, 1.7068530089708998, 2.3083653324531364, 2.7140181539236803, 2.9079004577655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9584465026855469})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5839064121246338})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.574105978012085})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5803396105766296})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6094961166381836})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5745911598205566})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6078511476516724})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5772905945777893})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6593656539916992})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.662493109703064})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5848287343978882})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.505131689453125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5891692042350769})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4563833475112915})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.39722469449043274})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4086272716522217})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.35269197821617126})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3516469895839691})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3612982928752899})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.3378835618495941})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 2036], ['id', 5315], ['ood', 59616], ['id', 22649], ['id', 27324]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7722185490489246, 1.4779798588597934, 2.0604251029260814, 2.4711122477170697, 2.740482666910724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0720343589782715})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6163132190704346})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.54304039478302})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5294427871704102})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4839059114456177})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5204464197158813})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5790760517120361})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6209105849266052})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5309627056121826})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.507879833984375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6276471614837646})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4655488133430481})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.41834211349487305})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.42499226331710815})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3851992189884186})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.36458486318588257})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.35496073961257935})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3360477089881897})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 57882], ['id', 11648], ['id', 10716], ['id', 21806], ['id', 24728]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.830098721240514, 1.5025814099537635, 2.037836886830582, 2.3880909043401584, 2.610293835670727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8440483808517456})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49557679891586304})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4832230806350708})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4500539302825928})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4814459979534149})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44137537479400635})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5286561250686646})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5220512747764587})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5472145080566406})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.429548291015625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6883929371833801})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4268023371696472})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3774970769882202})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3572571873664856})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.36599692702293396})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.33332914113998413})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3295224905014038})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3232201039791107})
store['active_learning_steps'][25]['eval_training']['best_epoch']=8
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 6466], ['id', 53324], ['id', 2236], ['id', 39031], ['id', 20120]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6974334145307179, 1.3339390261140363, 1.8621589035654988, 2.241491876778965, 2.4648489412795183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0021711587905884})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5519813299179077})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5121222734451294})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5436327457427979})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5138672590255737})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5396536588668823})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.604660153388977})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4993201494216919})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.45030166015625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.625701904296875})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4533478617668152})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4210127592086792})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.41288262605667114})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.37773001194000244})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.36914652585983276})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3373377323150635})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 8942], ['id', 27292], ['id', 3010], ['id', 35051], ['id', 49515]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7484935100445882, 1.4122804952671308, 1.959104219223894, 2.336025190624225, 2.5587801366525014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1840794086456299})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6297819018363953})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5796566009521484})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5812795162200928})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5104179382324219})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5629411935806274})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.612956166267395})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5576329231262207})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.46633232421875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6475369930267334})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46667343378067017})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.41427528858184814})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.41347870230674744})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.38485464453697205})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.3663899600505829})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.367548406124115})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 37048], ['id', 54030], ['id', 36452], ['id', 56735], ['id', 12089]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8045639035515277, 1.4807197394427862, 2.0091560818885217, 2.3721356137031364, 2.5906009808202732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9747133255004883})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5473096370697021})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5824471712112427})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.52080237865448})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.46204084157943726})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47457998991012573})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5280008316040039})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5414713621139526})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5704882740974426})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6093745231628418})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6106061935424805})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5349454879760742})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6583980917930603})
store['active_learning_steps'][28]['training']['best_epoch']=10
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.494624169921875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6618462800979614})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.46426811814308167})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.40271472930908203})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37761902809143066})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.34566402435302734})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.3776376247406006})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3587486743927002})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3563862144947052})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3378024697303772})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3089629113674164})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 59344], ['id', 20386], ['id', 20322], ['id', 34500], ['id', 26762]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8899080460546565, 1.61929578974024, 2.197207580004865, 2.569513482534231, 2.7657463717917787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.329219102859497})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.615557849407196})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.503516435623169})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4590332508087158})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48331958055496216})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.476007342338562})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4557463526725769})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49242204427719116})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4613327980041504})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46585404872894287})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47640058398246765})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5088263154029846})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9517, 'crossentropy': 0.41851318359375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6233459711074829})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46745550632476807})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41821885108947754})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3651861548423767})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.342864990234375})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.328209787607193})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.323691189289093})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2971946597099304})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.27946001291275024})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3125571310520172})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.2975027561187744})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 28536], ['id', 41054], ['id', 17121], ['id', 55513], ['id', 42547]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8827123339926939, 1.6341080265654133, 2.250122200810539, 2.624359009892581, 2.8262842095815435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1889207363128662})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6386499404907227})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.521744966506958})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5113242864608765})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4709661602973938})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4766429662704468})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49945268034935})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5414552688598633})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9413, 'crossentropy': 0.411512353515625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6554076671600342})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5308386087417603})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4166548252105713})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3764631152153015})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34936392307281494})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39378607273101807})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3743809163570404})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 5600], ['id', 14580], ['id', 49525], ['id', 49070], ['id', 3290]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7330191466585734, 1.3440768376252095, 1.8714282216124714, 2.2310584502202415, 2.4669977546648703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1112275123596191})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.624913215637207})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5331208109855652})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47143781185150146})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5085893273353577})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4821242094039917})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5433539152145386})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4968706965446472})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9422, 'crossentropy': 0.432381396484375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.649519681930542})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.484624445438385})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4342045187950134})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3791912794113159})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37090325355529785})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3601086437702179})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3626164197921753})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 28392], ['id', 3798], ['id', 8170], ['id', 31562], ['id', 50180]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7645069254667294, 1.3908224668706133, 1.9257099081151683, 2.3231364711762446, 2.5456658535672734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.184455156326294})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6258319616317749})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4729376435279846})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4644884467124939})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5126204490661621})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4789254665374756})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4727827310562134})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9436, 'crossentropy': 0.423332568359375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6537719964981079})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4622989594936371})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.44110655784606934})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41469722986221313})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3708958625793457})
store['active_learning_steps'][32]['eval_training']['best_epoch']=2
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 39421], ['id', 44095], ['id', 11889], ['id', 5370], ['id', 34308]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7203278615512925, 1.2899324822900735, 1.7612972353868575, 2.127699689608778, 2.4022391601639415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.203345537185669})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5837222337722778})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5203604698181152})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4609609544277191})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4627237319946289})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45419496297836304})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47071921825408936})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4728858470916748})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4472782015800476})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5182887315750122})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5161857604980469})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5343412756919861})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9464, 'crossentropy': 0.432422265625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6665458679199219})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48394349217414856})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4156014323234558})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.37827765941619873})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.34136050939559937})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3393424153327942})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33098554611206055})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.315150648355484})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3332468271255493})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.31018102169036865})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 32747], ['id', 22139], ['id', 36818], ['id', 53136], ['id', 39151]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7847848518978822, 1.4772242362014634, 2.03210782554265, 2.452079967604141, 2.707709418526834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1498808860778809})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6634936332702637})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4866738021373749})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43158310651779175})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47924941778182983})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5158247947692871})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48783427476882935})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44129472970962524})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9442, 'crossentropy': 0.413434765625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6479946970939636})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5092244744300842})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4532931447029114})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4119264483451843})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.37742364406585693})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4112629294395447})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34189674258232117})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 9439], ['id', 3030], ['id', 45917], ['id', 47662], ['id', 26516]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7828037296674262, 1.4277918826016212, 1.9670046708022921, 2.3224997979978275, 2.5675436901648174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1793386936187744})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.634791374206543})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5440480709075928})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49945950508117676})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5180354714393616})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48492079973220825})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5225257873535156})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5203367471694946})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4415885806083679})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5054379105567932})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5223569273948669})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5288996696472168})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5743622183799744})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4881257712841034})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5560691356658936})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5893099904060364})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6177195310592651})
store['active_learning_steps'][35]['training']['best_epoch']=14
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9518, 'crossentropy': 0.43352138671875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6516059637069702})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42980313301086426})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.38930845260620117})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3373785614967346})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35005807876586914})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33049654960632324})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3185986280441284})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.29813265800476074})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3129287362098694})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29735082387924194})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.287761390209198})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.285915344953537})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27457350492477417})
store['active_learning_steps'][35]['eval_training']['best_epoch']=10
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 14619], ['id', 48480], ['id', 39047], ['id', 27596], ['id', 57914]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8303567996292778, 1.6070647677069978, 2.2325270847843166, 2.6730501628992442, 2.88213406572466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.1467158794403076})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5864099860191345})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48558107018470764})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4449204206466675})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.48007309436798096})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4652244448661804})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48044246435165405})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.505059003829956})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.42716220703125}
