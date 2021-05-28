store = {}
store['timestamp']=1622161435
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=34']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=34
store['worker_id']=34
store['num_workers']=40
store['config']={'seed': 1272, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.177926540374756})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.4888577461242676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.854431629180908})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.872493267059326})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6897, 'crossentropy': 1.975742578125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1336599588394165})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1393769979476929})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.138232707977295})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 30738], ['id', 14614], ['id', 27120], ['id', 287], ['id', 30162]], 'labels': [8, 8, 2, 5, 8], 'scores': [1.07624004588975, 1.898378917894937, 2.5124539805609505, 2.894308769009962, 3.127243895390439]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.075826644897461})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.554025173187256})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.388314723968506})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.700335741043091})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7254014015197754})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7037, 'crossentropy': 2.1774669921875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.201286792755127})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.125460147857666})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1125638484954834})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1179523468017578})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 25359], ['id', 23642], ['id', 4873], ['id', 53574], ['ood', 20270]], 'labels': [5, 2, 8, 8, -1], 'scores': [1.1588252824361278, 2.096443346494186, 2.7552630296342393, 3.1633634884050394, 3.3682684763438546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.5055081844329834})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6840031147003174})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.826854705810547})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.972991466522217})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.0946760177612305})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.924002170562744})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.8232429027557373})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 3.047640323638916})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 3.22006893157959})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9813036918640137})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.6333885192871094})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.167971611022949})
store['active_learning_steps'][2]['training']['best_epoch']=9
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.702, 'crossentropy': 2.726609765625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1223983764648438})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.083540916442871})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.090649962425232})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1049842834472656})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1423404216766357})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 28900], ['id', 39963], ['id', 52322], ['id', 5315], ['id', 1758]], 'labels': [3, 4, 7, 3, 8], 'scores': [1.070130241172706, 1.9542293534572885, 2.576801989265169, 2.957239604879299, 3.1471150710513855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.9318995475769043})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.6074910163879395})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.6732544898986816})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.995842933654785})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.701226234436035})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.893998146057129})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.876340866088867})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.037684917449951})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.351600408554077})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7155, 'crossentropy': 2.451847265625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0989418029785156})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0917658805847168})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0942176580429077})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0632152557373047})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 34381], ['id', 45180], ['id', 24353], ['ood', 29168], ['ood', 33793]], 'labels': [0, 7, 5, -1, -1], 'scores': [1.0180538988186718, 1.8060246862263734, 2.355075781524125, 2.6769138023586487, 2.8568763841418328]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.101472854614258})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.5719151496887207})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.7896718978881836})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.0116138458251953})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.9541666507720947})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7054, 'crossentropy': 2.2097259765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2507014274597168})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.2195252180099487})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1850969791412354})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1717791557312012})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 16118], ['id', 30750], ['id', 57303], ['id', 12931], ['id', 6962]], 'labels': [6, 9, 1, 2, 8], 'scores': [0.9409952786669975, 1.7479906488695924, 2.407692581610534, 2.8526851930397212, 3.075741858354194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.5338659286499023})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.9558520317077637})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.256681442260742})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4557836055755615})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7502, 'crossentropy': 1.459413671875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.055373191833496})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9801866412162781})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9706246852874756})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 47368], ['id', 27641], ['id', 25798], ['id', 16593], ['id', 33050]], 'labels': [4, 2, 6, 4, 7], 'scores': [0.8698902668268385, 1.5818499069394925, 2.1090009512187375, 2.488331509048118, 2.715053424579387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3676021099090576})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.7149889469146729})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.905078649520874})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.7536711692810059})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.9800300598144531})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9663190841674805})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.0790560245513916})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.102766990661621})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.781, 'crossentropy': 1.6935140625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0110176801681519})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.8609814643859863})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.8792108297348022})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.8674263954162598})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8527650237083435})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.890112578868866})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.8789399862289429})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 48431], ['id', 17404], ['ood', 109], ['id', 56838], ['id', 44753]], 'labels': [3, 3, -1, 5, 5], 'scores': [0.9828902394709655, 1.7732198400789372, 2.394388758299576, 2.8186267290974003, 3.053908870243353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.290503740310669})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.6717681884765625})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.9495892524719238})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8453044891357422})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.925750494003296})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.0116682052612305})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.055095672607422})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 2.127192974090576})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7993, 'crossentropy': 1.6146984375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9695178270339966})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.8645755052566528})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.820399284362793})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.7982088923454285})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.7910126447677612})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.7851454019546509})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.8079859018325806})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 18042], ['id', 26233], ['id', 31706], ['id', 6514], ['ood', 57491]], 'labels': [0, 9, 8, 9, -1], 'scores': [0.891438361875017, 1.6451400869137438, 2.250234858625702, 2.6735480470557356, 2.8872849490151964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2247123718261719})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4061497449874878})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6327825784683228})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.6495327949523926})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.6679153442382812})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8044, 'crossentropy': 1.150203125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.8853700160980225})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.8502130508422852})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.8117507696151733})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.7927722930908203})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 52294], ['id', 15751], ['id', 31404], ['id', 34886], ['id', 49207]], 'labels': [0, 2, 3, 9, 3], 'scores': [0.8630636308036554, 1.60337149019306, 2.137336135283997, 2.5037775807306275, 2.7580150530734446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1686393022537231})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0897603034973145})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1755927801132202})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1781210899353027})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.363584041595459})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3374931812286377})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3695552349090576})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8477, 'crossentropy': 1.0799671875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.7870179414749146})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.68608158826828})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.6984260082244873})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.684490978717804})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.643190324306488})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 58429], ['id', 8353], ['id', 58470], ['id', 8586], ['id', 56440]], 'labels': [2, 7, 9, 9, 4], 'scores': [0.859239744792961, 1.6056275108243652, 2.1910756301943604, 2.577754738213069, 2.8342664478388215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0349924564361572})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0148866176605225})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1530953645706177})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.112039566040039})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2941832542419434})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8665, 'crossentropy': 0.8464693359375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7672872543334961})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6527262926101685})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6515769958496094})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6321879625320435})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 27915], ['id', 51492], ['id', 19590], ['id', 32348], ['id', 21007]], 'labels': [2, 5, 5, 5, 3], 'scores': [0.8007397892189219, 1.4748855330787585, 2.0356205605284776, 2.4126267681086384, 2.6458228271885993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8977669477462769})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8164091110229492})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0414478778839111})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9544698596000671})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.128378987312317})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8789, 'crossentropy': 0.739822998046875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7295960187911987})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6368021368980408})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.616564154624939})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.5892539024353027})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59286], ['id', 12984], ['id', 43648], ['id', 28413], ['id', 50424]], 'labels': [8, 8, 5, 5, 0], 'scores': [0.6921451767916114, 1.3123124012450327, 1.82501733790897, 2.2066135364669517, 2.465357405809433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9498769044876099})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.887248158454895})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0420010089874268})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1310298442840576})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1543225049972534})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8624, 'crossentropy': 0.804979833984375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7329603433609009})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6283891201019287})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6129015684127808})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6095289587974548})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 52686], ['id', 32173], ['id', 46903], ['id', 14866], ['id', 58058]], 'labels': [5, 7, 6, 7, 8], 'scores': [0.751602879809234, 1.4240301009521916, 1.9584050167781513, 2.3578404911067627, 2.6077444987400753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9021196365356445})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9208634495735168})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8982869386672974})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9981765747070312})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9056657552719116})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0043094158172607})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0465381145477295})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0658440589904785})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1609879732131958})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8764, 'crossentropy': 0.92270908203125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7031458020210266})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5824368596076965})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5289543867111206})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5389540195465088})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5105268359184265})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5270936489105225})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5335633754730225})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5067631006240845})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 35128], ['id', 10639], ['id', 20508], ['id', 39309], ['id', 12784]], 'labels': [2, 4, 9, 0, 2], 'scores': [0.9810895473080916, 1.7581317723286753, 2.356813985938027, 2.7549624698124138, 3.0086246084653183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8631906509399414})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7821636199951172})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9477649331092834})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9393419027328491})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9480001926422119})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.049135446548462})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0044413805007935})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8911680579185486})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9697110056877136})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1717959642410278})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.2203651666641235})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8883, 'crossentropy': 0.9239638671875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6668565273284912})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5523962378501892})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5133091807365417})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.500415563583374})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5076782703399658})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.4826677441596985})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 8439], ['id', 56457], ['id', 29630], ['ood', 39314], ['id', 7271]], 'labels': [9, 3, 6, -1, 0], 'scores': [0.8695012080658246, 1.642550153352913, 2.2525347936302325, 2.6552575483452987, 2.8979827410478007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8789867162704468})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.778613805770874})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8472497463226318})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9763857126235962})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0467337369918823})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8824, 'crossentropy': 0.683809716796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7446452379226685})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.5887148380279541})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.585777997970581})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5708526968955994})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 57236], ['id', 27113], ['id', 35232], ['id', 32344], ['id', 2740]], 'labels': [9, 2, 8, 5, 3], 'scores': [0.7534185668667663, 1.3820435462653702, 1.9179726226678566, 2.3276286936704347, 2.584577856669105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8208270072937012})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.784562885761261})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8389582633972168})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7787621021270752})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.873688817024231})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8635580539703369})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8575330972671509})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.941280722618103})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.930741548538208})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9673147201538086})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.0374855995178223})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 1.0173588991165161})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0536913871765137})
store['active_learning_steps'][16]['training']['best_epoch']=10
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.81921904296875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6353835463523865})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5334926843643188})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4850202202796936})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.47569769620895386})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.48452797532081604})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4489595592021942})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.47708025574684143})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 34199], ['id', 54452], ['id', 1740], ['ood', 35710], ['ood', 39784]], 'labels': [-1, 4, 9, -1, -1], 'scores': [1.0573991051616574, 1.8869041220383496, 2.5297227129781144, 2.9240802068208813, 3.1536736747429917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9045403599739075})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6689882874488831})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7546678781509399})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7233311533927917})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8075698614120483})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8485856056213379})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8774192929267883})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.65575634765625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6446793079376221})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5144707560539246})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4807322323322296})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.47809934616088867})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.45214909315109253})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.45737695693969727})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 59297], ['ood', 11641], ['id', 25384], ['id', 26785], ['ood', 11690]], 'labels': [1, -1, 5, 6, -1], 'scores': [0.8299039118217784, 1.5700839282085544, 2.134796112229788, 2.5361929407532537, 2.7728581051071455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8084248900413513})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7450540065765381})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6970373392105103})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8582892417907715})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8026490211486816})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7945848703384399})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9072095155715942})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.872944712638855})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.66906220703125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6361271142959595})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5074484944343567})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4833979308605194})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4893105626106262})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4652637839317322})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.46894389390945435})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.46234115958213806})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 33383], ['id', 38524], ['id', 10086], ['id', 20187], ['id', 40092]], 'labels': [1, 4, 7, 6, 8], 'scores': [0.8093384285835499, 1.5234527136908316, 2.1190983044240017, 2.5230755411709938, 2.793326657684748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7429163455963135})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6396735906600952})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.704584002494812})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8122929930686951})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.802568793296814})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.560536474609375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6732280254364014})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5517896413803101})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5558106303215027})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.49641329050064087})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 15832], ['id', 21880], ['id', 33812], ['id', 7264], ['id', 13179]], 'labels': [9, 2, 6, 9, 2], 'scores': [0.8362195982966647, 1.5278571234293432, 2.066996918710661, 2.450522343920867, 2.677590704396696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8429901599884033})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6309635639190674})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6417334079742432})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6739195585250854})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6729758977890015})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7441179156303406})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6727663278579712})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6870348453521729})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7457383871078491})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7466825246810913})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8949111700057983})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.573607958984375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6219835877418518})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5031919479370117})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4330419898033142})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3936610817909241})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.3920474052429199})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4278859794139862})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37559160590171814})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3906738758087158})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.38276785612106323})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.38504689931869507})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 42317], ['id', 35632], ['id', 40720], ['ood', 5355], ['ood', 24227]], 'labels': [5, 0, 3, -1, -1], 'scores': [0.9521623365562206, 1.7759767287870694, 2.3746044700272027, 2.7240672699964383, 2.900740605778914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8932188153266907})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6254321336746216})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7258440256118774})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8241021633148193})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.731273353099823})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9203, 'crossentropy': 0.549198046875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6808310747146606})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.596138596534729})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.49812692403793335})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5033623576164246})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 16983], ['id', 49482], ['id', 13259], ['id', 22459], ['id', 4165]], 'labels': [1, 1, 1, 3, 2], 'scores': [0.7058182142344991, 1.2920518627245543, 1.8050246385779438, 2.210505557011089, 2.507666641658984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9526067972183228})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6642981767654419})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7100808024406433})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7447711229324341})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7863996028900146})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.582842041015625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7093773484230042})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6449816226959229})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.563684344291687})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.595533549785614})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 19824], ['id', 11441], ['id', 42020], ['id', 52949], ['id', 44307]], 'labels': [9, 3, 9, 4, 5], 'scores': [0.6807988373465539, 1.284074976746843, 1.8089664550059528, 2.1867883669001795, 2.4356469556915368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9383074045181274})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6049038171768188})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5922104120254517})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6370769143104553})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6130267381668091})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6785981059074402})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7468663454055786})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7741574048995972})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9365, 'crossentropy': 0.507487841796875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6147206425666809})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.44711756706237793})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4098009765148163})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4132622480392456})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.3914793133735657})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3617907762527466})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3829886019229889})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 16022], ['id', 52099], ['id', 46658], ['id', 25508], ['id', 55724]], 'labels': [8, 2, 8, 5, 7], 'scores': [0.8805518412518105, 1.6271358432446776, 2.1969395859127, 2.5436594862155406, 2.7221359192801096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7598335146903992})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5602255463600159})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5898185968399048})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5463218688964844})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6072909832000732})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6333391666412354})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6522786617279053})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.47742919921875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6754052042961121})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.491220623254776})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43133336305618286})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4308599531650543})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4110499620437622})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.43181636929512024})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4153], ['ood', 37183], ['id', 48010], ['id', 18501], ['id', 14394]], 'labels': [2, -1, 7, 4, 3], 'scores': [0.7549241774679569, 1.4047523399890136, 1.9406217624360949, 2.3089246657936533, 2.532159439095551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8920484185218811})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.568564772605896})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5414081811904907})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6022270917892456})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6488229036331177})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.694808840751648})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6034784317016602})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7931196689605713})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7500738501548767})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8150993585586548})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.516541748046875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6320492029190063})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.4934941530227661})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4523470401763916})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39475464820861816})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4003279209136963})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3829430341720581})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4001038074493408})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 55804], ['id', 3719], ['id', 57742], ['ood', 32638], ['id', 29360]], 'labels': [5, 2, 6, -1, 8], 'scores': [0.8505729557940571, 1.6299971463840985, 2.222560923784931, 2.5777774002611267, 2.7560301527163134]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9262946844100952})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6145911812782288})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6276054978370667})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6220771670341492})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6286453008651733})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6729626655578613})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7761525511741638})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.53581689453125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6519196033477783})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49170926213264465})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4328722357749939})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42586439847946167})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4279824495315552})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.447323739528656})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 9608], ['id', 47597], ['id', 49493], ['id', 57263], ['id', 46441]], 'labels': [8, 8, 8, 8, 6], 'scores': [0.8434161875165123, 1.6006055307773144, 2.1950478374740285, 2.5623544638514675, 2.768073721901862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9451659917831421})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5336299538612366})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5568177700042725})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5246899127960205})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6129093170166016})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5564481616020203})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.465581005859375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6888048648834229})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5253244638442993})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4648587703704834})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43120861053466797})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.40417197346687317})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 27199], ['id', 25829], ['id', 53358], ['ood', 45486], ['id', 32730]], 'labels': [7, 3, 3, -1, 3], 'scores': [0.815533383227151, 1.5256182874920947, 2.0898155400794725, 2.506706683309509, 2.755159945586751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9751706123352051})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6003522872924805})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5929417610168457})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6715545058250427})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6746660470962524})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.648912250995636})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6048916578292847})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6368944644927979})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7145824432373047})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6629796028137207})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.7214645147323608})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7339087724685669})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.7172493934631348})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.731544554233551})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6974589824676514})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.8309586048126221})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7703834772109985})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8621023893356323})
store['active_learning_steps'][28]['training']['best_epoch']=15
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.941, 'crossentropy': 0.565080517578125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6071160435676575})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4403873085975647})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4109344482421875})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4063417315483093})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3762367367744446})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3681095540523529})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36113297939300537})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.33693820238113403})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3731531500816345})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3178057074546814})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.32666248083114624})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3202711343765259})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.33549800515174866})
store['active_learning_steps'][28]['eval_training']['best_epoch']=10
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 55028], ['id', 33438], ['id', 50898], ['id', 5029], ['id', 17736]], 'labels': [3, 2, 2, 8, 4], 'scores': [1.0145328215366982, 1.892143477004057, 2.5850179381352554, 2.997977287749543, 3.2210318783746636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8812311291694641})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5349213480949402})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49030250310897827})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5373178124427795})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5821449160575867})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5913731455802917})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5763037800788879})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6179885268211365})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5682368278503418})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5704563856124878})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6371153593063354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6488686800003052})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9456, 'crossentropy': 0.46016708984375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6547789573669434})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47778475284576416})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3955410122871399})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37529000639915466})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34938663244247437})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3476490080356598})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35890328884124756})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31666240096092224})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3195909857749939})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3116995692253113})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3169419765472412})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 14825], ['ood', 55778], ['ood', 24680], ['id', 25566], ['id', 27996]], 'labels': [3, -1, -1, 5, 5], 'scores': [0.914657004786581, 1.7248741245875108, 2.362627914386981, 2.776481071813386, 2.9929254515192927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8098247647285461})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5540624260902405})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.535869836807251})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5011138916015625})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5335946083068848})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6061621308326721})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.595516562461853})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5394178628921509})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5749237537384033})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6126032471656799})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6336740255355835})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.492619970703125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6345857977867126})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4748614430427551})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.42455732822418213})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.373627245426178})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3924531936645508})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3633083701133728})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3672105073928833})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.36485350131988525})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3469427525997162})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 41196], ['id', 45602], ['ood', 24172], ['id', 3094], ['ood', 11690]], 'labels': [9, 5, -1, 8, -1], 'scores': [0.8835251926343153, 1.6356358784460188, 2.2126201159684715, 2.6016335675838054, 2.805441767874229]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8895543217658997})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.609991192817688})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.503718912601471})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5643696784973145})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5346966981887817})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5498296618461609})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5794205665588379})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6035208702087402})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.413047412109375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5997651815414429})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.48470422625541687})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.43377619981765747})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41419717669487})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3773999810218811})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.37447887659072876})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35240602493286133})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 5370], ['id', 48006], ['id', 22497], ['id', 13099], ['id', 30742]], 'labels': [3, 6, 7, 3, 1], 'scores': [0.7577824321162139, 1.4116076734561567, 1.9484045322517476, 2.3436220325006545, 2.596715540468546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9488379955291748})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5896982550621033})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4847695231437683})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4882781505584717})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5476813316345215})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.611260712146759})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5118195414543152})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.438301904296875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6275773048400879})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4591056704521179})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4259033203125})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3787142038345337})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38705217838287354})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3853190839290619})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 4066], ['id', 3598], ['id', 21355], ['id', 3290], ['id', 16676]], 'labels': [1, 9, 0, 4, 3], 'scores': [0.769991930704313, 1.450843646832615, 2.0386351498933193, 2.45991986969676, 2.728587548942449]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9436930418014526})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6735305190086365})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4972595274448395})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5432460308074951})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5472043752670288})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5111190676689148})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5667377710342407})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6408828496932983})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.4687712890625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6361653804779053})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4999994933605194})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4273666739463806})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36697816848754883})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3929365575313568})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34790968894958496})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.39876335859298706})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 49616], ['id', 53872], ['id', 21304], ['id', 48102], ['id', 32286]], 'labels': [7, 8, 4, 7, 4], 'scores': [0.8608614570837649, 1.6020946710721815, 2.183312866823906, 2.5493363880261786, 2.728530812920912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0409421920776367})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6290326714515686})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5684632062911987})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5309659838676453})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5115231871604919})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.581089437007904})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5682041645050049})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5351269245147705})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9486, 'crossentropy': 0.42830576171875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6617456674575806})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4709469676017761})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4147781431674957})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43666693568229675})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36193251609802246})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37204909324645996})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3306739330291748})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 27991], ['id', 44123], ['id', 9294], ['id', 50202], ['ood', 43952]], 'labels': [-1, 8, 3, 5, -1], 'scores': [0.8320588618267952, 1.5811575229839532, 2.1588011606023514, 2.553725925686157, 2.801426764893929]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.048781156539917})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5679038166999817})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5162185430526733})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5223848819732666})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5278092622756958})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5582021474838257})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5682504177093506})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5652644634246826})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5943482518196106})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9401, 'crossentropy': 0.478946875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6989362835884094})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5082967877388})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43115201592445374})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.39556241035461426})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3803262710571289})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.40410763025283813})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3603821396827698})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.35202711820602417})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 43796], ['id', 9180], ['id', 44013], ['id', 37328], ['id', 40216]], 'labels': [7, 3, 4, 4, 7], 'scores': [0.7658986688026783, 1.4649649618344878, 2.009011970555103, 2.3896320223379792, 2.61689912657568]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0452563762664795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5565595626831055})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5338530540466309})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5169394016265869})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4849523901939392})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.49955636262893677})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5061696767807007})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5088215470314026})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5252904891967773})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5800190567970276})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5648192763328552})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5340893268585205})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9533, 'crossentropy': 0.42143515625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6221484541893005})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.44734445214271545})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4162404537200928})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37690305709838867})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.339032381772995})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.318345844745636})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.323280930519104})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.32773667573928833})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32555949687957764})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.304649293422699})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31701070070266724})
store['active_learning_steps'][36]['eval_training']['best_epoch']=11
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 54180], ['id', 7146], ['id', 50743], ['id', 40130], ['ood', 26635]], 'labels': [8, 2, 7, 4, -1], 'scores': [0.9004377803466392, 1.6911637518046998, 2.3378798349409475, 2.752633730517327, 3.0081638256949166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.964707612991333})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5488064289093018})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4680407643318176})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4945510923862457})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.50536048412323})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4817116856575012})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5372906923294067})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.431389501953125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6569373607635498})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5042569637298584})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.42898136377334595})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4132143557071686})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3722694218158722})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3946044445037842})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 54556], ['id', 27289], ['id', 49515], ['id', 34058], ['id', 11702]], 'labels': [2, 0, 2, 3, 1], 'scores': [0.8247162907567309, 1.514809526728099, 2.0597469736357885, 2.4243066497317907, 2.6637181976824476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9999688863754272})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5352020263671875})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49701082706451416})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4596686363220215})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4634981155395508})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.46907973289489746})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5272389054298401})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5312159657478333})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5060485601425171})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9515, 'crossentropy': 0.396493017578125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6390950679779053})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.463326096534729})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40549683570861816})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4014192223548889})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3787856698036194})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3553697466850281})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3313371539115906})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3534020185470581})
store['active_learning_steps'][38]['eval_training']['best_epoch']=7
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 49518], ['id', 43811], ['id', 48382], ['id', 45787], ['ood', 26295]], 'labels': [-1, 0, 8, 9, -1], 'scores': [0.7955286722682628, 1.5089722848841625, 2.1045047404119144, 2.495902453306069, 2.7430469874415007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9507992267608643})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4979662001132965})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.547592282295227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42822176218032837})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4873616695404053})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5043154358863831})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.43877899646759033})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5358539819717407})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5621776580810547})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5017485618591309})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.4042404541015625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6467336416244507})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4960189163684845})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38891831040382385})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37797051668167114})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3442922830581665})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37495774030685425})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3236217200756073})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3045559823513031})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30721670389175415})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 10064], ['ood', 3694], ['ood', 41157], ['ood', 13979], ['ood', 9049]], 'labels': [8, -1, -1, -1, -1], 'scores': [0.7521186080753777, 1.4371912617045437, 2.0097103045849183, 2.4560540537054214, 2.7627423813271736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9705337882041931})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5174601674079895})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4972226023674011})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4621298611164093})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47871890664100647})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4729357659816742})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.476706862449646})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49468863010406494})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5113875865936279})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.3911937255859375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6264569163322449})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.47513347864151})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41208189725875854})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39924728870391846})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3579868674278259})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33954960107803345})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.32639724016189575})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33151665329933167})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 1518], ['id', 42085], ['ood', 55201], ['id', 2548], ['ood', 25543]], 'labels': [9, 5, -1, 4, -1], 'scores': [0.7740716867635402, 1.4799370676211203, 2.0501843190215423, 2.4889491767785383, 2.7843283499108145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0694468021392822})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5205563306808472})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.48141008615493774})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46911799907684326})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5508919954299927})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.503059983253479})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.412845703125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6633707284927368})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5130677223205566})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4732745885848999})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41810178756713867})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45479586720466614})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 49497], ['id', 31301], ['id', 36818], ['id', 41999], ['ood', 7829]], 'labels': [0, 5, 7, 0, -1], 'scores': [0.6396356930805147, 1.2230208146572603, 1.7095517353800052, 2.103149787431085, 2.3790046502309696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1356797218322754})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5475884675979614})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5004777908325195})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49865150451660156})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4736056327819824})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44047778844833374})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.47694075107574463})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.533016562461853})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.45350000262260437})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5529158711433411})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5388103723526001})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5780134201049805})
store['active_learning_steps'][42]['training']['best_epoch']=9
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9552, 'crossentropy': 0.3911103271484375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5821783542633057})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46758270263671875})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37038248777389526})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36700713634490967})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3458858132362366})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29391101002693176})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2991502583026886})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31634366512298584})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30358248949050903})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29113537073135376})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3106452226638794})
store['active_learning_steps'][42]['eval_training']['best_epoch']=10
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 19089], ['ood', 21751], ['id', 38702], ['id', 20486], ['ood', 45096]], 'labels': [5, -1, 8, 6, -1], 'scores': [0.8652772096834579, 1.6308301760359285, 2.236171163857365, 2.637095498693819, 2.855327948184353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0964865684509277})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6459310054779053})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5219089984893799})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5036488771438599})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5306464433670044})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5667955875396729})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5206783413887024})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.565941333770752})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5346834659576416})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5288214087486267})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5759288668632507})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.6255784630775452})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.608932614326477})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.484517578125}
