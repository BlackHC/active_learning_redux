store = {}
store['timestamp']=1622152852
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=16']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=40
store['config']={'seed': 1252, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.370654582977295})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.535623550415039})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.824517250061035})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.7592058181762695})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7786431312561035})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.746349811553955})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.290935754776001})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7003, 'crossentropy': 2.5085015625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1028978824615479})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0970370769500732})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.107680320739746})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1258139610290527})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 35151], ['id', 29751], ['id', 50825], ['id', 29472], ['ood', 3468]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.2652845280340772, 2.153773611945921, 2.772401379284692, 3.14932782003752, 3.357259331609578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.934234857559204})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.05507230758667})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.6048126220703125})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.515775203704834})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.468559980392456})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7086, 'crossentropy': 1.7709037109375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1084742546081543})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0967007875442505})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1105523109436035})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0644938945770264})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 36721], ['id', 59974], ['id', 21276], ['id', 21990], ['id', 21013]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8623025302747718, 1.5828994935138923, 2.1629577642244744, 2.5914883391047123, 2.8515482973966932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.681965708732605})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.9629900455474854})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0714235305786133})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.2330269813537598})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.370945692062378})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7318, 'crossentropy': 1.6820390625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0328571796417236})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0031746625900269})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0295393466949463})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.9522756338119507})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 35139], ['id', 26834], ['id', 12196], ['id', 29422], ['id', 6666]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9305516056683873, 1.6609676300756853, 2.233159111494496, 2.6071127549938957, 2.837731826248394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7266242504119873})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.1664857864379883})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.12642240524292})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.225597381591797})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.523196220397949})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4653520584106445})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.531031608581543})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.726, 'crossentropy': 2.2284640625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.0425093173980713})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.058410406112671})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.0574997663497925})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0631732940673828})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 43041], ['id', 6352], ['id', 17925], ['id', 52725], ['id', 25783]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8696932078524482, 1.5780543592555163, 2.1480848641949652, 2.5331611271712458, 2.7586385810524803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6125826835632324})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.7600891590118408})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.0938479900360107})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.028791904449463})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.833803415298462})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 2.2595736980438232})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 2.1179213523864746})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 2.076261043548584})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 2.0526485443115234})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.1383252143859863})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 2.0350148677825928})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.246626377105713})
store['active_learning_steps'][4]['training']['best_epoch']=9
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7907, 'crossentropy': 1.66300078125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.8121000528335571})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8360472917556763})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8080934882164001})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8317189812660217})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8201698064804077})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.7998306155204773})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 28313], ['id', 48811], ['id', 56852], ['ood', 45822], ['id', 12907]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0763872075984275, 1.9601670519117205, 2.6136243557541103, 2.9217895283521758, 3.0750893188287147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.5506811141967773})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.6797585487365723})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.013392686843872})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9446308612823486})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2602367401123047})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7632, 'crossentropy': 1.45796259765625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9766117334365845})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9043892621994019})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9582359790802002})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.938560962677002})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 34974], ['id', 35652], ['id', 55591], ['id', 43165], ['id', 27406]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8466518407727239, 1.5130682538221012, 2.049544217118293, 2.4343640941844633, 2.63226389874362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1084742546081543})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3502047061920166})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4597302675247192})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.4613609313964844})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3571873903274536})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5127454996109009})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6280282735824585})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.6279778480529785})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.814785122871399})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8284, 'crossentropy': 1.250897265625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.786882758140564})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7329258918762207})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.7273792624473572})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.6829706430435181})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.7429908514022827})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.6855546236038208})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.67142653465271})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.6735312938690186})
store['active_learning_steps'][6]['eval_training']['best_epoch']=8
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 3584], ['id', 11269], ['id', 16467], ['id', 50871], ['id', 26022]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0495838620263604, 1.8617952451245379, 2.46917345784947, 2.857805742168347, 3.0909694688565796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2602064609527588})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.3520135879516602})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.4686126708984375})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.434828758239746})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.703355312347412})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.6718475818634033})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.6197535991668701})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.7893791198730469})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.7390385866165161})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.7285723686218262})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 2.033562660217285})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.8420186042785645})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.9168949127197266})
store['active_learning_steps'][7]['training']['best_epoch']=10
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8347, 'crossentropy': 1.43238486328125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8067245483398438})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7523582577705383})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.710175633430481})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.6791372299194336})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.728135347366333})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.6636476516723633})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.696135401725769})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.6828691959381104})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.6672248840332031})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.6665652990341187})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.6521297097206116})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.64478600025177})
store['active_learning_steps'][7]['eval_training']['best_epoch']=12
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 59833], ['id', 13548], ['id', 16706], ['id', 5600], ['id', 59335]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9939579625937285, 1.877667046554449, 2.5002128152349368, 2.908199796588013, 3.1088558857205353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2862999439239502})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3076647520065308})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3914368152618408})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4880719184875488})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7736566066741943})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.694785237312317})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8315, 'crossentropy': 1.1302568359375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8570656776428223})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.7549581527709961})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.7396950721740723})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7171770930290222})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7178792953491211})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 28256], ['id', 47214], ['id', 42654], ['id', 49010], ['id', 27316]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8296979495370695, 1.5499803130793994, 2.137247292446088, 2.534063406911046, 2.760210458675475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9800525307655334})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0643248558044434})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0409727096557617})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.035773754119873})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1740379333496094})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.873, 'crossentropy': 0.798852099609375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7689203023910522})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6923463344573975})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6623477339744568})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6622205972671509})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 13181], ['id', 32794], ['id', 31588], ['id', 2554], ['id', 46187]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7540737482479538, 1.3944326475203308, 1.8957385317200677, 2.240522305239825, 2.4761109112644686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.888213038444519})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9022175669670105})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9483150243759155})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9703421592712402})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1479861736297607})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8829, 'crossentropy': 0.715971875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7409943342208862})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6451581716537476})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6319847106933594})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.5964717864990234})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 50370], ['id', 39841], ['id', 32065], ['id', 49064], ['id', 58655]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7364450333427066, 1.400211838076736, 1.9278674811498275, 2.299649156923567, 2.542818878839565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8423280715942383})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8664700388908386})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9202355742454529})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.97959303855896})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0227360725402832})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0138543844223022})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9706015586853027})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8865, 'crossentropy': 0.7839955078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6692594289779663})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5725088119506836})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5677238702774048})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5414283275604248})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5383715629577637})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.49439775943756104})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 6650], ['id', 14514], ['id', 54814], ['id', 3580], ['id', 58430]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8081301845418072, 1.5135822797942406, 2.0784455584920316, 2.4526834620000795, 2.6876882545627314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.854724645614624})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7541742324829102})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7834628820419312})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8090394735336304})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9227678775787354})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8738818168640137})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9364535808563232})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.643875048828125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6796878576278687})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5684612393379211})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5420070290565491})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.48625195026397705})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.469470739364624})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.46842160820961})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 49893], ['id', 41299], ['id', 37794], ['id', 51127], ['ood', 59616]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9326849858761044, 1.6592653518288087, 2.2366062732041625, 2.5876266969610313, 2.7809182256324876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9379594326019287})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.79004967212677})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9018068313598633})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8577579259872437})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0980286598205566})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9986245632171631})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9972757697105408})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8919, 'crossentropy': 0.73391748046875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7664085626602173})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6020317077636719})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5447618961334229})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5508319139480591})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5287272930145264})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5149851441383362})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 9665], ['id', 5707], ['id', 109], ['id', 37363], ['id', 42828]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8153569224440265, 1.4837335987088047, 2.0209798549846205, 2.387824013214294, 2.6015329688631397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8336577415466309})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7063595056533813})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7130032777786255})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7285517454147339})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.870934247970581})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9396219849586487})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9710814952850342})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8936, 'crossentropy': 0.655244140625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.6908607482910156})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5522928237915039})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4830690324306488})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.48403528332710266})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.4804372191429138})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.4772297739982605})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 274], ['id', 49172], ['id', 22169], ['id', 38080], ['id', 22503]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7764287293445264, 1.4325152146216906, 1.9770200231891524, 2.35606242338942, 2.594527015211904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.766663670539856})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6980597376823425})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7128852605819702})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7519580125808716})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7481824159622192})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7832865715026855})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7996679544448853})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8497976064682007})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8113669157028198})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7993059158325195})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.666873828125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6040179133415222})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5170443058013916})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.45804333686828613})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.45685434341430664})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4503096342086792})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 22272], ['id', 7891], ['ood', 55043], ['id', 23038], ['id', 43014]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.813484670064321, 1.550844030827831, 2.0774479419651666, 2.4420791819643526, 2.6528187159155916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8327344655990601})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7135928869247437})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7011491060256958})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.723706841468811})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7606269717216492})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.79994797706604})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.6169943359375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6890119314193726})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5797809362411499})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5067271590232849})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.46947357058525085})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4817935824394226})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 19951], ['id', 57474], ['id', 48818], ['id', 22269], ['id', 11208]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.736238349298663, 1.3556162502626452, 1.8558789306222163, 2.2309359663767045, 2.4822569141127673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7424032688140869})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6010835766792297})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5734597444534302})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.637427031993866})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7028161883354187})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7174516320228577})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.4872048828125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6449437141418457})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5865368843078613})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5002619624137878})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.49330392479896545})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4512065052986145})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 42951], ['id', 33222], ['id', 44095], ['id', 39031], ['id', 36732]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6731380122899357, 1.260130942552332, 1.7243541721614548, 2.0770265774527745, 2.3192183439993777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8680139780044556})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5602209568023682})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5399059653282166})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6166273951530457})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5995628833770752})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.5269580078125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6779012084007263})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5695884227752686})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5479367971420288})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.47519195079803467})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 43648], ['id', 12497], ['id', 7833], ['id', 42746], ['id', 43560]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6497515229567177, 1.203709863566583, 1.6456237346504636, 1.9612025465814469, 2.183386878073776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8558092713356018})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6480878591537476})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6752451658248901})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7198575735092163})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6703152656555176})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.605485205078125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7859877347946167})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6492934226989746})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5761419534683228})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5826615691184998})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 58394], ['id', 43711], ['id', 14749], ['id', 57985], ['id', 36442]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6202191959574017, 1.1721511974325303, 1.659614004452779, 2.026342875610313, 2.2801678728013517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0106902122497559})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.603961169719696})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6523139476776123})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.594916582107544})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6078542470932007})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.678854763507843})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.679712176322937})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7592558264732361})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.576366552734375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6339760422706604})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5234131813049316})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.43739205598831177})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.46094852685928345})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.46265846490859985})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.42132365703582764})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 13428], ['id', 56838], ['id', 19086], ['id', 14735], ['id', 34294]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7147117475925542, 1.3332968988104978, 1.8574039910405986, 2.256074870450705, 2.512486792278649]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8775287866592407})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6386042833328247})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6344385743141174})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6754487752914429})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6803903579711914})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7260541915893555})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7608680725097656})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8043911457061768})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9168, 'crossentropy': 0.55288046875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6618742942810059})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4867364168167114})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.48115378618240356})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.460082083940506})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4440193772315979})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4083263576030731})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4171537160873413})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 4066], ['id', 52959], ['id', 15332], ['id', 26434], ['id', 30932]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7692071933584632, 1.462114140358255, 1.9936473385916678, 2.3962470151691972, 2.6379100142304575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.014545202255249})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6937830448150635})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6267186403274536})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.695067286491394})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6711134910583496})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7063627243041992})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.909491777420044})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8024439811706543})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.531852001953125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6810297966003418})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5118743181228638})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45111072063446045})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4260002374649048})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.44937044382095337})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.44809553027153015})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4152769148349762})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 33812], ['id', 11708], ['id', 7768], ['id', 53196], ['id', 3251]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7526712030454925, 1.4246908934545601, 1.9574864482134107, 2.29059262191595, 2.482933619072371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.051161766052246})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7148181200027466})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6507629752159119})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6828862428665161})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7688494324684143})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7340459823608398})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7131893634796143})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7321908473968506})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8716782331466675})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8648694753646851})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9236, 'crossentropy': 0.58518115234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6091639995574951})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.47241243720054626})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4215417802333832})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4199122190475464})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.42068102955818176})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4074253439903259})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.37025976181030273})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.3982973098754883})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.40388721227645874})
store['active_learning_steps'][23]['eval_training']['best_epoch']=9
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 10925], ['id', 2431], ['id', 42078], ['id', 15266], ['id', 53844]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8296882670450474, 1.6005959521009627, 2.239511615285278, 2.6478839363343765, 2.9117266059311753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9987351894378662})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6280896067619324})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5542430877685547})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5865911245346069})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6615172624588013})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.663496732711792})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.51435166015625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7015902996063232})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5117861032485962})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.47643372416496277})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4573213458061218})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4496570825576782})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 52971], ['id', 2426], ['id', 53998], ['id', 42243], ['id', 24819]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6938262158615145, 1.2767492159327114, 1.7737973134780214, 2.146448857272091, 2.4256127838853327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.905522882938385})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5657435059547424})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5376931428909302})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5439738035202026})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5268332362174988})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5640900135040283})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6697177886962891})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5944894552230835})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6246390342712402})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9446, 'crossentropy': 0.418720947265625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5849790573120117})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4512236714363098})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4146437644958496})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3596258759498596})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36129045486450195})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35157814621925354})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3481549620628357})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 25634], ['id', 45424], ['id', 32173], ['id', 49834], ['id', 35326]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6934945643375074, 1.3298138135626134, 1.8611761638837603, 2.240340101687888, 2.494153482503968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8132283687591553})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5170103311538696})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.504590630531311})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5531156063079834})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5245687961578369})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5168296694755554})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5477725267410278})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6364716291427612})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6105954647064209})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9406, 'crossentropy': 0.436228857421875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7045832872390747})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4569338262081146})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.42407166957855225})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.394813597202301})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.344819575548172})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.36514413356781006})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3356117010116577})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.33546626567840576})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 34524], ['id', 10992], ['id', 49276], ['id', 31102], ['id', 26090]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7585275827430851, 1.387276644290378, 1.9122337574887434, 2.307869372396252, 2.580351070595867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9270983934402466})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.524605929851532})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43843159079551697})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5262691974639893})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.470234751701355})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5060673952102661})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.415947900390625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6528436541557312})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4842514395713806})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4663107991218567})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.455328106880188})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.39189815521240234})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 5474], ['id', 30884], ['id', 4646], ['id', 38315], ['id', 3941]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6136207565254137, 1.138763724581076, 1.5956076603240286, 1.9398308853490445, 2.183769486252846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0548419952392578})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5633394122123718})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48444539308547974})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4700234532356262})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47359874844551086})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4854542315006256})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4712042808532715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4854780435562134})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5109086036682129})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5140057802200317})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9539, 'crossentropy': 0.3811735107421875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5966486930847168})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.47056421637535095})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.409736692905426})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3785836696624756})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3707401752471924})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3382338285446167})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.33434075117111206})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.36097145080566406})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3573070764541626})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 5315], ['id', 39208], ['id', 39877], ['id', 41433], ['id', 9552]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9023661048870342, 1.6804834510851019, 2.2813541536546884, 2.658944202009346, 2.877570085975502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0439300537109375})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5084725022315979})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5382891893386841})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.487424373626709})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46477508544921875})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5267430543899536})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4668106436729431})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5536131858825684})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5178464651107788})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5153343677520752})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.4068373779296875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5787597298622131})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4188215136528015})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.39237838983535767})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3957723081111908})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3464307188987732})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.31971216201782227})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3236233592033386})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.29018348455429077})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3365013599395752})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 13153], ['id', 20641], ['id', 33088], ['id', 34665], ['id', 38524]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8086615436036169, 1.5209295356696186, 2.0931274010523446, 2.5380388339189155, 2.8147356320406427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.160722017288208})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5807603001594543})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49176329374313354})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4604376554489136})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4328082799911499})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4716588258743286})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4967847466468811})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48831769824028015})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9474, 'crossentropy': 0.39400595703125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6271624565124512})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46298134326934814})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4219970703125})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3987455368041992})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37484031915664673})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.36734074354171753})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36828601360321045})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 28420], ['id', 42121], ['id', 58832], ['id', 51650], ['id', 25520]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.776784422073985, 1.4401925278721754, 1.9683390288930598, 2.3334222179281348, 2.5900718418390865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9974453449249268})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5378457903862})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43309545516967773})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42918169498443604})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4640710651874542})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4960659146308899})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9463, 'crossentropy': 0.4066074951171875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6094790697097778})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.46853503584861755})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3989836573600769})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40955138206481934})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.39647531509399414})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 27644], ['id', 10028], ['id', 29335], ['id', 8771], ['id', 53441]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6883304003565329, 1.285251168129216, 1.8099500845627476, 2.178704682482052, 2.4163415099889685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.06827712059021})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5443918704986572})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43672484159469604})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4041665196418762})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4785073399543762})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4344944357872009})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4267047643661499})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4456900358200073})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42736878991127014})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44073933362960815})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9498, 'crossentropy': 0.39893603515625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5956417322158813})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.441913366317749})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3976607918739319})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37495777010917664})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35654184222221375})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3370610475540161})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3236311674118042})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3268786072731018})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3084052503108978})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 52697], ['id', 2034], ['id', 6582], ['id', 7207], ['id', 33581]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7450772953507843, 1.4477346975067977, 2.042189939861757, 2.436330955621499, 2.649289922147436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1353214979171753})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6000688076019287})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49051207304000854})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.477399080991745})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4462874233722687})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46386024355888367})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4602992832660675})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44933420419692993})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4409463405609131})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4863624572753906})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49293071031570435})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4823262393474579})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5155508518218994})
store['active_learning_steps'][33]['training']['best_epoch']=10
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9505, 'crossentropy': 0.4142654296875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6343015432357788})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42290645837783813})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37220513820648193})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3752133250236511})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.32375138998031616})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.34982746839523315})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3226950168609619})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.32421863079071045})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 32784], ['id', 8680], ['id', 34122], ['id', 7840], ['id', 13604]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8074364918773311, 1.515091913099424, 2.0713820083782775, 2.429607443265555, 2.6225519943713618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8919569253921509})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.495651513338089})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42993998527526855})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3677014410495758})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3994535505771637})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4201221764087677})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3980199098587036})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.361758984375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6550921201705933})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4634242057800293})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41471222043037415})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3980676829814911})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39827942848205566})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37049782276153564})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 29530], ['id', 53979], ['id', 2803], ['id', 49593], ['id', 23690]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6623542220641374, 1.2610619808583778, 1.76484351969812, 2.1641001613389346, 2.4514275732074804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0386838912963867})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5198907852172852})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46676987409591675})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4119815528392792})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4128769040107727})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41204750537872314})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4753764867782593})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.366704931640625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6262123584747314})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4475412368774414})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40015119314193726})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39253515005111694})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.36612868309020996})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3593241572380066})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 34819], ['id', 27024], ['id', 31301], ['id', 12392], ['id', 33656]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6849124152235828, 1.267261143511785, 1.750086654203736, 2.116844047652963, 2.376794317673351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2345492839813232})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5721254348754883})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4221290349960327})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44913485646247864})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4248226284980774})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4284045696258545})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43127137422561646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47837141156196594})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4327425956726074})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4633535146713257})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9535, 'crossentropy': 0.3750903564453125}
