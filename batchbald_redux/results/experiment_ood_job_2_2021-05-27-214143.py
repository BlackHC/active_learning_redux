store = {}
store['timestamp']=1622148103
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=2']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=40
store['config']={'seed': 1236, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1934378147125244})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6525511741638184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6837615966796875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.813356637954712})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9517016410827637})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.724815845489502})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.8380250930786133})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.9290127754211426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.078594923019409})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.1395223140716553})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6974, 'crossentropy': 2.602639453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1511507034301758})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.144197940826416})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0867178440093994})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1157946586608887})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2072151899337769})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.146478295326233})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1265476942062378})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 15306], ['id', 9687], ['id', 30738], ['id', 9802], ['id', 49149]], 'labels': [5, 0, 8, 6, 3], 'scores': [1.218832646293913, 2.148006393881122, 2.8477132905825817, 3.271831943398416, 3.4961679157958434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.0516610145568848})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.4605226516723633})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.482154369354248})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.556952476501465})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7037, 'crossentropy': 1.9751818359375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1286934614181519})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0914618968963623})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0831339359283447})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 33064], ['id', 20169], ['id', 22530], ['id', 11492], ['id', 24713]], 'labels': [4, 4, 7, 5, 4], 'scores': [1.0110656605260846, 1.789038877340885, 2.389171818672871, 2.7999230475998367, 3.0225356192346027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.0838842391967773})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.285235643386841})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.8832132816314697})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.4883811473846436})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7222, 'crossentropy': 1.8000171875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1965835094451904})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1181553602218628})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0939452648162842})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 46707], ['id', 36717], ['id', 14697], ['id', 37760], ['id', 33759]], 'labels': [2, 2, 8, 2, 7], 'scores': [0.9002515214857074, 1.5990157654779056, 2.1802807324392957, 2.5932135957754516, 2.844770292472557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9081873893737793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.296675205230713})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.7759571075439453})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.342768669128418})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.6119871139526367})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.807823657989502})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.887589454650879})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7519, 'crossentropy': 2.088496484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9809976816177368})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9874938130378723})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9587322473526001})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0088781118392944})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 58469], ['id', 32591], ['id', 57315], ['id', 15366], ['id', 20330]], 'labels': [9, 8, 8, 8, 9], 'scores': [0.961203754802052, 1.7284831779777599, 2.279270504660511, 2.628708334423086, 2.832641237622596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3209564685821533})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.820434808731079})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.9665601253509521})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.9055559635162354})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7836, 'crossentropy': 1.2313181640625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.943220853805542})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.919869065284729})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.8780559301376343})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 10156], ['id', 13921], ['id', 4767], ['id', 34951], ['id', 16997]], 'labels': [1, 0, 8, 7, 0], 'scores': [0.7364212093323206, 1.4024034512169856, 1.9139540340142078, 2.255756862383005, 2.489969469317346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.114976167678833})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.416789174079895})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.589552640914917})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.8202414512634277})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8085, 'crossentropy': 1.0988037109375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8704220056533813})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.787726879119873})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7897788882255554})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 30378], ['id', 45797], ['id', 25321], ['id', 33798], ['id', 31962]], 'labels': [9, 5, 8, 7, 3], 'scores': [0.8636875787964184, 1.5447380155623347, 2.1249770221027457, 2.553059097289877, 2.8260691297835905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9792895317077637})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0848050117492676})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.14247727394104})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2093732357025146})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3579699993133545})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.343071699142456})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3220856189727783})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.42608642578125})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2895426750183105})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.369037389755249})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.3106420040130615})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.3366808891296387})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.2280521392822266})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.4224247932434082})
store['active_learning_steps'][6]['training']['best_epoch']=11
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8594, 'crossentropy': 1.21398017578125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7414604425430298})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6507648229598999})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6164274215698242})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.588023841381073})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.5861368179321289})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.5653128623962402})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6054182052612305})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 32760], ['id', 36320], ['id', 11734], ['id', 974], ['ood', 43952]], 'labels': [8, 8, 8, 9, -1], 'scores': [1.0703254724627052, 1.959846051677025, 2.6257665601376274, 3.0577116739786714, 3.3061520369731543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0642142295837402})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1353998184204102})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1602377891540527})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.462460994720459})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3655340671539307})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.6039485931396484})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8494, 'crossentropy': 1.110652734375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7001334428787231})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6909604072570801})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6211062073707581})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6143411993980408})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6150661706924438})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 2118], ['id', 27271], ['id', 57336], ['id', 400], ['ood', 11690]], 'labels': [7, 5, 3, 2, -1], 'scores': [1.0216529397017866, 1.8785963732819568, 2.50855119599923, 2.8746882877115993, 3.0680056312968578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0686900615692139})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.185415267944336})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2211188077926636})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.338430643081665})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3211100101470947})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.485974907875061})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8654, 'crossentropy': 0.9531380859375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7526916861534119})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6744461059570312})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6374328136444092})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.5749825835227966})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6077784299850464})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 44948], ['id', 18404], ['id', 20933], ['id', 59402], ['id', 17263]], 'labels': [9, 5, 5, 8, 2], 'scores': [0.8353867914705504, 1.6249587961214371, 2.1868345504402082, 2.5518314374279045, 2.753684848976871]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.935759961605072})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0400227308273315})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0819029808044434})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1521973609924316})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8474, 'crossentropy': 0.8781703125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.873551607131958})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7814198732376099})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7364084720611572})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 13030], ['id', 5442], ['id', 13460], ['id', 12514], ['id', 11619]], 'labels': [0, 3, 5, 2, 3], 'scores': [0.6532619388127023, 1.1969626213612692, 1.6797469542988157, 2.060714634713964, 2.3301583731552284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9672143459320068})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.112597942352295})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1449849605560303})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0615895986557007})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1510587930679321})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.3400559425354004})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1914151906967163})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.250058650970459})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.4679975509643555})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.3137485980987549})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.323204517364502})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.528056025505066})
store['active_learning_steps'][10]['training']['best_epoch']=9
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8721, 'crossentropy': 1.1239517578125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7325804233551025})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6100597381591797})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6026010513305664})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.578097939491272})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5751365423202515})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 966], ['id', 47321], ['id', 7264], ['id', 53693], ['ood', 18233]], 'labels': [3, 2, 9, 4, -1], 'scores': [1.0991997602746666, 1.9752802884370118, 2.6432417209532364, 2.956995697920097, 3.1121548124653007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9602138996124268})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8758913278579712})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.988789439201355})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1557799577713013})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.3036673069000244})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1505064964294434})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1787512302398682})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8688, 'crossentropy': 0.9916056640625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7845595479011536})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6532195210456848})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5987546443939209})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5689846277236938})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5785281658172607})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.538924515247345})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 44149], ['id', 24363], ['id', 48098], ['id', 47597], ['id', 48546]], 'labels': [2, 6, 7, 8, 4], 'scores': [0.9194213235798161, 1.6813412160761754, 2.286387475167607, 2.651379574412248, 2.82753363231524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8552601337432861})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8376586437225342})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9277787804603577})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9472314119338989})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9359195232391357})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.917981743812561})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0792036056518555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.2112112045288086})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8841, 'crossentropy': 0.8923525390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6978897452354431})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5533671379089355})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5449464917182922})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5173085927963257})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5034504532814026})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5114232301712036})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.48098209500312805})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 1423], ['id', 53316], ['id', 1019], ['id', 33319], ['ood', 23338]], 'labels': [0, 5, 7, 1, -1], 'scores': [1.0117280115001481, 1.8077826221612066, 2.4204846880464794, 2.8282457118193234, 3.0197805329090706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9765350222587585})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7890530824661255})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8495091795921326})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9876461625099182})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9921221733093262})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8663, 'crossentropy': 0.8110115234375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7260510921478271})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6310913562774658})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6145342588424683})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5612695217132568})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 25297], ['id', 14113], ['id', 10260], ['id', 15500], ['id', 44382]], 'labels': [6, 2, 3, 6, 6], 'scores': [0.7756778169683918, 1.4762487912536808, 2.0401383364573737, 2.390728229120273, 2.598495419697344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8761244416236877})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6655173897743225})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7377573847770691})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7258250713348389})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.799563467502594})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8514391183853149})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.690613134765625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6765587329864502})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5124689340591431})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4879223108291626})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4637816846370697})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4568920433521271})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 36884], ['id', 24222], ['id', 30750], ['id', 1535], ['id', 59538]], 'labels': [2, 1, 9, 1, 5], 'scores': [0.744109226573725, 1.4244430064263973, 1.9826976246993215, 2.3791605718772972, 2.635497774617715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.847366452217102})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7339686155319214})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.719014048576355})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7563179731369019})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7851450443267822})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7434090375900269})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.8079217672348022})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8293308019638062})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8693171739578247})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.7212244140625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6735088229179382})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5059003233909607})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4677208662033081})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4061189889907837})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.41699522733688354})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.42507579922676086})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.41694366931915283})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 20436], ['id', 8235], ['id', 528], ['id', 17712], ['id', 35144]], 'labels': [2, 4, 8, 3, 4], 'scores': [0.8767669676770602, 1.6453112341659346, 2.258146570584471, 2.625452420874937, 2.8315988191791037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8273724913597107})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6470834016799927})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.685581386089325})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7050783634185791})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.768097460269928})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8367118239402771})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7737400531768799})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8229879140853882})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8479275703430176})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.9165558815002441})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8076571822166443})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7987257242202759})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9526029825210571})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.8135665059089661})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.8555130958557129})
store['active_learning_steps'][16]['training']['best_epoch']=12
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.718311865234375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6346573829650879})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.46920686960220337})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.46134477853775024})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40278294682502747})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4129141569137573})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4016704261302948})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3881475329399109})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.396020770072937})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4023440182209015})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.396256685256958})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 39146], ['id', 46941], ['id', 55496], ['id', 16823], ['ood', 8624]], 'labels': [2, 5, 9, 7, -1], 'scores': [0.972589712634246, 1.832908945740868, 2.484760407459076, 2.8350063464603252, 2.983590695117039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7831056714057922})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6660349369049072})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6731648445129395})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6896937489509583})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6823961734771729})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7173796892166138})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6930725574493408})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8011592030525208})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.61375556640625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6607354879379272})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4952528476715088})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.45609694719314575})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4361059069633484})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4425092339515686})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.43960103392601013})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.43150627613067627})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 6418], ['id', 5259], ['id', 29167], ['id', 43532], ['id', 15756]], 'labels': [5, 2, 2, 8, 6], 'scores': [0.8544250499206785, 1.5882873930728243, 2.1273772523727845, 2.505364892112781, 2.7267454163359464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8175176382064819})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5852872133255005})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6617628335952759})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6364018321037292})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6281275749206543})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7127711772918701})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6427571773529053})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7445441484451294})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.573420068359375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5999152064323425})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4983291029930115})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4449462294578552})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4175134301185608})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3788951635360718})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.398529976606369})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.40119457244873047})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 12840], ['id', 42209], ['id', 24296], ['id', 32364], ['ood', 48214]], 'labels': [9, 9, 4, 7, -1], 'scores': [0.8458960048839164, 1.5491021895848913, 2.133051336443555, 2.5420674358837, 2.7975663925530228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9175843596458435})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6158474683761597})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5590991973876953})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5580742955207825})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6271257400512695})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6639801263809204})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7058995962142944})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9261, 'crossentropy': 0.538698291015625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6034194231033325})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4976918697357178})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4355386197566986})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42072194814682007})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.40608084201812744})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.422738641500473})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 6604], ['id', 49525], ['id', 15795], ['id', 41578], ['ood', 34303]], 'labels': [8, 8, 0, 8, -1], 'scores': [0.7701316309366417, 1.3733786718761962, 1.8574078276191202, 2.198623868237294, 2.405242749335729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7728199362754822})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.545536458492279})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5071943998336792})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5565682649612427})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5558534860610962})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6951643228530884})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.50837998046875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.648827314376831})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4703238010406494})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4255859851837158})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4093223810195923})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39390644431114197})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 48160], ['id', 7768], ['id', 13159], ['id', 48360], ['ood', 38890]], 'labels': [-1, 8, 2, 3, -1], 'scores': [0.7285629960441642, 1.3984712608493624, 1.9316530362435351, 2.3197450986209365, 2.572646952491861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8440825939178467})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6466231346130371})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6414429545402527})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.607792317867279})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6665533781051636})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6668381690979004})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6732008457183838})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7225372791290283})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7897071838378906})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7676424980163574})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.599971630859375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6208609342575073})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46199196577072144})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4195455014705658})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3987830579280853})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3656568229198456})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36924979090690613})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3753393292427063})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36759158968925476})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3581033945083618})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 29834], ['id', 37443], ['id', 414], ['ood', 50042], ['ood', 39169]], 'labels': [5, 3, 4, -1, -1], 'scores': [0.8986863438012502, 1.6621940780183957, 2.262354491951813, 2.665713713253247, 2.8822574827419194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7864149212837219})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5968711376190186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5820015668869019})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5979171991348267})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.647365927696228})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.697294294834137})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.533708935546875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.64300537109375})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5177268385887146})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4521011710166931})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4141286015510559})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.44746237993240356})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 30534], ['id', 32747], ['id', 39316], ['id', 19430], ['id', 49529]], 'labels': [2, 8, 7, 5, 3], 'scores': [0.7626818867671936, 1.4409791306062254, 1.9839939021354516, 2.3661329152420576, 2.6123033736859593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8255131840705872})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6622463464736938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.562179446220398})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6140559911727905})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6012102365493774})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6083890795707703})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5777338147163391})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6401399970054626})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7060641050338745})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7259607315063477})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6960299015045166})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.567839111328125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5630525350570679})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4597173035144806})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3964245319366455})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3873099088668823})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3595923185348511})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3515969216823578})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.37432152032852173})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.34591495990753174})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.33241379261016846})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 52392], ['ood', 50736], ['id', 26882], ['id', 40259], ['id', 31310]], 'labels': [1, -1, 7, 8, 0], 'scores': [0.8219201486776087, 1.5257318811934466, 2.097861002425727, 2.521265241232811, 2.768029524446847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9550265073776245})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5700154304504395})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6586934328079224})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6100070476531982})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6348907351493835})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.672243595123291})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6980722546577454})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6535882949829102})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6807326078414917})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7212123274803162})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7578052282333374})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.590157177734375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6280461549758911})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4600619673728943})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4300965964794159})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4468541145324707})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3714924454689026})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4028671979904175})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3710356652736664})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3725960850715637})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3708189129829407})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.35517963767051697})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 9948], ['id', 33161], ['id', 31738], ['id', 29530], ['id', 48010]], 'labels': [8, 3, 8, 4, 7], 'scores': [0.9722648347436584, 1.7623150564181693, 2.3883277879413294, 2.7574883394777725, 2.939873205830076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8656980991363525})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5766712427139282})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5953729152679443})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5340059995651245})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6827386021614075})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6450629234313965})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6683138608932495})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9303, 'crossentropy': 0.509910595703125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6253579258918762})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5081347227096558})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.42134493589401245})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4068932831287384})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.39135926961898804})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.37394970655441284})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 43588], ['ood', 48160], ['id', 36686], ['ood', 57445], ['ood', 26525]], 'labels': [8, -1, 6, -1, -1], 'scores': [0.7198715615552709, 1.3645314607484869, 1.9147112034951244, 2.3330649756725466, 2.6198670933283275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.899939775466919})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5759991407394409})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5814430713653564})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6085060238838196})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5997473001480103})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5998448133468628})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6053420305252075})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6829718351364136})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6196355223655701})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6332975625991821})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.584438427734375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.620124876499176})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.46303892135620117})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4169846177101135})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.38357973098754883})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3669138550758362})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3793184459209442})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.37156587839126587})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3631470799446106})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 42333], ['id', 39526], ['id', 31301], ['ood', 17421], ['id', 9552]], 'labels': [4, 5, 5, -1, 0], 'scores': [0.8512199164372618, 1.588269215200373, 2.197597628005136, 2.5735227829617875, 2.7956172896800053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9332435131072998})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5289258360862732})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5401130318641663})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5102161169052124})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5734891891479492})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5511706471443176})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5907110571861267})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6383723020553589})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.554817578125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6536155343055725})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.48466113209724426})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40734243392944336})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.39987194538116455})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.38809889554977417})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.37944281101226807})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.380666583776474})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 26966], ['id', 50912], ['id', 59747], ['id', 59295], ['id', 52228]], 'labels': [7, 6, 5, 9, 0], 'scores': [0.7622880618703745, 1.4570621327507793, 2.006908099567249, 2.418913098962374, 2.6483471083255523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.847000241279602})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5590041875839233})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5513179302215576})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5806602239608765})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5944242477416992})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5902690887451172})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9294, 'crossentropy': 0.522537109375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6457967758178711})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4966830611228943})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4910092353820801})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45882463455200195})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4356396794319153})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 25624], ['id', 5013], ['id', 12836], ['id', 47220], ['ood', 54928]], 'labels': [-1, 2, 3, 6, -1], 'scores': [0.7526254497837539, 1.412557333625585, 1.9666558421052738, 2.3161669115386267, 2.519905551027831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0125569105148315})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6119865775108337})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5703153610229492})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6437004804611206})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5724184513092041})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5582302808761597})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.609143853187561})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6056886911392212})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.531924560546875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.690793514251709})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.486228883266449})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4709979295730591})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4298221468925476})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4126928448677063})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3733247220516205})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.39124470949172974})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 28040], ['ood', 49192], ['id', 52099], ['id', 50202], ['id', 32330]], 'labels': [5, -1, 2, 5, 3], 'scores': [0.7357514096969946, 1.4111316238630387, 1.9518423738326156, 2.3379902999380384, 2.5963931292914593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9670510292053223})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6056698560714722})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5336730480194092})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5698297023773193})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.558638334274292})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5974265336990356})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6412850618362427})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5596113204956055})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6044374704360962})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5146446824073792})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6160151958465576})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5878573656082153})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5830201506614685})
store['active_learning_steps'][30]['training']['best_epoch']=10
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.533412109375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.633590579032898})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4702756404876709})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39339467883110046})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41419291496276855})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3621639013290405})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3392675817012787})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3447827100753784})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3545430600643158})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 52661], ['ood', 1990], ['ood', 32324], ['id', 19501], ['id', 44172]], 'labels': [3, -1, -1, 3, 8], 'scores': [0.9300973975393614, 1.7437487742624227, 2.343034262540006, 2.7504794041813794, 2.9500163999687183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9466961622238159})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5767107009887695})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6337435245513916})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5520188808441162})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5321661233901978})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5762563943862915})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6252673864364624})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6044987440109253})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6603823900222778})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6027668714523315})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6882238388061523})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.52228095703125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6469043493270874})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5033506155014038})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.43105393648147583})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.38350749015808105})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3583391308784485})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3569672107696533})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3636797368526459})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.35853928327560425})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3409847021102905})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 42707], ['id', 7900], ['id', 57575], ['id', 54038], ['id', 48942]], 'labels': [3, 5, 0, 9, 4], 'scores': [0.7935678571772966, 1.5006059136794554, 2.068602987145278, 2.48710011775274, 2.7454900625793908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9048687815666199})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5222412347793579})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.550208568572998})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49179792404174805})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5815384984016418})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5808247327804565})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5285214781761169})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.553182065486908})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5999613404273987})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.573500394821167})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.523542138671875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5684540271759033})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4468299150466919})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.41340672969818115})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.39480066299438477})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40242189168930054})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.352006196975708})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3571106493473053})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35039281845092773})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.357014000415802})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 42078], ['id', 48096], ['id', 1867], ['id', 40704], ['id', 8826]], 'labels': [4, 7, 5, 5, 6], 'scores': [0.7897615366544257, 1.5128260799291957, 2.110328911500705, 2.529689307376218, 2.77630380333747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1058409214019775})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5575304627418518})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5168874263763428})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5628905296325684})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5720983147621155})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.576808750629425})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5782642960548401})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6602591276168823})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5722723603248596})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6324731111526489})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5995920896530151})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.678848147392273})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5947626829147339})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.7014561891555786})
store['active_learning_steps'][33]['training']['best_epoch']=11
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.513826318359375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6079508066177368})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.46071258187294006})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.38465893268585205})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3829728960990906})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3458254337310791})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.33555084466934204})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34392887353897095})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.32466161251068115})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.32351505756378174})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.318037748336792})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 53873], ['ood', 34238], ['id', 43950], ['id', 39336], ['ood', 49304]], 'labels': [4, -1, 9, 6, -1], 'scores': [0.8748722398028428, 1.6249513604373065, 2.2401510352254537, 2.6755864903618907, 2.892170660140806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9730767011642456})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5254337787628174})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4906490445137024})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5069248080253601})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5162893533706665})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5035490393638611})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5183267593383789})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5387574434280396})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5923038125038147})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5046653151512146})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.560839056968689})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.481853857421875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5762300491333008})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4541568458080292})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4010881185531616})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.35420021414756775})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3415631055831909})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34256768226623535})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3210439383983612})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34254467487335205})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3204466700553894})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3395025134086609})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 35882], ['id', 13049], ['id', 12416], ['ood', 30603], ['ood', 31448]], 'labels': [2, 9, 3, -1, -1], 'scores': [0.913455052636202, 1.7542858115582405, 2.388508961691122, 2.8435548437285414, 3.086576784284736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0805938243865967})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5945996046066284})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5799857378005981})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5134186148643494})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5173279047012329})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5453996062278748})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5612260103225708})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5625017881393433})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6032798290252686})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.481079150390625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6017450094223022})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47236835956573486})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3775182068347931})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.38454052805900574})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.34352827072143555})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3649258315563202})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.33710038661956787})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.35252881050109863})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 10520], ['id', 22505], ['id', 21164], ['id', 54892], ['id', 27418]], 'labels': [-1, 9, 2, 3, 8], 'scores': [0.8023974466819175, 1.521510814958507, 2.1014752398584537, 2.521527719838712, 2.770717062125602]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1007964611053467})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5902537107467651})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5632962584495544})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5248924493789673})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5293534994125366})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5367892980575562})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5410888195037842})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6000423431396484})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5998189449310303})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.472714111328125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6310532093048096})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.45787301659584045})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4268408417701721})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3897504508495331})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.39768296480178833})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.36220163106918335})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3566889762878418})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3587632179260254})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 27395], ['id', 39208], ['id', 25309], ['ood', 39880], ['id', 37542]], 'labels': [0, 5, 2, -1, 6], 'scores': [0.791214921926545, 1.5176115264087189, 2.0771563577514716, 2.456936081966579, 2.713856189264864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0241795778274536})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6279445886611938})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.532683253288269})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5334524512290955})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4909573197364807})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5575672388076782})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5873302221298218})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5462141633033752})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5688642263412476})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5978712439537048})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6519796252250671})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.500362939453125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6349675059318542})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4762724041938782})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.39807718992233276})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3635003864765167})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.35974496603012085})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3577493131160736})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3473280966281891})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.32473066449165344})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3388155698776245})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 26568], ['ood', 32583], ['id', 37636], ['id', 7207], ['id', 44426]], 'labels': [-1, -1, 3, 2, 3], 'scores': [0.8982976003500862, 1.6376349432482176, 2.254099098378326, 2.6182439917481615, 2.8381032222856826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0152130126953125})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5216052532196045})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5398093461990356})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4424667954444885})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46418723464012146})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42450758814811707})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.485141396522522})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9451, 'crossentropy': 0.386729052734375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6240960359573364})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4825761318206787})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.42909449338912964})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37275993824005127})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38163697719573975})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.35607752203941345})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 60], ['id', 32918], ['id', 24870], ['id', 49764], ['ood', 9287]], 'labels': [4, 2, 3, 9, -1], 'scores': [0.7794749413912925, 1.4645635211494028, 1.9656381041392121, 2.3504266867855295, 2.59616646705355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9756180644035339})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5892295837402344})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4802309274673462})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4585055708885193})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5386338829994202})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5252367854118347})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4994349479675293})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4959425926208496})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5109946131706238})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5041090250015259})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5480637550354004})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.4249224609375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6759498119354248})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.47733888030052185})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43027639389038086})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3446173071861267})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3709999918937683})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.33033818006515503})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3353290557861328})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.344034880399704})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.31859129667282104})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 20641], ['id', 17055], ['id', 3010], ['ood', 1254], ['id', 5170]], 'labels': [9, 8, 7, -1, 8], 'scores': [0.8801270833309267, 1.6421489820453679, 2.2333915407683813, 2.59357750641609, 2.778244163476301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1619426012039185})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5899155735969543})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4731643795967102})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47453388571739197})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4691287577152252})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4616156220436096})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5285251140594482})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5123831629753113})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9483, 'crossentropy': 0.412620947265625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6730794906616211})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.43701326847076416})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4162355661392212})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3868730366230011})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38402581214904785})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3388543725013733})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34226590394973755})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 15738], ['id', 31545], ['id', 24899], ['id', 51432], ['ood', 10520]], 'labels': [-1, 5, 3, 1, -1], 'scores': [0.778786492986701, 1.4957303171803789, 2.078447127771611, 2.4621579043440835, 2.689583401388596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0370547771453857})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5298639535903931})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4430866241455078})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45286449790000916})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44389843940734863})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45449578762054443})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4461236894130707})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9437, 'crossentropy': 0.41336904296875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6577556133270264})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5078466534614563})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42801058292388916})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40015366673469543})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39469069242477417})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.381359338760376})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 49957], ['id', 644], ['id', 8731], ['id', 18130], ['id', 31608]], 'labels': [5, 7, 5, 8, 2], 'scores': [0.6992678011602975, 1.2932928377934934, 1.7949109839886948, 2.178346862381524, 2.4303906473415404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.2023565769195557})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5425423979759216})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4898664355278015})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45533087849617004})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4408908188343048})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.446756511926651})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46623343229293823})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9506, 'crossentropy': 0.3974106689453125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6741461753845215})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.49218955636024475})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4288398027420044})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39356857538223267})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.37113264203071594})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3631712794303894})
store['active_learning_steps'][42]['eval_training']['best_epoch']=5
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 44952], ['id', 6348], ['id', 30844], ['id', 7840], ['id', 51863]], 'labels': [6, 2, 8, 5, 9], 'scores': [0.7105364794656284, 1.3446091087837928, 1.874334257091654, 2.274625350754774, 2.535348381247407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0504024028778076})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5188542604446411})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4313381314277649})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4196203947067261})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40614110231399536})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4180312156677246})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3807113766670227})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4386320114135742})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4337106943130493})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4678584635257721})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4268723130226135})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.371648291015625}
