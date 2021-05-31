store = {}
store['timestamp']=1622148026
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=0']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=40
store['config']={'seed': 1234, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.173092842102051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.454342842102051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.655754566192627})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6076624393463135})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.6232247352600098})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.793619155883789})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.1201162338256836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.905629873275757})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7043, 'crossentropy': 2.4752515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1635191440582275})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.070251226425171})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1305381059646606})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1087288856506348})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0840644836425781})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 1981], ['id', 31030], ['id', 5409], ['id', 14887], ['id', 17291]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.131468729014601, 1.9451221562656382, 2.5832216411071185, 2.98909903397647, 3.1895401135446066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9199612140655518})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.1167776584625244})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.422184467315674})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.4238390922546387})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.65785551071167})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.771810531616211})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.7638392448425293})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7214, 'crossentropy': 2.1502697265625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0456581115722656})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0641977787017822})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9668396711349487})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0589442253112793})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0161315202713013})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0406527519226074})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 51265], ['id', 38147], ['id', 42053], ['id', 31847], ['id', 48170]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.094782084865989, 1.9564139049419902, 2.55532094372869, 2.955458125377123, 3.179834084613951]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7011306285858154})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.7775607109069824})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.258031129837036})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.3623342514038086})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.326615333557129})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7659, 'crossentropy': 1.6284078125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.0247032642364502})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9711888432502747})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9372280836105347})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9078541994094849})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 17972], ['id', 29300], ['id', 3720], ['ood', 50389], ['id', 3362]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9923551597537632, 1.8144575437677455, 2.4109693781366897, 2.8508918010917066, 3.110811535838124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3150718212127686})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.6993238925933838})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.7819972038269043})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.9157345294952393})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.0702872276306152})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7729, 'crossentropy': 1.48074140625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0164756774902344})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9807277917861938})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.9521230459213257})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9445905685424805})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 41782], ['id', 15116], ['id', 48145], ['id', 40523], ['id', 28693]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8252079086219215, 1.5512390631906343, 2.119398445824948, 2.516898929818873, 2.762360668816595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1784353256225586})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.310058832168579})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.359074592590332})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.4515948295593262})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4936349391937256})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.488504409790039})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8171, 'crossentropy': 1.28361298828125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9000158309936523})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8006949424743652})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.7850319147109985})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.7606974840164185})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.761298418045044})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 52953], ['id', 52012], ['id', 11964], ['id', 38122], ['id', 34041]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8002410156843458, 1.5483554188401505, 2.111126454381769, 2.5278797577388206, 2.772650073448874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.287556767463684})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4398071765899658})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.6079180240631104})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.5457481145858765})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.7444744110107422})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8151, 'crossentropy': 1.20281171875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.9027332067489624})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8207360506057739})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.7762442827224731})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.7685787081718445})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 36767], ['id', 54885], ['id', 52886], ['id', 29381], ['ood', 5905]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8949367307636664, 1.5615885372534204, 2.1016615379668515, 2.475775459660772, 2.710792000238232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0328130722045898})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.082977294921875})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.179492712020874})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.4067888259887695})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.3722813129425049})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.278095006942749})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8347, 'crossentropy': 1.094119140625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8210451006889343})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.7357780337333679})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7426322102546692})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7199741005897522})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.6785005331039429})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 15502], ['id', 7160], ['id', 49140], ['id', 38980], ['id', 20925]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.813262103760243, 1.5564395169797898, 2.153622558749473, 2.5214351981288052, 2.726039417644074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9557517170906067})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0745314359664917})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.088719367980957})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.150194525718689})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1328189373016357})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3052083253860474})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3814140558242798})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3784420490264893})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2755205631256104})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3885180950164795})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.4180772304534912})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3720407485961914})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.4317772388458252})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4857591390609741})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.6004977226257324})
store['active_learning_steps'][7]['training']['best_epoch']=12
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8481, 'crossentropy': 1.20604208984375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7624063491821289})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6585609912872314})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6500723361968994})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.6220299005508423})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6080389618873596})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6199256181716919})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 9081], ['id', 44753], ['id', 59297], ['id', 30016], ['ood', 1201]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.997166760418313, 1.8056455604336574, 2.465267943836868, 2.843030721395202, 3.0185546931046883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0648510456085205})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9505394697189331})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0341346263885498})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1727280616760254})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1890833377838135})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8444, 'crossentropy': 0.7929935546875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.7804502248764038})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7230428457260132})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.7142148613929749})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.6619234085083008})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 32065], ['id', 27703], ['id', 39573], ['id', 5085], ['id', 44881]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7448449014265301, 1.3532342863687092, 1.8642269128044155, 2.242479048880959, 2.503319465296814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9804481863975525})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0221318006515503})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.171895980834961})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.178727626800537})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2280772924423218})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2227730751037598})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2247729301452637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1542487144470215})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1581082344055176})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2790310382843018})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.402367353439331})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.330033302307129})
store['active_learning_steps'][9]['training']['best_epoch']=9
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8556, 'crossentropy': 1.03610966796875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7485805749893188})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.655982255935669})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6121921539306641})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6329872012138367})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.5831136107444763})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.5614736676216125})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.5743829011917114})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.54751056432724})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.5598732233047485})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.5863347053527832})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5613516569137573})
store['active_learning_steps'][9]['eval_training']['best_epoch']=8
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 43811], ['id', 201], ['id', 38275], ['id', 38193], ['id', 43696]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9940441147514862, 1.8388613302803822, 2.5145225525468247, 2.933281674605106, 3.135930501580299]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9513806104660034})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8962575197219849})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9631794691085815})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9608438611030579})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9942213296890259})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1493690013885498})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.875, 'crossentropy': 0.789644775390625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7158346176147461})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.6027377843856812})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.5882322788238525})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.5489504337310791})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.5373451113700867})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 54264], ['id', 29611], ['id', 32163], ['id', 39329], ['id', 20172]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7246125532254295, 1.381370633467807, 1.8967269114645147, 2.282361242259599, 2.5282921182792686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9638718962669373})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9104993343353271})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8756729364395142})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9622539281845093})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1090731620788574})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0933717489242554})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8828, 'crossentropy': 0.6986716796875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7470318078994751})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6570770740509033})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6015352010726929})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5712689161300659})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5924155712127686})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 2000], ['id', 15005], ['id', 34328], ['id', 2611], ['id', 58577]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7558349300156539, 1.4314941174562033, 1.9754288093774504, 2.3553630092028293, 2.6069378415510815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9674280285835266})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7710944414138794})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.825960636138916})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8688399791717529})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9606029987335205})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9753820896148682})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9499433636665344})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8831, 'crossentropy': 0.77617978515625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.66780686378479})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.5926531553268433})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5422374606132507})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5205687284469604})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5268502235412598})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5536263585090637})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22083], ['id', 37934], ['id', 49893], ['id', 55194], ['id', 56614]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9438512180467431, 1.7484898240749551, 2.3025129953420223, 2.6815643608592223, 2.8956781250386463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.840365469455719})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7957847118377686})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8045800924301147})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7606816291809082})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8510724306106567})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8781533241271973})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9119434356689453})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.679180712890625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6950470209121704})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5901480317115784})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5187956094741821})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.523413896560669})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5074897408485413})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.48755165934562683})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 26516], ['id', 49026], ['id', 47909], ['id', 30750], ['id', 51650]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7759730569816674, 1.4313934414422387, 1.991865817687211, 2.3824601233327263, 2.6150853739977986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8631128072738647})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6678231954574585})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7508925199508667})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7635374069213867})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8072220087051392})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7880105376243591})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8513877391815186})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8927888870239258})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.79164719581604})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9530687928199768})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 1.0116026401519775})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.905443549156189})
store['active_learning_steps'][14]['training']['best_epoch']=9
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9121, 'crossentropy': 0.685743212890625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6690268516540527})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.520933210849762})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4680842161178589})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.46180784702301025})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4491807222366333})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4571433365345001})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 37051], ['id', 59681], ['id', 15913], ['id', 56127], ['id', 21242]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8772638993248494, 1.6909228248216426, 2.314314481122289, 2.67185164843493, 2.8588745905965673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8708242774009705})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.717133641242981})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6937164068222046})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8142515420913696})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8416397571563721})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8701503872871399})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.60663857421875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6417407989501953})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5702073574066162})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.4911394715309143})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.48540735244750977})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.47905173897743225})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 51432], ['id', 44142], ['id', 13045], ['id', 54854], ['id', 16488]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7084188341614941, 1.3327121829484296, 1.8629977218293874, 2.2261970174405343, 2.458215492139357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9425992965698242})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7021061182022095})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.712821364402771})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7218700647354126})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6930681467056274})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8573843240737915})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7699577808380127})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8204193115234375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9149179458618164})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8424255847930908})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.65382890625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6509514451026917})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5696241855621338})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.472422331571579})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4493485689163208})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.44029366970062256})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4411107897758484})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4291098117828369})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.41227322816848755})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 9948], ['id', 29879], ['id', 39928], ['id', 4058], ['ood', 43952]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8410408534985465, 1.5970363871376954, 2.2111379426516287, 2.580215829140786, 2.7781878760392864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8698408603668213})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6644934415817261})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6831600666046143})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6960155963897705})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7536648511886597})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7755446434020996})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7910040616989136})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7342313528060913})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8516638278961182})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8188754916191101})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.835466206073761})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.633011328125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.624060869216919})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5131617188453674})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.49925243854522705})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4508618712425232})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.48337411880493164})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43919217586517334})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4459441304206848})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4327235817909241})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4277607202529907})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 57882], ['id', 16072], ['id', 15472], ['id', 56346], ['id', 18575]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8638473506941702, 1.6108276577780507, 2.2165320710291647, 2.6268865699586375, 2.8544685192712604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9377822875976562})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7450512051582336})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7384752035140991})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7338269352912903})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8212342262268066})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8056274652481079})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8656281232833862})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8624331951141357})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.716027294921875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6533865928649902})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.535802960395813})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4915449917316437})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.49784642457962036})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4584406912326813})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4874071478843689})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4456561803817749})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 57768], ['id', 10205], ['id', 8892], ['id', 57718], ['id', 46726]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7827847965935049, 1.4841956907695106, 2.085925508219927, 2.5012144645738097, 2.769775486220219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9912797212600708})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6610277891159058})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6113356947898865})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6385675668716431})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6488032341003418})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6843913793563843})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7006609439849854})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.512009375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6790891289710999})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5583438873291016})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5034393072128296})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.47140631079673767})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45909857749938965})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.45427656173706055})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 9118], ['id', 42467], ['id', 4822], ['id', 5422], ['id', 37907]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6976337464709328, 1.3238475941284884, 1.8202530492663413, 2.1986244686638434, 2.4565273155461638]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9010964632034302})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7205049395561218})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7127058506011963})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7002108097076416})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7388195991516113})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7063231468200684})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.817539632320404})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.604775244140625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6695787906646729})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5499821901321411})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4908338487148285})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4655567407608032})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4500269293785095})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4749279022216797})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 1019], ['id', 14881], ['id', 5013], ['id', 42193], ['id', 32702]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7318284635137766, 1.3486260040148403, 1.8666986806580637, 2.25277018565877, 2.5141604911362743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8828201293945312})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6236801147460938})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6264692544937134})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6317271590232849})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7102624177932739})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6142562627792358})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6963996887207031})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7086888551712036})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7178217172622681})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.55895830078125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6660374402999878})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5215877294540405})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.45884883403778076})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4216277599334717})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4365862011909485})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4140143394470215})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4197639226913452})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4107690453529358})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 31650], ['id', 37632], ['id', 31292], ['id', 48630], ['id', 48760]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6952390906519661, 1.3241750680389814, 1.8345951935282425, 2.2371785091095227, 2.5015831882413435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9346233606338501})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.653547465801239})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.651167631149292})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6151762008666992})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.588173508644104})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6576180458068848})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7136030197143555})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6426898241043091})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7003083825111389})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6690806746482849})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8132951259613037})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.58703017578125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6519788503646851})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4996475577354431})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4474460184574127})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4405374526977539})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4339427649974823})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41464197635650635})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.39257359504699707})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.37883907556533813})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40491992235183716})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.38365882635116577})
store['active_learning_steps'][22]['eval_training']['best_epoch']=9
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 3415], ['id', 57880], ['id', 12236], ['id', 25546], ['id', 25309]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8350112580348825, 1.5893273184220567, 2.232045773465522, 2.651720840631274, 2.8817812674678036]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9456286430358887})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5777021646499634})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5705999135971069})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5440301895141602})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5771899223327637})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6005035638809204})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6599937677383423})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6563005447387695})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9364, 'crossentropy': 0.47247431640625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6348638534545898})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4785902500152588})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.44392549991607666})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4584527611732483})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.407691091299057})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38394322991371155})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3969508409500122})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 25156], ['id', 19212], ['id', 54490], ['id', 14769], ['id', 12514]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7438044586300907, 1.4539735500466016, 2.0479937410950733, 2.4217485155779057, 2.629440398054654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0631537437438965})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5955649614334106})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5835155248641968})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.555773138999939})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6386594772338867})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.522283837890625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6780132055282593})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5884733200073242})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5050510168075562})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5829067230224609})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 50908], ['id', 16909], ['id', 20641], ['id', 42078], ['id', 59283]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6477241642474174, 1.205172240044155, 1.685055872700378, 2.083441818866051, 2.363831482409573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8668018579483032})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5774175524711609})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5401576161384583})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5970295667648315})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5606468915939331})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6222174167633057})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5658531188964844})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5854398012161255})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.43024794921875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6095250844955444})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5272904634475708})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4307047128677368})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.38968461751937866})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3795870542526245})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3985891342163086})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.3895307779312134})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 41196], ['id', 39461], ['id', 32335], ['id', 56913], ['id', 31741]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6744299577739132, 1.2487801047735498, 1.7339616064762158, 2.0997601489206623, 2.3287108454405248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8985244035720825})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5647662878036499})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6145232915878296})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6000247001647949})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6177772283554077})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.4859853515625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7501786351203918})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6303030252456665})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5675357580184937})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5525468587875366})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 8480], ['id', 17535], ['id', 49064], ['id', 12493], ['id', 51759]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5232228913545389, 1.0198151521966365, 1.416340787257755, 1.7423860298251048, 2.0029066686597066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9254106879234314})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.558674693107605})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5711909532546997})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5479207038879395})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5698391795158386})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5567735433578491})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6167035698890686})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6523739099502563})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6130714416503906})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.455208203125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6265586018562317})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.46243810653686523})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4345097839832306})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.39728957414627075})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.37637507915496826})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4052109718322754})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.36253851652145386})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3511403203010559})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 16023], ['id', 50212], ['id', 49010], ['id', 56480], ['id', 30071]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7342504868738273, 1.3548995080797228, 1.8793225412960899, 2.2653332187532307, 2.5128047971043452]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.1490356922149658})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6092206239700317})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6038335561752319})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.619260311126709})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6497272253036499})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5684119462966919})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6839183568954468})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.69609534740448})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.585137128829956})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7158593535423279})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6897213459014893})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7907898426055908})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.4887953125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.702642560005188})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.521307647228241})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4721801280975342})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4188615679740906})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.39136070013046265})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.37638235092163086})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.41979873180389404})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.3915647864341736})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3711274266242981})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 1758], ['id', 3474], ['id', 31794], ['id', 45034], ['ood', 58822]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7764929253887669, 1.443857991438155, 2.0140132604326504, 2.4416336082768852, 2.723858757662555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9792905449867249})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6076123714447021})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.48904842138290405})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5966410040855408})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5577397346496582})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5274897813796997})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.415097802734375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6131744384765625})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4733578562736511})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.44340822100639343})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.413602739572525})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3988177180290222})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 48006], ['id', 49425], ['id', 33404], ['id', 42004], ['id', 42838]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6240842534855022, 1.1935490825796689, 1.6792545866886108, 2.0458202584942935, 2.30170126228861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.1043105125427246})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6110799312591553})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4934127628803253})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5591981410980225})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5643584728240967})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6676281094551086})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6727997064590454})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.48088330078125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6351786851882935})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4894425868988037})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.439655065536499})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4222929775714874})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3964937925338745})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4189980626106262})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 37491], ['id', 37574], ['id', 36818], ['id', 52800], ['id', 43702]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7075690589146242, 1.3504215644791189, 1.8733273563353112, 2.238380974285426, 2.4946627677559725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0888185501098633})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6126348376274109})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5500000715255737})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5021536350250244})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49926015734672546})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.515639066696167})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.605075478553772})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5508608222007751})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6047753691673279})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.43420390625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6692537069320679})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4879745841026306})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4227769672870636})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4331943988800049})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4005683660507202})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40735357999801636})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.382189005613327})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3622545599937439})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 6130], ['id', 8693], ['id', 40259], ['id', 4014], ['id', 23516]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7113969126482671, 1.3552350813894418, 1.900340335396029, 2.2840395748808042, 2.548767508204998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.142498254776001})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6328240633010864})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5622900724411011})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5245307683944702})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4960857033729553})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5578689575195312})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5559922456741333})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5456269383430481})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6138241291046143})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6053529381752014})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9417, 'crossentropy': 0.451598583984375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.679097592830658})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.472695529460907})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4131866693496704})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.38684147596359253})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.37104156613349915})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3524104952812195})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3461339473724365})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3780270218849182})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 14851], ['id', 22283], ['id', 51482], ['id', 43012], ['id', 35021]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7130313897290081, 1.3623445568943646, 1.9134224320422994, 2.3033890678848232, 2.5675327005224675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.085358738899231})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5532920360565186})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47237616777420044})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4580659866333008})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5208826065063477})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5131999850273132})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.563617467880249})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5087192058563232})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5410297513008118})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5046406984329224})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47961997985839844})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.4022095947265625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6682248711585999})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4236541986465454})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.40209025144577026})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3645702004432678})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3770033121109009})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3359074592590332})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.32305124402046204})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.31000882387161255})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.33236080408096313})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 38711], ['id', 11208], ['id', 36139], ['id', 19895], ['id', 43636]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7678806584433293, 1.444819395397686, 2.0007072733332727, 2.4104855136807357, 2.660347567746377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0967423915863037})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.569938063621521})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5050941705703735})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4209134578704834})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4510609805583954})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44355541467666626})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4056451618671417})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45819804072380066})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4191809296607971})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4445061683654785})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44003355503082275})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5062268376350403})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43960124254226685})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4791378676891327})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4581714868545532})
store['active_learning_steps'][34]['training']['best_epoch']=12
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9516, 'crossentropy': 0.411371728515625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5891596674919128})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42190229892730713})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3731544613838196})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3660392165184021})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.356765478849411})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34234005212783813})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3561760187149048})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34409022331237793})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3142191469669342})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 30900], ['id', 33340], ['id', 40264], ['id', 47690], ['id', 57793]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8119306669845014, 1.5548566914193365, 2.1513494173260614, 2.5597532190352306, 2.795806569540951]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.076999306678772})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.544921875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43857041001319885})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4125311076641083})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4170626401901245})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45573994517326355})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.3984423095703125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7182198762893677})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.509482741355896})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.47111958265304565})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42166292667388916})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4060109853744507})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 44123], ['id', 33362], ['id', 11482], ['id', 55851], ['id', 28182]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5704160959289415, 1.077641804422194, 1.517719035522326, 1.8786634480609479, 2.141893682745679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0271201133728027})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6463212370872498})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.46739068627357483})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4977107048034668})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4601231515407562})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5023455619812012})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47821617126464844})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4694587290287018})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4795817732810974})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5049481391906738})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4652005434036255})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5137724280357361})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.449432909488678})
store['active_learning_steps'][36]['training']['best_epoch']=10
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.951, 'crossentropy': 0.42339365234375}
