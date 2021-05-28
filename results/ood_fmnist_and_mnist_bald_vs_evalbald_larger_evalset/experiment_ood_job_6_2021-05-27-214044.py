store = {}
store['timestamp']=1622148044
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=6']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=40
store['config']={'seed': 1240, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.504277229309082})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3698782920837402})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.887885570526123})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.925203800201416})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6962, 'crossentropy': 2.0238193359375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47605], ['id', 25309], ['id', 39253], ['id', 23391], ['id', 14756]], 'labels': [3, 2, 5, 8, 1], 'scores': [1.2288501092507274, 2.2190279691132253, 3.0167778334820605, 3.581292603806382, 3.9701372706909916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.7971200942993164})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.353976011276245})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.0070533752441406})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.446533679962158})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.7206106185913086})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.8368430137634277})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6412, 'crossentropy': 2.8017271484375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 42035], ['id', 59275], ['id', 11794], ['id', 43375], ['id', 5063]], 'labels': [9, 3, 0, 4, 9], 'scores': [1.1824119094684118, 2.2052012025488663, 3.0017196912402877, 3.5769165215761953, 3.975771245772913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.695098400115967})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.0204763412475586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9034218788146973})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.674943208694458})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.700860023498535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.778160572052002})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6589, 'crossentropy': 2.6238552734375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 12281], ['id', 13587], ['id', 8299], ['id', 34332], ['id', 39329]], 'labels': [2, 6, 8, 9, 3], 'scores': [1.2267546006150094, 2.2865078498258953, 3.154334910458225, 3.7278303772616983, 4.074803509908559]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.195737361907959})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3152952194213867})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.6201181411743164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.3856289386749268})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.5340704917907715})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.131509304046631})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.331881046295166})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.966663360595703})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2861766815185547})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.7941675186157227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.3924200534820557})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.851417064666748})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 3.0605297088623047})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.211972713470459})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 3.1630964279174805})
store['active_learning_steps'][3]['training']['best_epoch']=12
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7164, 'crossentropy': 2.444961328125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 3026], ['id', 48748], ['id', 13030], ['id', 48096], ['id', 29872]], 'labels': [8, 2, 0, 7, 6], 'scores': [1.3165939342222166, 2.4253181293007415, 3.308764902406031, 3.87296623019488, 4.205312307833694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.6606521606445312})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.0940418243408203})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.145486831665039})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.408249855041504})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.6645760536193848})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.710383892059326})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.3355979919433594})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7123, 'crossentropy': 2.1810962890625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 34780], ['id', 21527], ['id', 7895], ['id', 46658], ['id', 483]], 'labels': [4, 2, 2, 8, 7], 'scores': [1.1844159540378167, 2.2500749321118656, 3.127226731252134, 3.702045020246251, 4.067577928371932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.589383840560913})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.884868860244751})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.844055414199829})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.8385570049285889})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.9383798837661743})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.208894729614258})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 2.4607629776000977})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.6571202278137207})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7693, 'crossentropy': 1.7484146484375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 43176], ['id', 12947], ['id', 55496], ['id', 36234], ['id', 57441]], 'labels': [2, 0, 9, 7, 3], 'scores': [1.1763272502008761, 2.2016574414592895, 3.0246566441438834, 3.6579036755870096, 4.064889047015004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.2601919174194336})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3996024131774902})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.6466467380523682})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.9020731449127197})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.8735244274139404})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8003, 'crossentropy': 1.21980458984375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 26069], ['id', 51176], ['id', 2659], ['id', 44502], ['id', 58471]], 'labels': [5, 5, 7, 2, 5], 'scores': [1.1122056515034857, 2.079155971532696, 2.882476441343239, 3.4700587870686324, 3.886374837909046]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1284409761428833})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.3376344442367554})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5938031673431396})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5790457725524902})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.6086312532424927})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.8775359392166138})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.7915058135986328})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.74554443359375})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8237, 'crossentropy': 1.41267939453125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 20150], ['id', 49525], ['id', 51414], ['id', 7768], ['id', 59468]], 'labels': [3, 8, 8, 8, 7], 'scores': [1.2299369123515045, 2.3201322801303, 3.1608301248226436, 3.742651367924924, 4.109368115020165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0185964107513428})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1732423305511475})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1845521926879883})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2149709463119507})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3735857009887695})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.347110390663147})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3213955163955688})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8438, 'crossentropy': 1.07506259765625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 7885], ['id', 29834], ['id', 53912], ['id', 33222], ['id', 10070]], 'labels': [5, 5, 4, 5, 9], 'scores': [1.2386591012905677, 2.247214143850346, 3.105479104099228, 3.712098654729692, 4.096961416339032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.100259780883789})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3064968585968018})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.4338998794555664})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4963483810424805})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.6748619079589844})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5449213981628418})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 2.007861614227295})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8364, 'crossentropy': 1.28590087890625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 59783], ['id', 44732], ['id', 43574], ['id', 50090], ['id', 37974]], 'labels': [1, 6, 5, 4, 2], 'scores': [1.2291839181768225, 2.241257285177978, 3.0440182098018367, 3.6457994926383126, 4.045224973105245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8964297771453857})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9126293659210205})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9805428981781006})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0047564506530762})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.037447214126587})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0710961818695068})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1442052125930786})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.182776927947998})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.874, 'crossentropy': 0.86743779296875}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 57599], ['id', 11708], ['id', 34520], ['id', 40575], ['id', 54191]], 'labels': [-1, 3, 6, 3, 3], 'scores': [1.1317636131657947, 2.138498155576234, 2.99050662381093, 3.6359456169023785, 4.0503152555060336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9363771677017212})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8936383724212646})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0231072902679443})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0327999591827393})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0356472730636597})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8845, 'crossentropy': 0.73561044921875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 50052], ['id', 49593], ['id', 11304], ['id', 11377], ['id', 9403]], 'labels': [2, 6, 0, 3, 3], 'scores': [0.9658232170942087, 1.8375257339400686, 2.5930689408284664, 3.191864750730968, 3.650108457282113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8734791278839111})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8054298758506775})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.842301607131958})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8763520121574402})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.938554584980011})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0394773483276367})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8891, 'crossentropy': 0.7066455078125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 23104], ['id', 8339], ['id', 18487], ['id', 3524], ['id', 44466]], 'labels': [0, 5, 4, 6, 4], 'scores': [1.0691504692076954, 2.0184511813489316, 2.815475936495126, 3.4414649938549626, 3.8896949385237978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9276622533798218})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8302326202392578})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9058730006217957})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9273932576179504})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9789261221885681})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9842078685760498})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0318886041641235})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1472736597061157})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.777175830078125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 42703], ['id', 59747], ['id', 59983], ['id', 57474], ['id', 1364]], 'labels': [0, 5, 2, 3, 9], 'scores': [1.243573584463062, 2.2821373004038765, 3.129107827136899, 3.7304901913598885, 4.119777625832887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9538319110870361})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8652136325836182})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8190212845802307})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9609706997871399})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9419349431991577})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0177934169769287})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8908, 'crossentropy': 0.734044580078125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 32880], ['id', 56662], ['id', 12984], ['id', 41002], ['id', 23140]], 'labels': [0, 0, 8, 7, 7], 'scores': [1.0216893663163473, 1.966103543565604, 2.753631308794832, 3.362910805334348, 3.7920703225842534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9067870378494263})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8084813356399536})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8527289032936096})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8630450963973999})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9214439392089844})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0021928548812866})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0549014806747437})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.68499755859375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 33162], ['id', 26072], ['id', 43796], ['id', 21700], ['id', 23546]], 'labels': [8, 1, 7, 7, 5], 'scores': [1.1010751842857036, 2.0590956481547646, 2.882852816931294, 3.511734024986602, 3.95563310114232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9270458221435547})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7897657155990601})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8322207927703857})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8427000045776367})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8573979735374451})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8266845941543579})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8644168972969055})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.686504541015625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 6604], ['id', 13516], ['id', 28633], ['id', 55034], ['id', 37048]], 'labels': [8, 3, 3, 7, 9], 'scores': [1.1431407242057483, 2.1354215846975433, 2.9592999498116717, 3.5834477976072128, 4.005033248988077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.812621533870697})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7891076803207397})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7426352500915527})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8516332507133484})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7999094724655151})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8674176931381226})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8281855583190918})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9676907658576965})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.656316259765625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 44095], ['id', 26850], ['id', 29132], ['id', 45056], ['id', 54573]], 'labels': [2, 2, 8, 8, 2], 'scores': [1.0790297653348082, 2.0925607566746054, 2.994087088182786, 3.631094580001162, 4.02973503656405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0542147159576416})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8153489828109741})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8706080913543701})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.757271945476532})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7662789821624756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.811896026134491})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9027976393699646})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8918, 'crossentropy': 0.677604052734375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 7232], ['id', 19942], ['ood', 52889], ['id', 16511], ['id', 51081]], 'labels': [5, 5, -1, 5, 4], 'scores': [1.175420906646326, 2.206664996577384, 2.9877098277541583, 3.5627683593214368, 3.9617759005860362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8851120471954346})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.708648681640625})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.717557966709137})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7202492356300354})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7930796146392822})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7555265426635742})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9028, 'crossentropy': 0.63374482421875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 56427], ['id', 42078], ['id', 59731], ['id', 45602], ['id', 18572]], 'labels': [2, 4, 5, 5, 0], 'scores': [1.0286443664053047, 1.9995602019358616, 2.7635378658979866, 3.3544798055381477, 3.7850739001585954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0401370525360107})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7377720475196838})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7411285638809204})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8160796761512756})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7637530565261841})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8068034052848816})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.643433935546875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 47741], ['id', 8443], ['id', 57728], ['id', 11292], ['id', 14335]], 'labels': [5, 2, 9, 1, 4], 'scores': [0.9607576319335727, 1.835675224399727, 2.6226133437749137, 3.243644123424067, 3.7037480871619195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9773346185684204})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.768456220626831})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.696643590927124})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8157181739807129})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8034603595733643})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8260495066642761})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8018960952758789})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8772818446159363})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9043, 'crossentropy': 0.6442154296875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 42799], ['id', 5474], ['id', 38158], ['id', 7559], ['id', 40312]], 'labels': [2, 8, 8, 6, 0], 'scores': [1.0901278089502533, 2.0615402568587635, 2.8552748721034487, 3.4788408478506696, 3.9081866109791568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1540255546569824})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7722444534301758})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.726238489151001})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7248599529266357})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7689998149871826})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7817081212997437})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8166472911834717})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.650662109375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 2381], ['id', 51337], ['id', 13831], ['id', 44570], ['id', 8047]], 'labels': [7, 4, 3, 7, 8], 'scores': [1.1060549576682712, 2.098332153638873, 2.9466990280271492, 3.569562365558479, 3.968723725655005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9214522838592529})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.670447587966919})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.649446964263916})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7228667736053467})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6737855672836304})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.591014697265625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 22083], ['id', 17756], ['id', 4797], ['id', 5684], ['id', 966]], 'labels': [2, 8, 8, 6, 3], 'scores': [0.8784999203978714, 1.6227937173444822, 2.2715932036068134, 2.834582717911964, 3.2790429747183936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.179795742034912})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7588833570480347})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7301273345947266})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7002675533294678})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7424569129943848})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6794096827507019})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8217170834541321})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.676325830078125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 34524], ['id', 14697], ['id', 49893], ['id', 50369], ['id', 20091]], 'labels': [8, 8, 3, 3, 5], 'scores': [1.0581321329356175, 2.001092495291461, 2.8119790696466236, 3.4314704223724117, 3.8827818567534225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.190429449081421})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6865423917770386})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6385003328323364})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6893632411956787})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7679187059402466})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7981753349304199})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.5815876953125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 1239], ['id', 31624], ['id', 17712], ['id', 26788], ['id', 18324]], 'labels': [8, 9, 3, 2, 0], 'scores': [0.9585675175836554, 1.7691720197295355, 2.4979770321990804, 3.0844845357370607, 3.562496681846836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2012298107147217})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7253798246383667})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6442979574203491})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7033054828643799})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7252112030982971})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8202208280563354})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.59547880859375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 53873], ['id', 26376], ['id', 40334], ['id', 30144], ['id', 26358]], 'labels': [4, 1, 4, 9, 3], 'scores': [0.9373021222445539, 1.7857012754460442, 2.5373323618183443, 3.162872809538884, 3.6131722129305484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1095184087753296})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7003803253173828})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6912491321563721})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7041839361190796})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6910344362258911})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7625505328178406})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7468187212944031})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7058306932449341})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6626696586608887})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.729801595211029})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.624562109375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 52169], ['id', 12305], ['id', 46368], ['id', 42444], ['ood', 52889]], 'labels': [2, 9, 8, 0, -1], 'scores': [1.1147108011566567, 2.133282437029499, 2.98005076598527, 3.612393822331133, 4.032809122218898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2309579849243164})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6430480480194092})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6261899471282959})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6415623426437378})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6530110836029053})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.681849479675293})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6145143508911133})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.755416989326477})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6701000928878784})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7319316864013672})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.57769736328125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 43648], ['id', 34406], ['id', 1518], ['id', 31608], ['id', 31090]], 'labels': [5, 4, 9, 2, 4], 'scores': [1.1482707902229605, 2.198252673335955, 3.0477506031142587, 3.653564072857396, 4.06061071794308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1916751861572266})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.765386700630188})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7190296649932861})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7174593210220337})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7336952090263367})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7554821372032166})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8061904907226562})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7987006902694702})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8086082935333252})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8215396404266357})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7999616265296936})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8818460702896118})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.694992822265625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 17518], ['id', 39208], ['id', 4822], ['id', 9966], ['id', 28632]], 'labels': [0, 5, 4, 0, 7], 'scores': [1.181864812482329, 2.2645656033128394, 3.136971181360787, 3.7832282947492253, 4.158742883123581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.168173909187317})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7719242572784424})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7121423482894897})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7129725217819214})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.772392988204956})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7319175004959106})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9072, 'crossentropy': 0.62749716796875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 8932], ['id', 43532], ['id', 51759], ['id', 13428], ['id', 33538]], 'labels': [0, 8, 3, 9, 0], 'scores': [0.8579683917751959, 1.653024846573996, 2.3660313805607824, 2.9638221183087303, 3.4295913012250256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1316511631011963})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7355479598045349})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.686672568321228})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7106841802597046})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.778628945350647})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7025913000106812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6865063905715942})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7043849229812622})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6797953844070435})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8009552955627441})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7357485890388489})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8274903893470764})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.59733896484375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 34328], ['id', 46316], ['id', 59344], ['id', 42428], ['id', 47288]], 'labels': [8, 9, 9, 5, 6], 'scores': [1.0742475598288042, 2.0665444244016564, 2.913577929337224, 3.5445117096276704, 3.9715114628177712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2220616340637207})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7109668254852295})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.580176591873169})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5406489372253418})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6113258004188538})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6210440397262573})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5997723340988159})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6147623062133789})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5948619842529297})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6702466011047363})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7004647850990295})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.637717604637146})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.53638447265625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 19590], ['id', 8704], ['id', 32776], ['id', 2761], ['id', 27292]], 'labels': [5, 1, 4, 8, 7], 'scores': [1.185003491668164, 2.277459808366917, 3.1265095009066224, 3.714499706197195, 4.104349402788488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.025026798248291})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6173619627952576})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5689126253128052})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6376547813415527})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6350185871124268})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6293895244598389})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.50628837890625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 56440], ['id', 35401], ['id', 1642], ['id', 9147], ['id', 22497]], 'labels': [4, 3, 6, 4, 7], 'scores': [0.9342235889555093, 1.7340032105106173, 2.4517264407407, 3.040310376956569, 3.506457010295171]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2130073308944702})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6910288333892822})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5969165563583374})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5925956964492798})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5400301218032837})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.586396336555481})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6037951707839966})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6211681962013245})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.941, 'crossentropy': 0.450408984375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 54024], ['id', 20869], ['id', 53872], ['id', 1423], ['id', 9340]], 'labels': [5, 3, 8, 0, 5], 'scores': [0.963562899024279, 1.8639564739300227, 2.6805939949428392, 3.3026826657080726, 3.767859449053251]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3540804386138916})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.796141505241394})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6923742294311523})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6018792986869812})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6269518136978149})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.585205078125})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6671426296234131})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6243794560432434})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7171951532363892})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7009767889976501})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7037078142166138})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.54589814453125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 25508], ['id', 53156], ['ood', 9238], ['id', 39943], ['id', 36818]], 'labels': [5, 3, -1, 4, 7], 'scores': [1.0849139769474578, 2.0984730504999414, 2.9398914127785813, 3.586734158669314, 4.006883711817164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1746199131011963})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6319082975387573})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5152294039726257})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5913887023925781})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5721699595451355})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5691689252853394})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.942, 'crossentropy': 0.47199375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 33338], ['id', 16628], ['id', 59681], ['id', 57575], ['id', 43126]], 'labels': [8, 9, 0, 0, 3], 'scores': [0.8788596237461177, 1.636421886228964, 2.323652011790317, 2.8953054034511725, 3.3484058477561263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3998658657073975})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7049247026443481})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5668962597846985})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6843931674957275})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5756497383117676})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5473635196685791})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.520736575126648})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5263509750366211})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5910005569458008})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5254226326942444})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5610616207122803})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5631909370422363})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5516630411148071})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9512, 'crossentropy': 0.46287880859375}
