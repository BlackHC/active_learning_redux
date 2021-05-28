store = {}
store['timestamp']=1622153763
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=18']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=40
store['config']={'seed': 1254, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.1405153274536133})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.7438406944274902})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.836555004119873})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1440744400024414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.973517656326294})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.022418975830078})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.2519776821136475})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.200282573699951})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6854, 'crossentropy': 2.58655234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1124694347381592})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.145745873451233})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1587066650390625})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1230838298797607})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 29433], ['id', 23859], ['id', 55558], ['id', 1574], ['id', 35521]], 'labels': [5, 2, 6, 9, 8], 'scores': [1.1932794500326334, 2.0580601387571553, 2.7041052907657717, 3.098327604134079, 3.3134532785141317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.9533638954162598})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.315800189971924})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.5944762229919434})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.6354308128356934})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.998765468597412})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.9088950157165527})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.5332770347595215})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7175, 'crossentropy': 2.30522890625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0714783668518066})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9846502542495728})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9622036814689636})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9818528890609741})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.058830738067627})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 4873], ['id', 4066], ['id', 5173], ['id', 11712], ['id', 44002]], 'labels': [8, 1, 3, 0, 8], 'scores': [1.1775513627758774, 2.0992849173480925, 2.6925651433057283, 3.0801182669540053, 3.2805696121744994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.52763032913208})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.782780408859253})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.044365406036377})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.989799976348877})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.9622007608413696})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7649, 'crossentropy': 1.6890607421875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9347701072692871})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9131903648376465})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.886623740196228})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8735834360122681})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 1423], ['id', 45753], ['id', 45424], ['id', 2765], ['ood', 53991]], 'labels': [0, 5, 4, 0, -1], 'scores': [1.0331666884749726, 1.9064667156190547, 2.545142589249303, 2.887467555299211, 3.084541023834216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.6632839441299438})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.91563081741333})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.438767433166504})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.2479569911956787})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7537, 'crossentropy': 1.46744521484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.0115141868591309})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9397691488265991})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9441705346107483})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 8702], ['id', 14679], ['id', 36825], ['id', 22769], ['id', 20859]], 'labels': [9, 8, 8, 2, 8], 'scores': [0.8292625483520752, 1.4826581723944368, 1.9942207580486766, 2.3706541890609634, 2.6013882440409066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8749136924743652})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.9620978832244873})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.9428198337554932})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.3535537719726562})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.390883445739746})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.2074499130249023})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.239436149597168})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.5658068656921387})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7612, 'crossentropy': 2.10369453125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9988232851028442})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.8724690675735474})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.867059051990509})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9344856142997742})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9260995388031006})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 41904], ['id', 57292], ['id', 20573], ['id', 41283], ['ood', 16319]], 'labels': [5, 7, 9, 3, -1], 'scores': [1.0514302049042845, 1.9253256758508046, 2.5577939763490605, 2.9287946703687657, 3.121131931676481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.799201250076294})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.8759925365447998})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.5359115600585938})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.199655532836914})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.755093574523926})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7408, 'crossentropy': 1.846387109375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.0178184509277344})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9974579811096191})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0104509592056274})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9860491752624512})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 22506], ['id', 27316], ['id', 14341], ['id', 37491], ['id', 50343]], 'labels': [5, 3, 9, 2, 6], 'scores': [0.8710747134260817, 1.5739489608133885, 2.1284317497766487, 2.526170578665152, 2.7520020973360104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.455451250076294})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.658562421798706})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.141380786895752})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.2282323837280273})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.2377796173095703})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7639, 'crossentropy': 1.60535478515625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.9973330497741699})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.8808916807174683})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9389482736587524})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9021302461624146})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 39397], ['id', 7596], ['id', 12223], ['id', 5422], ['id', 51600]], 'labels': [3, 4, 2, 7, 4], 'scores': [0.8646099327409755, 1.5714096561539614, 2.1311657053889537, 2.47058071431886, 2.6817681258257116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.6300787925720215})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.779614806175232})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.924337387084961})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.243114709854126})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.464656352996826})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.4247183799743652})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7462, 'crossentropy': 1.9307353515625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.0087194442749023})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.9618840217590332})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.940964937210083})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9583638906478882})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9618624448776245})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 16195], ['id', 1311], ['id', 52686], ['id', 189], ['id', 33912]], 'labels': [4, 5, 5, 2, 7], 'scores': [0.914385769902788, 1.6861902827308253, 2.299408500915881, 2.664640188040363, 2.8649994080587255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.138822317123413})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3791964054107666})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3103010654449463})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.408217430114746})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5401289463043213})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4158601760864258})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.6514310836791992})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5116829872131348})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.864706039428711})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8368, 'crossentropy': 1.2284939453125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9000396728515625})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8065587282180786})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7041082382202148})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6770974397659302})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6714794635772705})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.6772129535675049})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6931596994400024})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 21408], ['id', 49957], ['ood', 14612], ['id', 4919], ['ood', 58209]], 'labels': [8, 5, -1, 4, -1], 'scores': [0.9020818914465243, 1.7252937202873886, 2.3232779499157665, 2.74089037561981, 3.0052608056619636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3072923421859741})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.5792030096054077})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.6717216968536377})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.7046886682510376})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.6788122653961182})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.8260157108306885})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.9948060512542725})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 2.1310324668884277})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8067, 'crossentropy': 1.59561162109375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8819077610969543})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8211781978607178})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.7984762787818909})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.7834515571594238})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.7844408750534058})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 3382], ['id', 19590], ['id', 16860], ['id', 26733], ['id', 53977]], 'labels': [9, 5, 8, 2, 7], 'scores': [0.9334624780833727, 1.757609845449272, 2.3831507542439887, 2.7643471629090746, 2.9572094453659634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0875649452209473})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0597131252288818})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2078323364257812})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1722347736358643})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4168214797973633})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3489811420440674})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.4968719482421875})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8561, 'crossentropy': 1.07029140625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8349477052688599})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7175770998001099})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6388989686965942})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6532248854637146})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6436222791671753})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.5989949703216553})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 17404], ['id', 42821], ['id', 37313], ['id', 43588], ['id', 28375]], 'labels': [3, 2, 5, 8, 5], 'scores': [0.9015125603818706, 1.6324268241688662, 2.202550267731916, 2.5937387412053923, 2.8173489449083124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9207676649093628})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.098196029663086})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2770826816558838})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3571972846984863})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.4739086627960205})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.5207116603851318})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8476, 'crossentropy': 1.16725498046875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.7964604496955872})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7289725542068481})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6689580082893372})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.692868709564209})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6732168793678284})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 49509], ['id', 6174], ['id', 659], ['id', 44345], ['id', 58398]], 'labels': [8, 9, 3, 4, 2], 'scores': [0.8399691558310187, 1.6022573751800695, 2.194224081597305, 2.5953413700478114, 2.8358500789184475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0912916660308838})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1323869228363037})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2602825164794922})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.437325358390808})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.5279531478881836})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.849, 'crossentropy': 1.03001650390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8007630109786987})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7288157939910889})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.6985424757003784})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6915560364723206})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 27225], ['id', 1290], ['id', 47597], ['id', 34042], ['id', 12297]], 'labels': [7, 3, 8, 8, 9], 'scores': [0.7909177906845524, 1.4621524346788854, 1.9430379610321173, 2.286352703250527, 2.528499087171406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0940871238708496})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1131622791290283})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2201048135757446})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.275726079940796})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.4485889673233032})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.4119899272918701})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.482108473777771})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.868, 'crossentropy': 1.0687068359375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7818853855133057})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.697938084602356})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6543869972229004})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6696346998214722})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6611802577972412})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6240508556365967})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 57514], ['id', 48102], ['id', 46379], ['id', 49673], ['ood', 43952]], 'labels': [6, 7, 3, 3, -1], 'scores': [0.8517499489872002, 1.603375309757204, 2.1859427438271, 2.5656078511466145, 2.794920808204372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0602588653564453})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0856106281280518})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1628937721252441})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3829874992370605})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.3709945678710938})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.5781543254852295})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.29140305519104})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.6785451173782349})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.8154613971710205})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.6210213899612427})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.7709898948669434})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.6894824504852295})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.7374284267425537})
store['active_learning_steps'][14]['training']['best_epoch']=10
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8589, 'crossentropy': 1.2819341796875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8248043060302734})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6845364570617676})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6803997755050659})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.6780604124069214})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6647399663925171})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6486598253250122})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 20792], ['id', 21390], ['id', 9449], ['id', 31710], ['id', 35545]], 'labels': [9, 3, 2, 8, 5], 'scores': [0.8562365944334194, 1.6197060967499604, 2.2186139623961445, 2.5895785986364466, 2.760735388232108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9448505640029907})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.047213077545166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0996133089065552})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1830806732177734})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2000575065612793})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.415057897567749})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3901855945587158})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8592, 'crossentropy': 1.05489814453125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8324605226516724})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.716640055179596})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6716718673706055})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6778998970985413})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6674506664276123})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.620498538017273})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 6446], ['id', 58401], ['id', 55496], ['id', 8458], ['id', 21242]], 'labels': [0, 9, 9, 4, 0], 'scores': [0.8623646968831173, 1.5733736235055735, 2.148276761924002, 2.572769491521658, 2.8313169633789226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9237080812454224})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9078671932220459})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9951788187026978})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1073436737060547})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1454286575317383})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1437112092971802})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2634791135787964})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2871356010437012})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2845513820648193})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8698, 'crossentropy': 1.00483193359375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8156185150146484})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.688505232334137})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6742092370986938})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6085162162780762})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.6074373126029968})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.5834370851516724})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.5832295417785645})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.5847529172897339})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 39309], ['id', 19023], ['ood', 26118], ['id', 23236], ['id', 42793]], 'labels': [0, 7, -1, 6, 4], 'scores': [0.9334050895250954, 1.709902975208637, 2.355985483005357, 2.7927687286412333, 3.0478412751114092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.94638991355896})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9080600738525391})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9640555381774902})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0057860612869263})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2230007648468018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.2594513893127441})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.2234638929367065})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8784, 'crossentropy': 0.88738798828125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7851298451423645})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6472764015197754})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.5981571674346924})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.5990989208221436})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.5618820190429688})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5817966461181641})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 43434], ['id', 9568], ['id', 4414], ['id', 41962], ['id', 50993]], 'labels': [2, 5, 2, 9, 1], 'scores': [0.7122684347928978, 1.37817243520752, 1.941336224805613, 2.329998497532431, 2.5662386184518624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9634225368499756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7614202499389648})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.769149899482727})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8811291456222534})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9317030906677246})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9441639184951782})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9210855960845947})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8771002292633057})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8980802893638611})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0580055713653564})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.044775128364563})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 1.001051902770996})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.763891357421875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.69644695520401})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5397790670394897})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5049172639846802})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4857863783836365})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4286947250366211})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.43017449975013733})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4320249557495117})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4298666715621948})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 42838], ['id', 57882], ['id', 3390], ['id', 17487], ['id', 7700]], 'labels': [9, 0, 2, 1, 6], 'scores': [1.0569526612973315, 1.884333117484326, 2.4787387662314844, 2.901657846072574, 3.107343749657474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8876425623893738})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7949955463409424})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6434025764465332})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7093797326087952})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8900384902954102})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.782415509223938})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8350863456726074})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7373347878456116})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7706378102302551})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8310564160346985})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.770550012588501})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.9209408164024353})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.9001479148864746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.9757863283157349})
store['active_learning_steps'][19]['training']['best_epoch']=11
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.664052783203125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6714413166046143})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.48607614636421204})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4359276294708252})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.39935722947120667})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4087716341018677})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.38014429807662964})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.37532564997673035})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 5303], ['id', 26966], ['id', 34920], ['ood', 19185], ['ood', 26892]], 'labels': [5, 7, 9, -1, -1], 'scores': [0.98056975480931, 1.7858486389959527, 2.344886392334125, 2.7068408326991555, 2.9061648521864054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8257945775985718})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7322639226913452})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6851726770401001})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7192516922950745})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7524858713150024})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7317600250244141})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8107079863548279})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8351906538009644})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9118, 'crossentropy': 0.637228515625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6258243322372437})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.46026086807250977})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.46944504976272583})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4488488435745239})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.41132330894470215})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 59344], ['id', 37154], ['id', 26850], ['ood', 53460], ['ood', 43952]], 'labels': [9, 1, 2, -1, -1], 'scores': [0.8849619182170714, 1.5686599065392133, 2.100961297273831, 2.4254921980611863, 2.6226559565353273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8173121213912964})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7585028409957886})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7268187999725342})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.736100435256958})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7188549041748047})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7026169300079346})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7584370374679565})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.883431077003479})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.79929518699646})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.5956220703125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6617456674575806})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5155627727508545})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.45128530263900757})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4459685981273651})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4025542140007019})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.40743905305862427})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4113091230392456})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.37781599164009094})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 30884], ['id', 56514], ['id', 55314], ['ood', 43952], ['ood', 1254]], 'labels': [2, 2, 6, -1, -1], 'scores': [0.8882863878995608, 1.6697754323757446, 2.305560390835364, 2.693992649481829, 2.931347582861351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9196271896362305})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6946433782577515})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6508498191833496})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7481703758239746})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8222228288650513})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7820026874542236})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.840889573097229})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8896965980529785})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8772797584533691})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.67935}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6925493478775024})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5124824047088623})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4811512231826782})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.46389442682266235})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.425481379032135})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4402594566345215})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.41279083490371704})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4186495542526245})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 34328], ['id', 41832], ['id', 20287], ['id', 17417], ['ood', 19837]], 'labels': [8, 2, 4, 4, -1], 'scores': [0.8590841829743434, 1.661798618124426, 2.221942233660914, 2.5842967543911186, 2.776176847740542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.90886390209198})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.702983021736145})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6507500410079956})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7506521344184875})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7864648103713989})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7835687398910522})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.570103076171875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.752250075340271})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5902531147003174})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5164753198623657})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.49546095728874207})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.489530086517334})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 53979], ['id', 1075], ['id', 14001], ['id', 41383], ['id', 57463]], 'labels': [8, 7, 1, 0, 6], 'scores': [0.7301465502256026, 1.3009828184792447, 1.7781862060428777, 2.130627760087041, 2.3691269264295087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9036418199539185})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6361535787582397})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5964033603668213})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7296489477157593})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6708250641822815})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7333970069885254})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.505685400390625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6295729875564575})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.49081751704216003})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4473986029624939})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4560038447380066})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4451223611831665})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 57345], ['id', 26511], ['ood', 57069], ['id', 58874], ['ood', 29068]], 'labels': [5, 6, -1, 3, -1], 'scores': [0.6822240772062664, 1.3030946085620698, 1.8145760497087284, 2.2030705996839135, 2.4857495141128547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7948023676872253})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6270558834075928})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6197119951248169})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6345337629318237})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6990203857421875})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7253785133361816})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.511360546875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6341345310211182})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5187522172927856})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4592156410217285})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4818189740180969})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.41605883836746216})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 30530], ['id', 53120], ['id', 30478], ['id', 5315], ['id', 11208]], 'labels': [2, 5, 8, 3, 9], 'scores': [0.7086338770506913, 1.3686847738364105, 1.9065892267522342, 2.2885784195737546, 2.531711746903065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0213720798492432})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5612791776657104})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.540524959564209})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5558277368545532})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6009103059768677})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5825787782669067})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.624054491519928})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6756222248077393})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6339672803878784})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7154121398925781})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.555293603515625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5824270844459534})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4592071771621704})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4099406599998474})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41300320625305176})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.3910064697265625})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.36570724844932556})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.35678744316101074})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.35441210865974426})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3586695194244385})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 33364], ['id', 22272], ['id', 2546], ['ood', 19837], ['ood', 25759]], 'labels': [2, 5, 4, -1, -1], 'scores': [0.8981753153374556, 1.649640165133202, 2.2715183608718554, 2.6783258158589582, 2.907947643138616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8704484701156616})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5792853236198425})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6043568253517151})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6837910413742065})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6338602304458618})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6677076816558838})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6881762742996216})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7523723840713501})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.541951806640625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.575702428817749})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4894881248474121})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4467531442642212})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4223644733428955})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.39132261276245117})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.39074772596359253})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.39001035690307617})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 35232], ['id', 48973], ['ood', 53357], ['ood', 15878], ['id', 57972]], 'labels': [8, 8, -1, -1, 4], 'scores': [0.8066461024118654, 1.5017764468440369, 2.052065824240792, 2.4163972396423015, 2.6355697847843658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8566651344299316})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5737593770027161})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5929479598999023})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6534033417701721})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6432952284812927})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6214300394058228})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6562182903289795})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7113118767738342})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6118674278259277})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7718035578727722})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6734344959259033})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7624051570892334})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.561519482421875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6374499797821045})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4829058349132538})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4514094591140747})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.40363845229148865})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.37633997201919556})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.37219807505607605})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.34826308488845825})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.34007394313812256})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 52462], ['ood', 24061], ['id', 34968], ['id', 45580], ['ood', 56898]], 'labels': [9, -1, 8, 6, -1], 'scores': [0.9285954971412129, 1.7002870043658591, 2.2944060380037774, 2.711407577289182, 2.951424544047364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0136432647705078})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5902878046035767})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5410500764846802})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5441726446151733})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6055785417556763})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5855620503425598})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.53724205493927})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.676355242729187})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.575710117816925})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5729427933692932})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6106094121932983})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6861388683319092})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6766670942306519})
store['active_learning_steps'][29]['training']['best_epoch']=10
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.501104931640625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6559730768203735})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.49440526962280273})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4116963744163513})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4155644178390503})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.3739956021308899})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.36324310302734375})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3553239703178406})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3336581289768219})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.334322988986969})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.3551127314567566})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.33317190408706665})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.33930283784866333})
store['active_learning_steps'][29]['eval_training']['best_epoch']=9
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 52851], ['id', 42878], ['id', 51180], ['id', 15701], ['ood', 55521]], 'labels': [2, 8, 7, 3, -1], 'scores': [0.8140176785341025, 1.5794469269437164, 2.1743184548784456, 2.5895000567544724, 2.817185813462455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0124770402908325})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.628148078918457})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6139679551124573})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6015355587005615})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5810481905937195})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6527333855628967})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6603421568870544})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.489798828125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6480666399002075})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5109405517578125})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4497554302215576})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4172205626964569})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.40740787982940674})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.39580804109573364})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 47603], ['id', 29303], ['id', 56695], ['id', 14581], ['id', 19330]], 'labels': [2, 8, 5, 7, 6], 'scores': [0.770644556406135, 1.477243776740914, 2.06572795904603, 2.46952685699358, 2.7255551167760244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8294309973716736})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5292428135871887})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5019888877868652})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5202223658561707})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5124683976173401})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6625901460647583})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5520341396331787})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5549965500831604})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5828122496604919})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5660760402679443})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.451438037109375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6146330833435059})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4374529719352722})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3762359023094177})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3627290427684784})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3553720712661743})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.317080557346344})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3413585424423218})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.333892822265625})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34889015555381775})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 37383], ['id', 17382], ['id', 24899], ['ood', 27465], ['id', 2810]], 'labels': [3, 6, 3, -1, 8], 'scores': [0.8572778092893207, 1.5569031145984473, 2.0939393330750153, 2.456457410785573, 2.665014692433936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8956961035728455})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4758002758026123})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44390004873275757})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46351873874664307})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5244754552841187})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4676876664161682})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.498756468296051})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46177035570144653})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6023209095001221})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47050994634628296})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9366, 'crossentropy': 0.493611767578125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.572494626045227})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4318910241127014})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3912009000778198})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3858526945114136})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3396824300289154})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3284740447998047})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3250519037246704})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.31248751282691956})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3085448741912842})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 4945], ['id', 53666], ['id', 12070], ['id', 26937], ['id', 41744]], 'labels': [7, 7, 4, 0, 1], 'scores': [0.9120876165818645, 1.6566739304697538, 2.2666791759253537, 2.704850620894411, 2.946449602443513]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9185510277748108})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5634730458259583})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4532283842563629})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49584144353866577})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.488924115896225})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5502844452857971})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.432218115234375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6473054885864258})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4972612261772156})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4630928039550781})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43615061044692993})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.40351420640945435})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 42703], ['id', 52169], ['id', 48344], ['id', 43278], ['id', 9324]], 'labels': [0, 2, 9, 4, 3], 'scores': [0.6311852083446672, 1.2155185319613606, 1.711139364433297, 2.054344935381791, 2.2607915257382443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9856692552566528})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.552859902381897})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48218053579330444})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5431397557258606})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46357443928718567})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4926348328590393})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4850437641143799})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4937385320663452})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5875488519668579})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6060841083526611})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5173561573028564})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.43992880859375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5771881341934204})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.44791388511657715})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.35030725598335266})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3424413204193115})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.33831357955932617})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30260583758354187})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3131391406059265})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3012434244155884})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2904781699180603})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 41108], ['id', 18398], ['id', 29672], ['id', 48975], ['id', 56228]], 'labels': [0, 4, 9, 2, 3], 'scores': [0.8414782509555867, 1.5788626507791936, 2.1577069626538457, 2.545527838724828, 2.769233369821805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8903032541275024})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5205539464950562})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4853402376174927})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.475063681602478})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5220258235931396})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4587271511554718})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5350192785263062})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.439945361328125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6124899387359619})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4434773027896881})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4424101710319519})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37398138642311096})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3751341700553894})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33245235681533813})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 27998], ['id', 49282], ['ood', 5905], ['ood', 14130], ['id', 17739]], 'labels': [-1, 2, -1, -1, 5], 'scores': [0.7276100868779052, 1.3922818067410727, 1.90964065254534, 2.307727548760072, 2.5568465398634803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0212481021881104})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5439841747283936})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48469704389572144})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48917943239212036})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4978382885456085})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5002315044403076})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46029427647590637})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4928198456764221})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4742355942726135})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5191707611083984})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47891148924827576})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5404381155967712})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5614539384841919})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4921504259109497})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5557703971862793})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5308067798614502})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5444160103797913})
store['active_learning_steps'][36]['training']['best_epoch']=14
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9474, 'crossentropy': 0.489855859375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5982921123504639})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43525415658950806})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35632073879241943})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3488093316555023})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3286861777305603})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.2945740222930908})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.2986104488372803})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3018032908439636})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.29127997159957886})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.2901829481124878})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.27457600831985474})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.302346408367157})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3078351616859436})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2964687943458557})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.27264171838760376})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27850478887557983})
store['active_learning_steps'][36]['eval_training']['best_epoch']=16
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 47401], ['id', 13016], ['id', 33928], ['ood', 38890], ['id', 1461]], 'labels': [8, 8, 5, -1, 4], 'scores': [0.8949878959458393, 1.7137313238934606, 2.3489711459391787, 2.782336286455026, 3.0375803710882554]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8965449333190918})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4987342059612274})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4944918155670166})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4419485330581665})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5163666605949402})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5113655924797058})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5066258311271667})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9422, 'crossentropy': 0.4113888671875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6636723279953003})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47295013070106506})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3869894742965698})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3776974678039551})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3515207767486572})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3437574505805969})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 7933], ['id', 36818], ['id', 11514], ['id', 19948], ['id', 6227]], 'labels': [2, 7, 0, 8, 0], 'scores': [0.7692784719741188, 1.4538986520891815, 2.004068694451515, 2.363482052180788, 2.585775122089954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1319090127944946})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5361407995223999})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4744063913822174})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4543183147907257})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4644414782524109})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45761752128601074})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.470599889755249})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44368094205856323})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48186638951301575})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9471, 'crossentropy': 0.428164306640625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5857005715370178})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.433334082365036})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3744467496871948})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35984909534454346})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3622720241546631})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.33116719126701355})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3174564838409424})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3356664180755615})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 40530], ['id', 4646], ['id', 40775], ['id', 18041], ['id', 52858]], 'labels': [2, 2, 6, 8, 6], 'scores': [0.7727194220149471, 1.473016735003688, 2.047415616784046, 2.4527748612154, 2.697067315153409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0894839763641357})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5787234306335449})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4363846480846405})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43234556913375854})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4688432514667511})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4286109507083893})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.43341708984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6307958364486694})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49531838297843933})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4201098084449768})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3926607370376587})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37681180238723755})
store['active_learning_steps'][39]['eval_training']['best_epoch']=4
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 37048], ['id', 28040], ['ood', 15738], ['id', 51987], ['id', 20659]], 'labels': [9, 5, -1, 3, 1], 'scores': [0.6094223418612579, 1.1500009461241314, 1.6190171456427054, 1.9881237280319581, 2.254059732778228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0600765943527222})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5389502048492432})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4632274806499481})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4701073169708252})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4700480103492737})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45918112993240356})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.476471483707428})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4372546076774597})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9491, 'crossentropy': 0.4076476318359375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6291919946670532})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.49790823459625244})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42752113938331604})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3592940866947174})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3511396050453186})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.32024386525154114})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3215126395225525})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 13969], ['id', 24927], ['id', 20226], ['ood', 56420], ['id', 8763]], 'labels': [3, 9, 7, -1, 0], 'scores': [0.810425251408391, 1.488956517933532, 2.008973670651823, 2.3759305830942443, 2.613852912767907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.03035569190979})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5262781381607056})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43953222036361694})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43890902400016785})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4537927508354187})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4848160147666931})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4811094105243683})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.3920832763671875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6192946434020996})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4568246901035309})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3883969485759735})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.39947518706321716})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3607853055000305})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35502904653549194})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 14655], ['id', 1674], ['id', 31312], ['id', 34665], ['id', 57764]], 'labels': [3, 9, 9, 9, 6], 'scores': [0.7957338699846435, 1.468678049746238, 1.948491863449239, 2.278271916921671, 2.4996883658083924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9956962466239929})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5261552929878235})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4223805069923401})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4070631265640259})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.386780321598053})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4283197522163391})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4620789885520935})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42231038212776184})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4326832890510559})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3962506055831909})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4685359001159668})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.49497976899147034})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4360547959804535})
store['active_learning_steps'][42]['training']['best_epoch']=10
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.401326318359375}
