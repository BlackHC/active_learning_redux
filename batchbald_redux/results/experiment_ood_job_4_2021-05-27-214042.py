store = {}
store['timestamp']=1622148042
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=4']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=4
store['worker_id']=4
store['num_workers']=40
store['config']={'seed': 1238, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0615382194519043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4197230339050293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.558882713317871})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9552721977233887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9500293731689453})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6985, 'crossentropy': 2.21062734375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 51137], ['id', 4727], ['id', 30359], ['id', 50981], ['id', 26901]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2532070666008677, 2.344022540705738, 3.1357416691508213, 3.6776900844955716, 4.038486486018585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.1144652366638184})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.369246244430542})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4054183959960938})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.7427163124084473})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.5662143230438232})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9777603149414062})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.311372756958008})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.2902495861053467})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7313, 'crossentropy': 2.0289619140625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 17540], ['id', 32531], ['id', 3118], ['id', 57242], ['id', 3880]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.3376109237957667, 2.4553141027524443, 3.278210391630509, 3.8559487731047266, 4.198255283273303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8864036798477173})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.5543251037597656})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.2808032035827637})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.5982327461242676})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.8777573108673096})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 3.0306894779205322})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7075, 'crossentropy': 2.2451296875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 11911], ['id', 49642], ['id', 5728], ['id', 12202], ['id', 42697]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2324625992332718, 2.2543981400622575, 3.1178534937959084, 3.705674093278269, 4.060402699639072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.9315747022628784})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.435925006866455})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.4017913341522217})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.405916690826416})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.610661029815674})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 3.147434949874878})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7352, 'crossentropy': 2.1435046875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 12035], ['id', 37313], ['id', 36826], ['id', 58560], ['id', 19942]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2293496902562424, 2.3402392359133697, 3.198045915537998, 3.7910044415014648, 4.153456618284954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4204928874969482})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.8966166973114014})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.058727264404297})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.0137405395507812})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.0281872749328613})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.9199923276901245})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 2.220125675201416})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.6292383670806885})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.8481321334838867})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.329911708831787})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7797, 'crossentropy': 1.8808658203125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 22269], ['id', 4935], ['id', 56695], ['id', 27440], ['id', 37770]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.2406199592093325, 2.3491875666807376, 3.25842111832581, 3.881876643899151, 4.256578572662459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4420814514160156})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.749617099761963})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.5951571464538574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.8843947649002075})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.9727210998535156})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.9958858489990234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.9225902557373047})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7801, 'crossentropy': 1.734955078125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 14484], ['id', 42784], ['id', 59280], ['id', 46163], ['id', 29803]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.2773433743491562, 2.3806951333637727, 3.1963894948499494, 3.7808354601125913, 4.141528933302785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.3006497621536255})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.5220744609832764})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.9248638153076172})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.6304301023483276})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.9190564155578613})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.8422234058380127})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.17494535446167})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.0169055461883545})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.9448487758636475})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7828, 'crossentropy': 1.855090234375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 21650], ['id', 39016], ['id', 22493], ['id', 50546], ['id', 24533]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2453283140109175, 2.321347144434809, 3.2082693517696246, 3.796660752683785, 4.160683444202354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.087581992149353})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.4604403972625732})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.5218361616134644})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7419747114181519})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.7912991046905518})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.923954725265503})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8378608226776123})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.732431173324585})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8075, 'crossentropy': 1.545404296875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 47479], ['id', 28226], ['id', 16994], ['id', 26742], ['id', 34188]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2533957623638416, 2.340850894047752, 3.1732424378903765, 3.777586552736248, 4.1350844752861615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0388102531433105})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3067686557769775})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1617975234985352})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2804036140441895})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.2837276458740234})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.308593988418579})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 1.08091240234375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 2765], ['id', 12196], ['id', 40905], ['id', 33331], ['id', 1239]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2229497817882058, 2.246379615723302, 3.0963085755423485, 3.692469506949485, 4.0870910631223385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.076854944229126})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1221493482589722})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3378543853759766})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.514303207397461})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3771631717681885})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8258, 'crossentropy': 1.0798435546875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 31847], ['id', 49890], ['id', 56049], ['id', 41714], ['id', 36256]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.134902863896016, 2.034979244294437, 2.8109452466555016, 3.406160146817978, 3.8308658965719173]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1153409481048584})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2939172983169556})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.409191608428955})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2863166332244873})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2890934944152832})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.3995559215545654})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.5483505725860596})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6155165433883667})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8296, 'crossentropy': 1.18858408203125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 5474], ['id', 27473], ['id', 43796], ['id', 20569], ['id', 4799]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1247855944525418, 2.1241286679908185, 2.9768404844533203, 3.576710633783387, 3.9864436646249475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.1487810611724854})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2987277507781982})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4162781238555908})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3505465984344482})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4247198104858398})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5742943286895752})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6977543830871582})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8265, 'crossentropy': 1.23094189453125}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 25662], ['id', 19298], ['id', 9118], ['id', 25823], ['id', 134]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1175796668420062, 2.0975912966092447, 2.891459726914034, 3.492696959599181, 3.9135435174895923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1411211490631104})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1681160926818848})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4706883430480957})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.5423381328582764})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4530727863311768})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.6237468719482422})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.66725754737854})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.6042072772979736})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8143, 'crossentropy': 1.4006619140625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 14649], ['id', 9713], ['id', 39899], ['id', 22550], ['id', 5013]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0970913565958205, 2.131872237757009, 3.023964662870478, 3.6547267337291913, 4.050762243115647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1466076374053955})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1894562244415283})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.5015292167663574})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.3479270935058594})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.2604413032531738})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.395477294921875})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.44949471950531})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.5095340013504028})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8458, 'crossentropy': 1.12451962890625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 39135], ['id', 21880], ['id', 1364], ['id', 51764], ['id', 49607]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1608292132816982, 2.1737666216010822, 3.020296537575595, 3.656059167155509, 4.061750755955204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0561833381652832})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0113184452056885})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9637661576271057})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.116551399230957})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.01566743850708})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1162493228912354})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9925757646560669})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1566400527954102})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2067275047302246})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2459335327148438})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8692, 'crossentropy': 0.95951904296875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 53872], ['id', 14655], ['id', 41108], ['id', 9472], ['id', 32521]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1577254838219915, 2.2280035544865795, 3.0876958286318494, 3.7062118371748474, 4.093276323204829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1343224048614502})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9253618717193604})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1150137186050415})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0597624778747559})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0657215118408203})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2138214111328125})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1699556112289429})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2298705577850342})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2066998481750488})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3107404708862305})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8579, 'crossentropy': 1.08703603515625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 14765], ['id', 53873], ['id', 34678], ['id', 35397], ['id', 31699]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1790645467487564, 2.2733495904061654, 3.179428250297141, 3.825475209248266, 4.204100751416588]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2628350257873535})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0715270042419434})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1784907579421997})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.3629131317138672})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.196996808052063})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3520883321762085})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2873733043670654})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.309411644935608})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8515, 'crossentropy': 1.0179068359375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 36998], ['id', 31014], ['id', 4784], ['id', 48046], ['id', 32880]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1610687407241236, 2.1737570610104546, 2.9762074810103467, 3.6082025878610526, 4.026704169545962]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1552395820617676})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.943506121635437})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1164822578430176})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2094625234603882})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2595701217651367})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1629769802093506})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3822920322418213})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.345033884048462})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2687973976135254})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1918542385101318})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.3511457443237305})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4359458684921265})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.4437534809112549})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2811914682388306})
store['active_learning_steps'][17]['training']['best_epoch']=11
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8606, 'crossentropy': 1.24141904296875}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 47626], ['id', 53854], ['id', 53019], ['id', 1674], ['id', 40576]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2786950631527116, 2.4338539214708375, 3.3103345685905357, 3.8909322669439357, 4.241547138376593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.2849090099334717})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9991526007652283})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0345895290374756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0494847297668457})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1982595920562744})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3168690204620361})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8534, 'crossentropy': 0.94739365234375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 11208], ['id', 28512], ['id', 27687], ['id', 12767], ['id', 59747]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9687400126339605, 1.7760467271995273, 2.494163278114881, 3.1014627587070347, 3.558418641374093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2067780494689941})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9152259826660156})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9556031227111816})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0562002658843994})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1470277309417725})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9595034122467041})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1895982027053833})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1475813388824463})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.2573620080947876})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.4350731372833252})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.3133859634399414})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.4044240713119507})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8738, 'crossentropy': 1.076841796875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 59344], ['id', 10038], ['id', 2795], ['id', 25508], ['id', 49910]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.1894834444997486, 2.2384513283843255, 3.1042952678880793, 3.733579200815937, 4.119359393076756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2412055730819702})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9602970480918884})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9681742191314697})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0386618375778198})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9193065166473389})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.102298617362976})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1472604274749756})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0849635601043701})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8753, 'crossentropy': 0.8980833984375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 33812], ['id', 29476], ['id', 18398], ['id', 45801], ['id', 52149]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.0946895558723853, 2.085053053540911, 2.902611968250083, 3.5228677822226873, 3.9359294289056406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1681129932403564})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9543247818946838})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.037684679031372})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0353518724441528})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9730018973350525})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1724755764007568})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1666555404663086})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.2304998636245728})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.87, 'crossentropy': 0.926453515625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 3762], ['id', 52785], ['id', 19590], ['id', 33505], ['id', 51464]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0630318760022162, 2.052787662804885, 2.880086854825338, 3.5166730282227032, 3.9433947790662245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1731395721435547})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8995053768157959})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8537071347236633})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9945090413093567})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.124377965927124})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0206365585327148})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1329946517944336})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0338757038116455})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.3632705211639404})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8743, 'crossentropy': 0.94607666015625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 8704], ['id', 29591], ['id', 32276], ['id', 44342], ['id', 36818]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.110292199405169, 2.1137549232402297, 2.99292362681154, 3.602973650992622, 4.013336221495778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0783181190490723})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.855033278465271})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8719995021820068})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0553854703903198})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0390714406967163})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9844187498092651})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0637447834014893})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0547325611114502})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0865728855133057})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8829, 'crossentropy': 0.92035703125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 48102], ['id', 26693], ['id', 5430], ['id', 17222], ['id', 13997]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.153263183525058, 2.1718415711141628, 2.9945848169359977, 3.617714981684559, 4.029833417324998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1313858032226562})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7230682373046875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7383891344070435})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.745092511177063})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7044751644134521})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7496227622032166})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.766998291015625})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7517681121826172})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.67586669921875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 11708], ['id', 15781], ['id', 14760], ['id', 47870], ['id', 23468]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.05385767304584, 2.0357626814174496, 2.8607218576074995, 3.457317391667484, 3.881115244497127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0391594171524048})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7877252101898193})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7345975041389465})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7614932656288147})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8592668771743774})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8246859312057495})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8913452625274658})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9671322703361511})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8693397045135498})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9598608016967773})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0710244178771973})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.1915826797485352})
store['active_learning_steps'][25]['training']['best_epoch']=9
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.737510205078125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 48360], ['id', 20120], ['id', 37538], ['id', 52169], ['id', 3810]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1594464588028046, 2.1871329341603243, 3.06697686766089, 3.672021457769649, 4.070463068512023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1132323741912842})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7673531770706177})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7244923710823059})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6821895837783813})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7410300970077515})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8002522587776184})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9288343191146851})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8819297552108765})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8226833343505859})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.70372890625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 49824], ['id', 50297], ['id', 24740], ['id', 43745], ['id', 21436]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1542098555232463, 2.156900786249068, 2.99414553143646, 3.6114701405446574, 4.027167143696948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.209060549736023})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7588262557983398})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.811713695526123})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.797700047492981})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8652716875076294})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9100744128227234})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8657779693603516})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8482412695884705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9526869654655457})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9151721000671387})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.761545361328125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 45944], ['id', 4741], ['id', 56572], ['id', 17808], ['id', 44123]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0695777402524527, 2.019533717575807, 2.8490644559739557, 3.493992500759963, 3.9305557664740025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.2951940298080444})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7280657291412354})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6486611366271973})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6517472267150879})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.743607223033905})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6529433727264404})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.641291081905365})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7025167346000671})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7310699820518494})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.762175440788269})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.693515419960022})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7442792654037476})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7320393323898315})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8575860261917114})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7568874359130859})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7927332520484924})
store['active_learning_steps'][28]['training']['best_epoch']=13
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.693144921875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 17478], ['id', 21174], ['id', 3691], ['id', 55190], ['id', 20641]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1243581054332679, 2.1705157808399096, 3.064383539553053, 3.7230478116057037, 4.143757378885754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2007255554199219})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7882124185562134})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6730763912200928})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5571920871734619})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7217139005661011})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5768262147903442})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6156108379364014})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6689621210098267})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7555748224258423})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9267, 'crossentropy': 0.526203076171875}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 45246], ['id', 5536], ['id', 50431], ['id', 670], ['id', 42112]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9857208778270634, 1.8929641364591956, 2.6951245804015933, 3.333804527557813, 3.794374968446638]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.145071029663086})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6279988884925842})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6086677312850952})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.570179283618927})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5948721170425415})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5620041489601135})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7252088785171509})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6679229736328125})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6801661252975464})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.545776708984375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 59294], ['id', 50320], ['id', 13752], ['id', 30692], ['id', 43176]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0909675460837325, 2.068084812191479, 2.895522590189329, 3.508327505304522, 3.9372845730062505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2233312129974365})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7432074546813965})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.59278404712677})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5748089551925659})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5576446056365967})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5580465793609619})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6156777143478394})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5932491421699524})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9308, 'crossentropy': 0.545750732421875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 36008], ['id', 6050], ['id', 1295], ['id', 38061], ['id', 17741]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0097037037437262, 1.9448030423452565, 2.7717949344016226, 3.4150268782569864, 3.8637586623518896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2433632612228394})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6859950423240662})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6592400074005127})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5816787481307983})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6452943682670593})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5909092426300049})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5594614744186401})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6545273065567017})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6570600271224976})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7217011451721191})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.53963544921875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 22139], ['id', 37469], ['id', 30883], ['id', 57972], ['id', 2381]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.0243448498550167, 1.9856339975168642, 2.835196505238631, 3.478938435823352, 3.935694993284372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3327360153198242})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7622991800308228})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6244519352912903})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6208024024963379})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.615019679069519})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6028428077697754})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5943169593811035})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5880985260009766})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6167438626289368})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6644580364227295})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6723140478134155})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7115339040756226})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9268, 'crossentropy': 0.588551171875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 54195], ['id', 12450], ['id', 47595], ['id', 36408], ['id', 3941]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.156368233836391, 2.1701054805001583, 3.030162808821262, 3.6307934829128072, 4.03981299800073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2729806900024414})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6427435874938965})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5635731220245361})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5094999074935913})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5276219844818115})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.570632815361023})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48560935258865356})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.483177125453949})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5108824968338013})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5414052605628967})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5983707308769226})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5309317111968994})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5807597637176514})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.498515966796875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 57319], ['id', 41133], ['id', 51337], ['id', 57728], ['id', 31114]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1617205679064442, 2.2110853690772245, 3.112273392141354, 3.737418246145296, 4.1114963543613765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3947887420654297})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.628813624382019})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.527624785900116})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5056624412536621})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5746468901634216})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5783477425575256})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.545455224609375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 43224], ['id', 1075], ['id', 49525], ['id', 30897], ['ood', 47647]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8668303070344112, 1.6336222607569155, 2.3166851797405617, 2.901560711864847, 3.3608303132294495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4093477725982666})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6490368843078613})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5532557368278503})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4800480604171753})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5051788687705994})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45713239908218384})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47127214074134827})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49696069955825806})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5233427882194519})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.456972412109375}
