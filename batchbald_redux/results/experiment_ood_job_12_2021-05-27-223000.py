store = {}
store['timestamp']=1622151000
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=12']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=12
store['worker_id']=12
store['num_workers']=40
store['config']={'seed': 1247, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.237905979156494})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.6937150955200195})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7671799659729004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8729186058044434})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6896, 'crossentropy': 2.03115}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 34678], ['id', 13827], ['id', 39100], ['id', 47322], ['id', 14145]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.162343242047232, 2.113954876847771, 2.868197555468548, 3.4354944871531607, 3.837383304418899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.278745174407959})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.542788505554199})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.7584891319274902})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.9554712772369385})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.9853646755218506})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.8962106704711914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.1516642570495605})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.4023001194000244})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7168, 'crossentropy': 2.525937890625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 22861], ['id', 9687], ['id', 42123], ['id', 47844], ['id', 1272]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.4277829490485385, 2.605013098689797, 3.4782118574447516, 4.020942322133097, 4.310846399986298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.965559482574463})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.1640965938568115})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.272700309753418})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.701136589050293})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7036, 'crossentropy': 1.8302064453125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 15798], ['id', 31400], ['id', 24457], ['id', 28136], ['id', 43008]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.163016411340315, 2.106596192620801, 2.898154764615768, 3.4457315921221685, 3.833123049398635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.7544199228286743})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.2729501724243164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1272215843200684})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.4917311668395996})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.5040440559387207})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6267776489257812})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.726, 'crossentropy': 2.0507888671875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 45845], ['id', 27915], ['id', 55182], ['id', 31637], ['id', 49607]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.175737958061052, 2.260542377420065, 3.093038636246737, 3.6650597802033777, 4.030101759877494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.8112454414367676})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2606682777404785})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.398961067199707})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.68125057220459})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.6384060382843018})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.850003957748413})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.6194992065429688})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.9201955795288086})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7274, 'crossentropy': 2.50235}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 9912], ['id', 49548], ['id', 46530], ['id', 52574], ['id', 34468]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2468818257798309, 2.3590622145965217, 3.223189843780858, 3.821908373708025, 4.176665182502429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2964179515838623})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.6631548404693604})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7386610507965088})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6283925771713257})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.7949248552322388})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.8343695402145386})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.9255889654159546})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.9000604152679443})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7811, 'crossentropy': 1.6444142578125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 55591], ['id', 28512], ['id', 37181], ['id', 9508], ['id', 56348]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.2316939793516781, 2.2781706816538168, 3.1457323175423397, 3.763226177263551, 4.157310258383937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2486026287078857})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2312016487121582})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4188417196273804})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.552877426147461})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.3800067901611328})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.5182675123214722})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8189, 'crossentropy': 1.260206640625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 5088], ['id', 28102], ['id', 207], ['id', 35232], ['id', 24038]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1447334092643628, 2.2082935432895123, 3.052348677010265, 3.6421996673788124, 4.017349976984297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1893150806427002})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.585842251777649})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.7065470218658447})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.9426939487457275})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7887, 'crossentropy': 1.104915625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 47787], ['id', 8691], ['id', 45047], ['id', 20057], ['id', 31624]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9336865723152528, 1.7784735696324208, 2.5064469102101885, 3.05732992611107, 3.48575456145284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1636931896209717})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.4943383932113647})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.4453465938568115})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.661240577697754})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5726039409637451})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5226502418518066})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.801, 'crossentropy': 1.367780078125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 36303], ['id', 49497], ['id', 26444], ['id', 4133], ['id', 30188]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1509777636106504, 2.123908768785365, 2.9597545859376915, 3.539143748659777, 3.9299813400709933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0069422721862793})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1373497247695923})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1018415689468384})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0857503414154053})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.192623496055603})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1489402055740356})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1945009231567383})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3255417346954346})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.3923304080963135})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3140625953674316})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8548, 'crossentropy': 1.16064033203125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 51199], ['id', 50317], ['id', 40766], ['id', 32926], ['id', 25332]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2555631091227084, 2.346668864569286, 3.214149934560867, 3.825240749682532, 4.203786481783404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0936778783798218})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.160088062286377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1923370361328125})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.221427321434021})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2285313606262207})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1972111463546753})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3829376697540283})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.4194080829620361})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3656225204467773})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8507, 'crossentropy': 1.15323837890625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 26072], ['id', 34445], ['id', 48384], ['id', 18962], ['id', 6066]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2732564068758707, 2.382553414179274, 3.263570040390694, 3.8774046772311728, 4.219402819981765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1088669300079346})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2054498195648193})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4090332984924316})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3029645681381226})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4408804178237915})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.351011037826538})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.283697247505188})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2423121929168701})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.5721914768218994})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.623838186264038})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5154800415039062})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8438, 'crossentropy': 1.18434990234375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 42121], ['id', 56379], ['id', 1278], ['id', 52169], ['id', 23187]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.143942844481919, 2.1804211089746355, 3.0080573520292857, 3.6210365241739995, 4.030817154274112]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.105217695236206})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0854560136795044})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.196599006652832})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4141440391540527})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.18719482421875})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3816938400268555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.5224617719650269})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3917909860610962})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8561, 'crossentropy': 1.0585537109375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 6418], ['id', 16971], ['id', 49474], ['id', 33484], ['id', 424]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1713630815937346, 2.182597868719784, 3.031728264168253, 3.6765764626246096, 4.0647447057000505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8448271751403809})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7542688846588135})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7147769927978516})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8211879730224609})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7254642248153687})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7623145580291748})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9364741444587708})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8993179798126221})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8686214685440063})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.735820703125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 39480], ['id', 21023], ['id', 29132], ['id', 21532], ['id', 43065]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1358881867232982, 2.159347700307022, 3.0540058522791345, 3.6925771014701745, 4.084682211976872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9264624118804932})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7488836050033569})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8130344152450562})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8212316036224365})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8542089462280273})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.670209228515625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24587], ['id', 55311], ['id', 38298], ['id', 48880], ['id', 31301]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9685341075075942, 1.8317291860716693, 2.586823711726316, 3.19071840899094, 3.648374496678395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9409121870994568})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7964718341827393})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7321525812149048})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7988932132720947})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8443628549575806})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7759259343147278})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8116432428359985})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9461848735809326})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8298953175544739})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9054610729217529})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.74706962890625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 2381], ['id', 36417], ['id', 56464], ['id', 46412], ['id', 14697]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1459474242873535, 2.189587130729777, 3.047079074813551, 3.672755190272585, 4.0806471831046105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9385225772857666})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.731979489326477})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7551279067993164})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7879340648651123})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8500555157661438})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.862882137298584})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9024, 'crossentropy': 0.646943310546875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 58560], ['id', 6604], ['id', 39656], ['id', 37962], ['id', 34677]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9710589505723477, 1.8551002462057076, 2.643357433257096, 3.2616795657773974, 3.721416471416661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0317234992980957})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.743561863899231})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7102946043014526})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7761268019676208})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8782539367675781})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7933897972106934})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7626610994338989})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8922481536865234})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8036478757858276})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8541346192359924})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9087, 'crossentropy': 0.70709462890625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 38397], ['id', 26733], ['id', 49563], ['id', 33162], ['id', 6272]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.226236701765635, 2.3399098204093716, 3.1421302694650226, 3.7213792863192747, 4.096606253289407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1073168516159058})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7415452003479004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7261053323745728})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6706756949424744})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7119582891464233})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8638860583305359})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.869910478591919})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7784249782562256})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.684176171875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 19942], ['id', 34520], ['id', 57728], ['id', 8887], ['id', 51004]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.1278719477662316, 2.1458956636487376, 3.0083862896231457, 3.6258972498532263, 4.031561623500023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9790714979171753})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6357667446136475})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6095418930053711})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5612213015556335})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5940089225769043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.627383291721344})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6721541881561279})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7067660093307495})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6725651621818542})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7473020553588867})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.6073587890625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 34115], ['id', 38409], ['id', 29834], ['id', 49200], ['id', 50366]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1426474613527762, 2.186463551858324, 3.031114427712849, 3.660644931869637, 4.069161628394357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0204954147338867})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6134066581726074})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6290173530578613})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5448107719421387})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6521588563919067})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7374162077903748})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6185462474822998})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.548119580078125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 15767], ['id', 13942], ['id', 16911], ['id', 36126], ['id', 12257]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0157819417990703, 1.9546104668242856, 2.7732569823982285, 3.3921332673986964, 3.8210105305549007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.015189528465271})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6598935127258301})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6046100854873657})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6002247333526611})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6628562211990356})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5995179414749146})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6016536355018616})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7472132444381714})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6432987451553345})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.553031494140625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 57474], ['id', 55244], ['ood', 6574], ['id', 43126], ['id', 59726]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.110028465775494, 2.071017277154713, 2.842206633644592, 3.4433080593403975, 3.879433937271468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9789304733276367})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5874367952346802})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6219363212585449})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5804671049118042})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6287143230438232})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6920974254608154})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7039393186569214})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.55249892578125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 16628], ['id', 20172], ['id', 51464], ['id', 17059], ['id', 3791]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0797678748061625, 2.041239406206139, 2.8177241557495716, 3.3991675411439033, 3.818489603349235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9545263648033142})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6457675695419312})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6572376489639282})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5957433581352234})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5602636933326721})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.534252941608429})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6326931715011597})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.61264967918396})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.568054052734375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 4955], ['id', 35566], ['id', 42838], ['id', 46832], ['id', 5163]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0865945164435713, 2.102898798259705, 2.958681351738363, 3.5887894577594297, 3.994781349529716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0298473834991455})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6519278287887573})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5657634735107422})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5270591378211975})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49261707067489624})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5712282657623291})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6129070520401001})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.528023974609375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 3980], ['id', 5679], ['id', 54994], ['id', 45784], ['id', 9433]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9887747589863438, 1.8964920643443035, 2.6840355903522806, 3.3035586253476517, 3.7441319962455744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1603453159332275})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6691261529922485})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5523377060890198})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5595394372940063})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5676974058151245})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5342155694961548})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6238977909088135})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5702721476554871})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.618107795715332})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.53375439453125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 14749], ['id', 41307], ['id', 14367], ['id', 38920], ['id', 2845]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0613490768466254, 2.02082774394536, 2.8462020511230346, 3.4877554637138237, 3.927375414475481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.116811752319336})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6228487491607666})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5645798444747925})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5687114596366882})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5524571537971497})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5425326228141785})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.56137275390625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 7146], ['id', 26635], ['id', 42078], ['id', 32880], ['id', 3947]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9250464702085468, 1.7364347880037516, 2.4491633825782735, 3.040944481784271, 3.5041606432567782]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.257727861404419})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6694308519363403})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5415273904800415})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5338411331176758})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49943113327026367})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.527572512626648})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.479094091796875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 59314], ['id', 9180], ['id', 42703], ['id', 51759], ['id', 39561]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9995874974173831, 1.894566957703426, 2.6317159859337, 3.2096686501791076, 3.6521293552421312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2363359928131104})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6510417461395264})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5134152173995972})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4931132197380066})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4963037967681885})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4824768006801605})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5205553770065308})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9378, 'crossentropy': 0.465801611328125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 31289], ['id', 21880], ['id', 8978], ['id', 9118], ['id', 34739]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9962646592081832, 1.8876759419803308, 2.67276058679424, 3.2905331227421684, 3.7299582412280827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1849242448806763})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7135457992553711})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5743846297264099})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5786111354827881})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5635936260223389})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5538144111633301})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.516941650390625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 27514], ['id', 30810], ['id', 31090], ['id', 3691], ['id', 32445]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8184478544194345, 1.571384289183218, 2.2613006496985086, 2.8498746207178147, 3.33293265627268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2680320739746094})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6113729476928711})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5179377794265747})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4850917458534241})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4790780544281006})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5156947374343872})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5428351163864136})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4966609477996826})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.441334375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 17958], ['id', 59297], ['id', 18598], ['id', 45658], ['id', 5684]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9812781432423847, 1.8800811107023057, 2.664428702012975, 3.3024046643780434, 3.748471091321661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1492438316345215})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.649217963218689})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5414285659790039})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4901279807090759})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5034719705581665})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5695982575416565})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5674355030059814})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.475334619140625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 34946], ['id', 33388], ['id', 7322], ['id', 40066], ['id', 54954]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9373753590056859, 1.7928350826983563, 2.5597937434100277, 3.1623924267932564, 3.6169664936072525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1984245777130127})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5821080207824707})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5129532217979431})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5412810444831848})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5156641006469727})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.606994140625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 52099], ['id', 32523], ['id', 59158], ['id', 31184], ['id', 36268]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7397414539669454, 1.4417350811470362, 2.043387110307944, 2.5596681194393263, 2.9989220372469667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.240553617477417})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6552565693855286})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4966445863246918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4498205780982971})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5007100701332092})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4968527853488922})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9409, 'crossentropy': 0.4617220703125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 34847], ['id', 20037], ['id', 1674], ['id', 37469], ['id', 56082]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8184099458429379, 1.5663047852780503, 2.246495597374592, 2.8176270563250236, 3.273283406008799]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2598029375076294})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7164352536201477})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5305945873260498})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5875478982925415})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4850775897502899})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.507950484752655})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6230061054229736})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5240883231163025})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5278198719024658})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.94, 'crossentropy': 0.469404443359375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 43950], ['id', 26358], ['id', 46441], ['id', 50371], ['id', 3136]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.0394280240442568, 1.9484820654145416, 2.7540421488921574, 3.3943395647274635, 3.817682218277832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1579937934875488})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6848728656768799})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4602211117744446})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44809117913246155})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42625394463539124})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44419988989830017})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5140522122383118})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9433, 'crossentropy': 0.4442642578125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 4822], ['id', 46368], ['id', 32776], ['id', 9557], ['id', 11292]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9489989965110723, 1.792523159112688, 2.5367436809942507, 3.125302136274426, 3.573364699066297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.223872184753418})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6290560960769653})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5069111585617065})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4664969742298126})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4925060272216797})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49451401829719543})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4707610607147217})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5169875621795654})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47810089588165283})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9411, 'crossentropy': 0.486767578125}
