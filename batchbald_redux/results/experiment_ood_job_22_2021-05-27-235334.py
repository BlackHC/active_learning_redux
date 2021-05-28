store = {}
store['timestamp']=1622156014
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=22']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=22
store['worker_id']=22
store['num_workers']=40
store['config']={'seed': 1258, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.18837571144104})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.682811737060547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9211511611938477})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.765324592590332})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.182021141052246})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.3784642219543457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.1261658668518066})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9751229286193848})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.1791164875030518})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.225358486175537})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9508047103881836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.2043380737304688})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.981916904449463})
store['active_learning_steps'][0]['training']['best_epoch']=10
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6903, 'crossentropy': 2.748106640625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 23859], ['id', 42172], ['id', 3258], ['id', 57632], ['id', 17817]], 'labels': [2, 6, 3, 2, 9], 'scores': [1.3372408314946194, 2.440099468442324, 3.278667977427994, 3.832942492525511, 4.172971674825004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.273730516433716})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.646239757537842})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1015639305114746})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.213998794555664})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6701, 'crossentropy': 2.0580822265625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 50802], ['id', 56664], ['id', 53571], ['id', 47683], ['id', 14749]], 'labels': [2, 2, 2, 5, 0], 'scores': [1.1369627216152258, 2.0657664968614124, 2.8221600449217137, 3.3995894630750323, 3.7941125409482117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.3265693187713623})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.5062196254730225})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.8110172748565674})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.7265331745147705})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.6475424766540527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6268608570098877})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8787927627563477})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.5096356868743896})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.031456470489502})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.8524832725524902})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.9382247924804688})
store['active_learning_steps'][2]['training']['best_epoch']=8
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7147, 'crossentropy': 2.3076080078125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 7843], ['id', 26208], ['id', 43362], ['id', 54461], ['id', 47089]], 'labels': [4, 3, 7, 5, 4], 'scores': [1.2548487500298573, 2.386340802130955, 3.25431986105572, 3.8502780217661154, 4.196682606959605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8405754566192627})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.069929838180542})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.203338623046875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4758830070495605})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.168653964996338})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.064211130142212})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 3.0075082778930664})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.589668035507202})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.6960294246673584})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7488, 'crossentropy': 1.9191537109375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 25919], ['id', 12157], ['id', 42573], ['id', 9499], ['id', 43212]], 'labels': [0, 5, 7, 7, 5], 'scores': [1.2228225796135457, 2.2999918690479233, 3.18606570907604, 3.771738751159205, 4.140617659828131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.8685909509658813})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.1167471408843994})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.2858099937438965})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.6415958404541016})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.5560073852539062})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7378, 'crossentropy': 1.9357984375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 8661], ['id', 18527], ['id', 38404], ['id', 49034], ['id', 16051]], 'labels': [8, 3, 0, 2, 4], 'scores': [1.1566829601871447, 2.1901756366236045, 3.046792265120869, 3.6802324179850086, 4.052172601735432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4903717041015625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.8326833248138428})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8228883743286133})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.1530063152313232})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.1764631271362305})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7909, 'crossentropy': 1.53328046875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 59361], ['id', 26444], ['id', 44850], ['id', 4290], ['id', 20089]], 'labels': [8, 1, 4, 5, 8], 'scores': [1.1851883647495702, 2.1931501312143276, 3.0392074087609915, 3.6405499761715054, 4.042753385425842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5016741752624512})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.6581292152404785})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.8579961061477661})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.3412485122680664})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.222902297973633})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7761, 'crossentropy': 1.56702119140625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 4767], ['id', 5679], ['id', 2118], ['id', 3370], ['id', 23435]], 'labels': [8, 3, 7, 4, 4], 'scores': [1.1171109350463437, 2.103088391577005, 2.938235094027818, 3.583857632191253, 3.9797729882689277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6509994268417358})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6703159809112549})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.9654877185821533})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.1618242263793945})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.1029064655303955})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.9468567371368408})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.0405027866363525})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.3851888179779053})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.3591647148132324})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.19221830368042})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.1805248260498047})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.168036937713623})
store['active_learning_steps'][7]['training']['best_epoch']=9
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7861, 'crossentropy': 1.9433548828125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 23104], ['id', 50010], ['id', 15679], ['id', 27632], ['id', 56348]], 'labels': [0, 5, 2, 7, 9], 'scores': [1.2987350745577841, 2.4627183949867764, 3.3749670522481505, 3.977198968204158, 4.291438161749907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1670030355453491})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.306114912033081})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.520938754081726})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.6080467700958252})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.7555623054504395})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8103, 'crossentropy': 1.0678533203125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 40208], ['id', 3051], ['id', 28313], ['id', 18398], ['id', 9428]], 'labels': [0, 3, 9, 4, 9], 'scores': [1.0208671567104144, 1.9195859958579757, 2.685433581481398, 3.3011288114749266, 3.75088737769216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.175835371017456})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.3539068698883057})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.5457221269607544})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.509321689605713})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.6348068714141846})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8123, 'crossentropy': 1.13655478515625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 17756], ['id', 49537], ['id', 39627], ['id', 15250], ['id', 40642]], 'labels': [8, 2, 2, 3, 6], 'scores': [1.2011404595497024, 2.109691760382895, 2.8912165584231353, 3.4949564738626338, 3.9126041855619302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.174245834350586})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.3217558860778809})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.5001451969146729})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4044253826141357})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3804664611816406})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.693683385848999})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6699180603027344})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8337, 'crossentropy': 1.1683798828125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 45077], ['id', 33505], ['id', 28183], ['id', 25384], ['id', 53656]], 'labels': [2, 2, 9, 5, 2], 'scores': [1.184991343503746, 2.144201801063109, 3.0017815182767986, 3.619392770319985, 4.019837901241679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0268617868423462})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2304959297180176})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2898545265197754})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2813814878463745})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3184237480163574})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4683680534362793})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.4860211610794067})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.327552080154419})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4973793029785156})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.558436393737793})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6058907508850098})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8502, 'crossentropy': 1.1378779296875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 42121], ['id', 52801], ['id', 7923], ['id', 50750], ['id', 39561]], 'labels': [5, 2, 8, 0, 2], 'scores': [1.2620787023048705, 2.3305564039623996, 3.1967046466955953, 3.770201567526624, 4.151789782360266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0987786054611206})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0727038383483887})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1519211530685425})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.296083927154541})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.663143515586853})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8429, 'crossentropy': 0.9401740234375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 19942], ['id', 1019], ['id', 13652], ['id', 51903], ['id', 48824]], 'labels': [5, 7, 9, 3, 8], 'scores': [1.031090498982358, 1.9429925793024454, 2.737043512558415, 3.3397050546221667, 3.76464851337858]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1001787185668945})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0986953973770142})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1009202003479004})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3749408721923828})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3189198970794678})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.4468605518341064})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8494, 'crossentropy': 0.9996595703125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37507], ['id', 40595], ['id', 1674], ['id', 12497], ['id', 5728]], 'labels': [5, 8, 9, 0, 3], 'scores': [1.1077277278494715, 2.100435826213417, 2.928229866885501, 3.564626847506984, 3.9655780821866102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9864874482154846})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9520930051803589})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0856225490570068})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1630330085754395})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1824676990509033})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8511, 'crossentropy': 0.8533271484375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 36508], ['id', 17083], ['id', 23901], ['id', 33594], ['id', 11586]], 'labels': [5, 6, 9, 3, 8], 'scores': [0.9802579029522229, 1.8636169634079378, 2.5831002275038024, 3.1710246012341967, 3.61432049145837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8613460063934326})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8614197969436646})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8541141748428345})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8143909573554993})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8785548210144043})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9663905501365662})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9417691230773926})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8818, 'crossentropy': 0.8057576171875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 42787], ['id', 36810], ['id', 44202], ['id', 33388], ['id', 49519]], 'labels': [4, 6, 8, 8, 1], 'scores': [1.1249069377499201, 2.1164434536759504, 2.920903321809539, 3.535682392908315, 3.935054871866148]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9446744918823242})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.68622225522995})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7137579917907715})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.721937894821167})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.70848548412323})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7665641903877258})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7821370363235474})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.751227617263794})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7828876972198486})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7459980249404907})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.70143349609375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 33812], ['id', 39355], ['id', 18739], ['id', 15948], ['id', 21023]], 'labels': [6, 8, 3, 2, 2], 'scores': [1.2257261346381447, 2.2657395833965346, 3.1246035370609864, 3.734311163485172, 4.124794617979106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.059514045715332})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6550760269165039})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5944637060165405})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6584737300872803})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6715354919433594})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.747221827507019})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.59241845703125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 4761], ['id', 10210], ['id', 20547], ['id', 11621], ['id', 34520]], 'labels': [8, 3, 5, 2, 6], 'scores': [1.0192839613040752, 1.9242280537313183, 2.7191365544762505, 3.328133105467126, 3.7676173173753353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0400497913360596})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.721832275390625})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6837747097015381})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7266098260879517})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6972543001174927})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7275447845458984})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6677321195602417})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7857171297073364})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.78050696849823})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.909, 'crossentropy': 0.707112548828125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 25332], ['id', 31847], ['id', 39429], ['id', 46368], ['id', 36818]], 'labels': [2, 8, 2, 8, 7], 'scores': [1.1619146753715879, 2.2090864914992867, 3.097502839095581, 3.697452807665943, 4.066835500921613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0110509395599365})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6899139881134033})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6742532253265381})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7341755628585815})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.753788948059082})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7970361709594727})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7807680368423462})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8030551671981812})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7074164748191833})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8819054961204529})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7678182125091553})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6717644929885864})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7493219375610352})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8002023696899414})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7306679487228394})
store['active_learning_steps'][19]['training']['best_epoch']=12
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.619994873046875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 51081], ['id', 52462], ['id', 5013], ['id', 9472], ['id', 58829]], 'labels': [4, 9, 2, 2, 0], 'scores': [1.2288051171399001, 2.292702632735547, 3.158565071787235, 3.7706338743132264, 4.142061802487392]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.963090181350708})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.678530216217041})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6951731443405151})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6715524196624756})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6871472597122192})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7224579453468323})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7409648299217224})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7211521863937378})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6621809005737305})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7656902074813843})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7291951775550842})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7448393106460571})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8700960874557495})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8585382699966431})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8919819593429565})
store['active_learning_steps'][20]['training']['best_epoch']=12
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.71582724609375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 19254], ['id', 13021], ['id', 44196], ['id', 43048], ['id', 24424]], 'labels': [9, 5, 8, 5, 1], 'scores': [1.2602804071255118, 2.394147965160483, 3.307797568243231, 3.8974306745337577, 4.24093191715684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0415585041046143})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7409951686859131})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.678840696811676})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7485055327415466})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7162809371948242})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6865881085395813})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8143554329872131})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.790390133857727})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7619215250015259})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.655814306640625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 53873], ['id', 18598], ['id', 7886], ['id', 37907], ['id', 49493]], 'labels': [4, 9, 9, 4, 8], 'scores': [1.0635526483672517, 2.002318603734903, 2.802648556096461, 3.4288811734274836, 3.876791427811856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1023002862930298})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.736447274684906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6955792307853699})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7679911255836487})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8047937154769897})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8752313256263733})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7380433678627014})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8056894540786743})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.891711950302124})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8012033104896545})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.739739599609375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 1282], ['id', 5259], ['id', 36408], ['id', 52049], ['id', 32276]], 'labels': [9, 2, 1, 6, 3], 'scores': [1.0967665466039977, 2.1111654283911014, 2.976516774956046, 3.623128683204298, 4.036721525281698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9473684430122375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6691025495529175})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6220851540565491})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6661389470100403})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6241335272789001})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6280226707458496})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6742472648620605})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.698209285736084})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9096, 'crossentropy': 0.62855595703125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 1024], ['id', 47260], ['id', 8214], ['id', 52169], ['ood', 26568]], 'labels': [5, 6, 7, 2, -1], 'scores': [1.0270055535263478, 1.9785927095926716, 2.799605544698844, 3.4148673813987225, 3.8524277491605297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9982746839523315})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6933767199516296})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.59443199634552})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6492867469787598})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6452077627182007})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7785954475402832})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.55476376953125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 7833], ['id', 14692], ['ood', 49218], ['id', 31562], ['ood', 2782]], 'labels': [5, 3, -1, 3, -1], 'scores': [1.0185126738779258, 1.884112468575105, 2.6348144770672075, 3.223985254211507, 3.6668095975979256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1839892864227295})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5969514846801758})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5985560417175293})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6490886211395264})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6709184646606445})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7053110003471375})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.5386369140625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 52358], ['id', 32776], ['id', 53062], ['id', 8449], ['id', 134]], 'labels': [2, 4, 4, 0, 1], 'scores': [0.9681555112393001, 1.8434812468324928, 2.5974364490427817, 3.183715784315159, 3.624944297320468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.1913704872131348})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.708650529384613})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.582748532295227})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6155821084976196})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6397583484649658})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6295819282531738})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6232845187187195})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6984022259712219})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6722342371940613})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9206, 'crossentropy': 0.558981396484375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 39480], ['id', 42438], ['id', 8207], ['id', 37696], ['id', 5155]], 'labels': [9, 9, 4, 2, 4], 'scores': [1.0654930866616292, 2.0295300959884273, 2.8280408290659285, 3.47278789641084, 3.913057163220752]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0969698429107666})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6889153718948364})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6320996880531311})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6231426000595093})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6451749801635742})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7108874320983887})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6820400953292847})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.550350927734375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 46132], ['id', 22083], ['id', 40304], ['id', 1642], ['id', 17389]], 'labels': [7, 2, 6, 6, 3], 'scores': [0.9948308263285424, 1.926115489218558, 2.7274784730016037, 3.343686007677647, 3.7885911295480703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1228976249694824})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6439756155014038})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5215240716934204})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5635783672332764})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5487431287765503})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.593327522277832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.512804388999939})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6886614561080933})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.52378955078125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 17941], ['id', 49890], ['ood', 53054], ['id', 39818], ['id', 3204]], 'labels': [0, 5, -1, 1, 5], 'scores': [1.0578536757869434, 1.970799470915944, 2.7536285540338783, 3.3856489211646714, 3.8256116068052286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0590267181396484})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.632158100605011})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5479787588119507})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5563902854919434})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5786893367767334})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.576846718788147})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47826075553894043})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5907077193260193})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6019909381866455})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6968899965286255})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9381, 'crossentropy': 0.46863271484375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 1075], ['id', 28512], ['id', 4822], ['id', 43126], ['id', 7406]], 'labels': [7, 5, 4, 3, 1], 'scores': [1.12261523093906, 2.1441769075716213, 2.994524701683525, 3.607171044890352, 4.015373274062384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.144988775253296})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5860840082168579})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5077767372131348})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.515869677066803})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5915377140045166})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5179364681243896})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.479198681640625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 53844], ['id', 1160], ['id', 48360], ['id', 7322], ['id', 32519]], 'labels': [5, 4, 3, 3, 5], 'scores': [0.9092150424147427, 1.7561267654447268, 2.4903445097915924, 3.1122495451052865, 3.5811457359311536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1932625770568848})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6220850944519043})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.540332019329071})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5603729486465454})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5624227523803711})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5109817981719971})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4845212697982788})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5599408149719238})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5985084772109985})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6889486908912659})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.492363525390625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 17739], ['id', 7768], ['id', 19886], ['id', 20150], ['id', 53029]], 'labels': [5, 8, 2, 3, 2], 'scores': [1.103690543936291, 2.0924649572046423, 2.942912501728319, 3.56911143291972, 3.994757372833699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1382838487625122})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5711709856987})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5267112851142883})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5051713585853577})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.609453022480011})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.52199387550354})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5850048065185547})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5629007816314697})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6247223019599915})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.62615567445755})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6554245948791504})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.528133154296875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 32173], ['id', 15723], ['id', 35401], ['id', 14697], ['id', 51144]], 'labels': [7, 8, 3, 8, 5], 'scores': [1.1437878704876305, 2.1453245719454177, 3.0027708891522007, 3.622473220814637, 4.035734516526878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1969382762908936})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7444232702255249})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5848464965820312})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5253061652183533})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5272469520568848})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5504669547080994})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6221225261688232})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5975808501243591})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.480545263671875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 46412], ['id', 36337], ['id', 44806], ['id', 50930], ['id', 35688]], 'labels': [0, 3, 8, 0, 3], 'scores': [0.9454314747961634, 1.8350494426957247, 2.5952780142636405, 3.228098656101629, 3.704272350852861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.300736665725708})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6655795574188232})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5802274942398071})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.569054126739502})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5825148820877075})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5552768707275391})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.639113187789917})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5882573127746582})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6326704621315002})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.508717529296875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 37048], ['id', 15832], ['id', 39942], ['id', 43745], ['id', 4153]], 'labels': [9, 9, 9, 8, 2], 'scores': [1.1588261640684765, 2.178974121681157, 3.021492436024592, 3.6452152568905642, 4.050075963584728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3319900035858154})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7425515651702881})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.565901517868042})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5728774070739746})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5246528387069702})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5442454814910889})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9332, 'crossentropy': 0.499268505859375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 43648], ['id', 58560], ['id', 31301], ['id', 50320], ['id', 33162]], 'labels': [5, 0, 5, 5, 8], 'scores': [0.845430716586042, 1.6529948077343368, 2.3640866773092553, 2.9538935055853965, 3.4174283907153864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3410890102386475})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7507386803627014})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6077061891555786})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5093064308166504})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6351159811019897})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6047853827476501})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6163723468780518})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.46927900390625}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 42113], ['id', 3810], ['id', 40466], ['id', 31124], ['id', 12936]], 'labels': [-1, 3, 8, 8, 8], 'scores': [0.9167148179129696, 1.777444907218014, 2.5295749538573133, 3.1374864009544847, 3.5846995974982327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.2974964380264282})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6131640672683716})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5295573472976685})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49676015973091125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5885671973228455})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5575311183929443})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.6288164854049683})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5203830003738403})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5408491492271423})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6004998683929443})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.557806134223938})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9374, 'crossentropy': 0.4945392578125}
