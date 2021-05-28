store = {}
store['timestamp']=1622150505
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=10']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=40
store['config']={'seed': 1245, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.615990161895752})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.829294443130493})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7502405643463135})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.98714017868042})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.707611560821533})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6695, 'crossentropy': 2.4646146484375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1953825950622559})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2107692956924438})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.284072995185852})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2340553998947144})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 49149], ['id', 29361], ['id', 52959], ['id', 37125], ['id', 16624]], 'labels': [3, 5, 2, 8, 8], 'scores': [1.1660227656269182, 2.059119649547021, 2.678276869026961, 3.0629697478414757, 3.260595776375374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.0632715225219727})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2106895446777344})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.4767985343933105})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.780567169189453})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 3.000762462615967})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7367, 'crossentropy': 2.0472669921875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0501322746276855})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0004725456237793})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9713265895843506})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9827635884284973})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 21851], ['id', 19315], ['id', 28561], ['id', 4241], ['id', 32531]], 'labels': [8, 9, 3, 2, 0], 'scores': [1.072993072415458, 1.9202058937624167, 2.564796794112506, 2.946721602556341, 3.164882256189453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.8904757499694824})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.0650134086608887})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3941328525543213})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.4558959007263184})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.539032459259033})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.8325116634368896})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.705, 'crossentropy': 2.1726126953125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0983879566192627})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0389618873596191})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0294663906097412})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0244381427764893})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 27225], ['id', 17217], ['id', 28189], ['ood', 45812], ['ood', 20270]], 'labels': [7, 5, 2, -1, -1], 'scores': [0.9785263456273783, 1.723193968569245, 2.304721830753479, 2.6395929023831846, 2.8515469074602464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.6181014776229858})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.793569803237915})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.9635429382324219})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4146764278411865})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.4973864555358887})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7423, 'crossentropy': 1.74254140625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.9755329489707947})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9694168567657471})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9419529438018799})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9525939226150513})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 41923], ['id', 27073], ['id', 25315], ['id', 27006], ['id', 22503]], 'labels': [4, 2, 5, 6, 9], 'scores': [0.9980370819004303, 1.7980870607013246, 2.3312514228309773, 2.6569021273815716, 2.8373054331423955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3828251361846924})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.5431270599365234})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.717822551727295})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7385830879211426})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.9509453773498535})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7951, 'crossentropy': 1.28335791015625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9381076097488403})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.7778745293617249})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.7698807716369629})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.7450324892997742})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 38310], ['id', 60], ['id', 27783], ['id', 29239], ['id', 38559]], 'labels': [0, 4, 3, 1, 0], 'scores': [0.9433178659973618, 1.651110160148968, 2.2302564690956634, 2.6206105787021494, 2.841546406877626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.431548833847046})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.597731351852417})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.6874994039535522})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5456938743591309})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.7096819877624512})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.6960660219192505})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.6186420917510986})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 2.1449694633483887})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.9137523174285889})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.9730868339538574})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8334, 'crossentropy': 1.53766982421875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8113263249397278})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7142434120178223})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.680828332901001})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6566890478134155})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.6668980121612549})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.6829541921615601})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 13030], ['id', 24902], ['id', 22561], ['id', 7833], ['ood', 56860]], 'labels': [0, 9, 6, 5, -1], 'scores': [1.1103434219039712, 2.032096309099746, 2.6933686981607554, 3.0571358349269495, 3.21353420297463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2962093353271484})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.364565372467041})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4444612264633179})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.4370111227035522})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.4931507110595703})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.847820520401001})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.5756750106811523})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.7902483940124512})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.829, 'crossentropy': 1.37154296875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.829596221446991})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7382924556732178})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6851317882537842})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7353061437606812})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6462104320526123})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6750032901763916})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6479795575141907})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 27357], ['id', 59321], ['id', 4909], ['id', 9348], ['id', 41403]], 'labels': [7, 4, 8, 4, 9], 'scores': [0.9856333368771513, 1.8905693056412494, 2.547095917526124, 2.955285417452174, 3.168650222663701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.082388162612915})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1793098449707031})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.142012596130371})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2242732048034668})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2715246677398682})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.2329328060150146})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2932989597320557})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.4458539485931396})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.537964105606079})
store['active_learning_steps'][7]['training']['best_epoch']=6
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8587, 'crossentropy': 1.1491837890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6945145726203918})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6342451572418213})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.5902354717254639})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5938570499420166})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5640697479248047})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5377044677734375})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5351505279541016})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5539608001708984})
store['active_learning_steps'][7]['eval_training']['best_epoch']=7
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 47558], ['id', 41507], ['id', 14068], ['id', 41108], ['id', 44102]], 'labels': [4, 3, 8, 0, 6], 'scores': [0.9395445785627841, 1.755041263508776, 2.4099358493899032, 2.8172955297941904, 3.0510543932465435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9199622273445129})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.03269362449646})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2817147970199585})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.381457805633545})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.4655224084854126})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8492, 'crossentropy': 0.97505341796875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8087904453277588})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6950877904891968})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.624824047088623})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6403903365135193})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 57273], ['id', 36884], ['id', 12281], ['id', 33967], ['id', 19212]], 'labels': [2, 2, 2, 2, 9], 'scores': [0.8588334848831847, 1.5385477806105272, 2.081464813782194, 2.4285204842651016, 2.6352979033748563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0128929615020752})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1141949892044067})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0399521589279175})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2591803073883057})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.3193998336791992})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2812604904174805})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8732, 'crossentropy': 0.88278896484375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7749025821685791})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6236000061035156})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5944333076477051})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.571395754814148})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.5650688409805298})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 32419], ['id', 9380], ['id', 9538], ['id', 31148], ['id', 40787]], 'labels': [4, 3, 7, 2, 8], 'scores': [0.8266218931139273, 1.5186494128635228, 2.0694639492597995, 2.446833466733069, 2.6666091661227647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8520318269729614})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0002977848052979})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9822722673416138})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0711767673492432})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.339627742767334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.159008502960205})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.438570261001587})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8696, 'crossentropy': 0.9396087890625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6809713840484619})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.5660667419433594})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5957765579223633})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.5698291659355164})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.5800514221191406})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 31404], ['id', 8027], ['id', 41299], ['id', 43796], ['ood', 59884]], 'labels': [3, 5, 3, 7, -1], 'scores': [0.8968504790782561, 1.5870256338111073, 2.131020825262029, 2.5132366534970023, 2.731873556086512]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0424774885177612})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9484944939613342})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1715359687805176})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.192407488822937})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.2009176015853882})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2382779121398926})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.2275886535644531})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.3523019552230835})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.4494590759277344})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.4251785278320312})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.3281421661376953})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.490905523300171})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.36903977394104})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.5128886699676514})
store['active_learning_steps'][11]['training']['best_epoch']=11
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 1.2297697265625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.7509233951568604})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5897024273872375})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.579139769077301})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5825157165527344})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5380508899688721})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5480033159255981})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5214067697525024})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5442037582397461})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 51286], ['id', 16951], ['id', 7768], ['id', 14473], ['id', 53673]], 'labels': [0, 8, 8, 6, 4], 'scores': [1.074511649110703, 1.981277032855035, 2.6685595491150664, 3.012601803320793, 3.1643240814506965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0243703126907349})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0400304794311523})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0979913473129272})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1533923149108887})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.246812343597412})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.2541462182998657})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.315234899520874})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.231189489364624})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.3333384990692139})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.263296365737915})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8759, 'crossentropy': 1.01591025390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.712726891040802})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.609186053276062})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5428563952445984})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5418387651443481})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5433824062347412})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5085762143135071})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5298160910606384})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5285259485244751})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5182579755783081})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 6604], ['id', 32169], ['id', 18018], ['id', 22621], ['id', 46814]], 'labels': [8, 2, 5, 1, 9], 'scores': [1.0093695829584273, 1.821012405501119, 2.443343158585443, 2.8206501927860392, 3.0164658894428094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8814370632171631})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9351085424423218})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8881304264068604})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9322422742843628})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8843921422958374})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9981459379196167})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9229469299316406})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0008225440979004})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.1599658727645874})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0445668697357178})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.813897998046875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6545349359512329})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5464308261871338})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5471199750900269})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.47524869441986084})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.47722744941711426})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5015814304351807})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.47256654500961304})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 22481], ['id', 58837], ['id', 19980], ['ood', 51018], ['id', 36606]], 'labels': [7, 8, 5, -1, 9], 'scores': [0.9389134455503523, 1.7516095143993908, 2.3867498611444242, 2.761852778613, 3.001791379939794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8436199426651001})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8006502985954285})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8958612680435181})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0132577419281006})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9780417084693909})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.241966724395752})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0078307390213013})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8977, 'crossentropy': 0.767208837890625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.721305787563324})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5488705635070801})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5261505842208862})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5358491539955139})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.538891077041626})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 20322], ['ood', 47078], ['id', 31710], ['ood', 52394], ['ood', 411]], 'labels': [1, -1, 8, -1, -1], 'scores': [0.9259732086864361, 1.6789308674159402, 2.2645617746485316, 2.6668094085428766, 2.895795563403164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8438037633895874})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.774776041507721})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9001445174217224})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9954806566238403})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0082361698150635})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9691089391708374})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1895160675048828})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.034876823425293})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0421593189239502})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8941, 'crossentropy': 0.87782353515625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6641640067100525})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5498380064964294})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5286544561386108})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5206775665283203})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5247331857681274})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.5184899568557739})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 24479], ['id', 59380], ['id', 22139], ['id', 48010], ['ood', 38890]], 'labels': [8, 8, 2, 7, -1], 'scores': [1.0418588488841038, 1.860417452120568, 2.4572662146552915, 2.82185813502114, 3.0229009510839466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.913447380065918})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8435232043266296})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7703424692153931})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9068228006362915})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9107613563537598})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8989461660385132})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8995, 'crossentropy': 0.69902373046875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7073830962181091})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5738387107849121})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5287627577781677})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5068168044090271})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.4914610981941223})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 51144], ['id', 14655], ['id', 32168], ['id', 5315], ['id', 27678]], 'labels': [5, 3, 5, 3, 8], 'scores': [0.8404107755975034, 1.584305321330469, 2.170529290590741, 2.5614060732798345, 2.78166798913108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9361881017684937})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.841238260269165})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.055976390838623})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8620728254318237})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0310300588607788})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 1.0571281909942627})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0570639371871948})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.31658935546875})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0019433498382568})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8982, 'crossentropy': 0.82731748046875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.726932168006897})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5722733736038208})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5257477164268494})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5274810194969177})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.4812927842140198})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.4697529077529907})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.492051899433136})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 16209], ['id', 8439], ['id', 8812], ['ood', 39314], ['id', 6390]], 'labels': [2, 9, 0, -1, 8], 'scores': [0.8987927135344556, 1.6424731525484275, 2.212067121080233, 2.5703768148190127, 2.7818573929876207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0327796936035156})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.865027666091919})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9411956071853638})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9836217761039734})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9468368887901306})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.966544508934021})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.0427567958831787})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 1.1213887929916382})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 1.1011282205581665})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0738155841827393})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.1502149105072021})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8941, 'crossentropy': 0.91297421875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.661636233329773})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5195997953414917})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5030484199523926})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.4860907793045044})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5060467720031738})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.508202314376831})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.45308032631874084})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.4740992784500122})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4567216634750366})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.4754336476325989})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 33161], ['id', 51600], ['id', 50981], ['ood', 23302], ['ood', 19837]], 'labels': [3, 4, 4, -1, -1], 'scores': [1.040871710397419, 1.8868678747966454, 2.5156692802969127, 2.877887074287428, 3.0677593274966455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9318606853485107})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7493621110916138})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8227725028991699})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.870836079120636})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.853670597076416})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9477401971817017})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.003722906112671})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.029064416885376})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8966, 'crossentropy': 0.795552294921875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6595872044563293})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5659136772155762})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.49115467071533203})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.4947482943534851})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.4594659209251404})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4450351595878601})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.4561569094657898})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 40702], ['id', 49202], ['id', 43282], ['id', 41924], ['id', 58472]], 'labels': [4, 5, 9, 9, 2], 'scores': [0.9123387135247478, 1.701434696997195, 2.321793956425865, 2.720840555421998, 2.9376457245697614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8918307423591614})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7452276945114136})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8205080032348633})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.754859447479248})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9184059500694275})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9093103408813477})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.947246789932251})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.67154560546875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6187942624092102})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5035287737846375})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.49133145809173584})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.4899081587791443})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.4586166739463806})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4507504105567932})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 37440], ['id', 20271], ['id', 16072], ['id', 37048], ['ood', 8522]], 'labels': [2, 8, 5, 9, -1], 'scores': [0.7682576610751028, 1.4680008228354389, 2.0262368971292544, 2.4142598971433564, 2.662696903027393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0468270778656006})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7629760503768921})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7952553033828735})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7363479137420654})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8320382237434387})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7949473857879639})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9484695196151733})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.928372323513031})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9287890195846558})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.68171982421875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6039614677429199})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5232279300689697})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.457758367061615})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4784620404243469})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4371339976787567})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4078338146209717})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.42111459374427795})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.43071722984313965})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 55496], ['id', 26947], ['id', 2148], ['id', 44854], ['ood', 33266]], 'labels': [9, 8, 6, 9, -1], 'scores': [0.8935773664378761, 1.680222741951534, 2.2590153641931616, 2.6312148125326527, 2.83341413989724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9326187372207642})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.72519850730896})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8353934288024902})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7621908783912659})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8044631481170654})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7377095222473145})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8915145397186279})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8413654565811157})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8772304058074951})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.69065712890625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6739367246627808})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5308396220207214})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4600200057029724})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.43395739793777466})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.43453848361968994})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.41046059131622314})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.41621506214141846})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 11213], ['id', 48292], ['id', 3862], ['id', 31310], ['id', 4282]], 'labels': [8, 2, 4, 0, 8], 'scores': [0.8735213877663529, 1.606230935633767, 2.222368379415252, 2.6302780433127593, 2.872956055953666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9605125188827515})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7745497226715088})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7384597063064575})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7977880239486694})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.754037618637085})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8494570255279541})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.59945185546875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7066820859909058})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5327103734016418})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5134437084197998})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.47882986068725586})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4503413438796997})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 33538], ['id', 52172], ['id', 34934], ['id', 19412], ['id', 57683]], 'labels': [0, 5, 7, 9, 9], 'scores': [0.737750373027185, 1.412433361148608, 1.945461641100179, 2.341762851443857, 2.58176741721328]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9661970138549805})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7243143320083618})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7645626664161682})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8767461776733398})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7947307825088501})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9378728270530701})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.85671067237854})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.988756537437439})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.6192423828125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6828208565711975})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5175007581710815})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.46121689677238464})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4365483820438385})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.44717174768447876})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.39305996894836426})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.38813960552215576})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 44684], ['id', 34847], ['id', 340], ['ood', 36850], ['id', 48948]], 'labels': [3, 0, 7, -1, 7], 'scores': [0.7752326555267048, 1.4913249726456779, 2.038892488839423, 2.43556883325068, 2.6927240760645237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1050560474395752})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6607652902603149})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6273280382156372})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6300966739654541})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7448434829711914})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7018095850944519})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6305053234100342})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.54751943359375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6122838854789734})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.49595803022384644})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.45558661222457886})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4145370125770569})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.43915289640426636})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.40042537450790405})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 49487], ['ood', 7949], ['id', 35246], ['ood', 43952], ['ood', 46116]], 'labels': [8, -1, 8, -1, -1], 'scores': [0.8730441485748339, 1.6583962301190258, 2.2273525958436764, 2.618926367641457, 2.86230242319324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0475267171859741})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6404788494110107})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.687955915927887})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6660952568054199})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6598507165908813})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6799736022949219})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7572991847991943})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6889691352844238})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.717154860496521})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6842344403266907})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.730817973613739})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.7274047136306763})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.766722559928894})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8091322183609009})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.860553503036499})
store['active_learning_steps'][26]['training']['best_epoch']=12
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.6159712890625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6363791823387146})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4733985364437103})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.41577786207199097})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.38754504919052124})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.38979506492614746})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3795081675052643})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 6044], ['ood', 14384], ['ood', 15494], ['id', 30267], ['ood', 57965]], 'labels': [2, -1, -1, 8, -1], 'scores': [0.9179907234518607, 1.6979593995460056, 2.340692923876138, 2.8019681417523987, 3.0621181960596244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2335844039916992})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7177718877792358})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6443020701408386})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6951977610588074})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6214615106582642})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.708538830280304})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7142543792724609})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7588775753974915})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.561533447265625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6328181028366089})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.493640273809433})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4425213634967804})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.42335212230682373})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4196421802043915})
store['active_learning_steps'][27]['eval_training']['best_epoch']=2
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 31046], ['id', 12655], ['id', 26444], ['id', 56717], ['id', 46534]], 'labels': [6, 9, 1, 1, 3], 'scores': [0.8042948803519532, 1.5310391114564625, 2.1033768114317892, 2.479422710197264, 2.684189237996735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0215013027191162})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6383475065231323})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6778525114059448})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.649500846862793})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6416293978691101})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6668299436569214})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6899119019508362})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7385588884353638})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7153737545013428})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7801799774169922})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9262, 'crossentropy': 0.582512255859375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6259313821792603})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.48907244205474854})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.43256986141204834})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4092857837677002})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.3859270513057709})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.36645209789276123})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3617739975452423})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.3620205521583557})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.38402044773101807})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 41334], ['ood', 2369], ['id', 3036], ['ood', 26568], ['ood', 40550]], 'labels': [9, -1, 6, -1, -1], 'scores': [0.9316894175583201, 1.732457449388991, 2.385757320981442, 2.8471033824778793, 3.114710842211247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8869813084602356})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6158647537231445})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6005377769470215})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5673099756240845})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6272015571594238})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6233243942260742})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6463215351104736})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6240367889404297})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6692014932632446})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6359203457832336})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7427005171775818})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7325711846351624})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.56808408203125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6341252326965332})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.48066240549087524})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4154031276702881})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.38113725185394287})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.37708401679992676})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.3794270157814026})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 49890], ['id', 42221], ['id', 52886], ['ood', 9692], ['id', 48966]], 'labels': [5, 5, 7, -1, 5], 'scores': [0.9036887891317742, 1.655643874880293, 2.25778006626913, 2.628676200840201, 2.8247734091622982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0425522327423096})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6154335737228394})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6534130573272705})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5926936864852905})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6049737930297852})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6898653507232666})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7186538577079773})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9292, 'crossentropy': 0.499540234375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6061409115791321})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.48579326272010803})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.425517737865448})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.43320202827453613})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4195009469985962})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3703938126564026})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 23350], ['id', 6466], ['ood', 7949], ['id', 41322], ['ood', 53128]], 'labels': [8, 2, -1, 5, -1], 'scores': [0.8512204407038069, 1.581026572194176, 2.0800456012739588, 2.4227466575472807, 2.635250187131165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.087348222732544})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6276662945747375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5360218286514282})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6151156425476074})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6337363719940186})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6667098999023438})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.5256275390625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6826868057250977})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5274081230163574})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.509793758392334})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4530888795852661})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.42401593923568726})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 55540], ['id', 52866], ['ood', 45550], ['id', 38796], ['id', 34058]], 'labels': [2, 7, -1, 6, 3], 'scores': [0.723841955841539, 1.3805313121961063, 1.9159019965316464, 2.3218994047805506, 2.600862502357879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9899059534072876})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6268658638000488})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5689974427223206})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6282622218132019})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.640100359916687})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6509552001953125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.641282320022583})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6792294383049011})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9295, 'crossentropy': 0.56794287109375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7475730776786804})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5058466196060181})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4389957785606384})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4197787344455719})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41976243257522583})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.40210115909576416})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.40777823328971863})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 18398], ['id', 14722], ['id', 38577], ['id', 0], ['ood', 43952]], 'labels': [4, 0, 5, 5, -1], 'scores': [0.8198081724723105, 1.5667384528724098, 2.146718543054539, 2.5552737175671885, 2.798724905244664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1234365701675415})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5814717411994934})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5555080771446228})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5504027009010315})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5441267490386963})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5998888611793518})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6674847602844238})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5865159034729004})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7030910849571228})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.651771068572998})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6959781646728516})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.468672705078125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6190341711044312})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4717845618724823})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.40683120489120483})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4092220366001129})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.34575769305229187})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.3853062093257904})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 40589], ['id', 34946], ['id', 42746], ['ood', 36647], ['ood', 13271]], 'labels': [2, 8, 2, -1, -1], 'scores': [0.8668010759324669, 1.6497933053332257, 2.25880483759515, 2.6148689377258787, 2.8196560690997234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0672087669372559})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.568825364112854})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5286272168159485})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5971908569335938})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.612816333770752})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6462593674659729})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6049438714981079})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6310211420059204})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.600310206413269})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5974287986755371})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.614985466003418})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6135899424552917})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9409, 'crossentropy': 0.48708642578125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6569133996963501})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.46902090311050415})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4180006980895996})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.37983301281929016})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.34073320031166077})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3599955439567566})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3505462110042572})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3441081643104553})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 6309], ['id', 26733], ['id', 1364], ['id', 46288], ['id', 2872]], 'labels': [3, 2, 9, 2, 1], 'scores': [0.8791287499093228, 1.6528394329589413, 2.227198506977773, 2.601668206582784, 2.8121625316165373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0202335119247437})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5260791778564453})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5940642952919006})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4649580717086792})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49432727694511414})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5657221078872681})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5847702026367188})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6095940470695496})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9381, 'crossentropy': 0.4488095703125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6108123064041138})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.45291227102279663})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4062897562980652})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.36086583137512207})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3825998306274414})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3531002402305603})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3460797369480133})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 30983], ['ood', 1925], ['ood', 36647], ['id', 41779], ['id', 39727]], 'labels': [5, -1, -1, 7, 6], 'scores': [0.7715520793197488, 1.4307436565949994, 1.970093686755411, 2.3748279598703474, 2.6339891552775168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0780755281448364})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5602887868881226})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49419450759887695})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5278879404067993})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5239652395248413})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5056185722351074})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5671285390853882})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5575658082962036})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9417, 'crossentropy': 0.438386083984375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5792423486709595})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.48601311445236206})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.415094792842865})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39321067929267883})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.36552366614341736})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3687748908996582})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3662705421447754})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 45954], ['id', 28844], ['ood', 36647], ['ood', 43952], ['ood', 21981]], 'labels': [8, 2, -1, -1, -1], 'scores': [0.8247201125876078, 1.5100133580429, 2.0815291206497566, 2.5196226575527625, 2.8070365656820524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9087182283401489})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5473456382751465})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.517416775226593})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5476211309432983})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.567507266998291})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6004461050033569})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6622684597969055})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5934611558914185})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7292469143867493})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.52179013671875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6744990348815918})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5282659530639648})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4509168863296509})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.38785412907600403})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.37140244245529175})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.39270421862602234})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.3857266902923584})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.39458662271499634})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 49222], ['id', 53873], ['id', 19942], ['id', 47597], ['id', 10227]], 'labels': [3, 4, 5, 8, 5], 'scores': [0.8414074216924108, 1.5765035220427999, 2.190739173608243, 2.630580468185088, 2.8863071566094245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0825471878051758})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5978041887283325})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6324756145477295})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5748241543769836})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6224383115768433})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6091946363449097})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6665157079696655})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6604909896850586})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6256550550460815})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6993058919906616})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7778900861740112})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7015695571899414})
store['active_learning_steps'][38]['training']['best_epoch']=9
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.53067724609375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6367941498756409})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4516056180000305})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.38804370164871216})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.3684166669845581})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.35787415504455566})
store['active_learning_steps'][38]['eval_training']['best_epoch']=2
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 28801], ['id', 7886], ['id', 47297], ['id', 44590], ['ood', 48735]], 'labels': [2, 9, 8, 7, -1], 'scores': [0.7795392783695152, 1.5010979243750109, 2.098364412230435, 2.533110293983918, 2.7960457684225446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.083660364151001})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.585098147392273})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.539766788482666})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4959825277328491})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.567818284034729})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5773340463638306})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5871522426605225})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9409, 'crossentropy': 0.4089142822265625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6721137166023254})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.45685839653015137})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.38663703203201294})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3884797692298889})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3703870475292206})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.37453794479370117})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 51212], ['id', 51544], ['id', 47288], ['id', 26785], ['id', 18598]], 'labels': [2, 1, 6, 6, 9], 'scores': [0.6463162931336869, 1.2618376618754898, 1.8027695439009546, 2.205902775491463, 2.484548396061105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.154813528060913})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.562568724155426})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5487037301063538})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5199282765388489})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.566447377204895})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5625874996185303})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5598675012588501})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9308, 'crossentropy': 0.433278173828125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6485260725021362})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5011705756187439})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4443037509918213})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43434539437294006})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4008609354496002})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4086746871471405})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 35996], ['ood', 26568], ['id', 37062], ['ood', 10350], ['ood', 3582]], 'labels': [9, -1, 9, -1, -1], 'scores': [0.6751849768580005, 1.2967360333181905, 1.8432751106617955, 2.247035693502231, 2.5412922564124827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9987618923187256})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5749197006225586})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49297869205474854})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4897004961967468})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5710923671722412})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5576328039169312})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.44773046875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7002969980239868})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5050279498100281})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4723624587059021})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4052169620990753})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.43659037351608276})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 22272], ['id', 5013], ['id', 52236], ['id', 57215], ['id', 14152]], 'labels': [5, 2, 9, 7, 7], 'scores': [0.6732461165061929, 1.2591818958867136, 1.7194631464559222, 2.0846695659827024, 2.325440683276156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.290001630783081})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5958858728408813})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5213843584060669})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4888257086277008})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4813305735588074})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5031204223632812})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5102469325065613})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5109965205192566})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5395383834838867})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5047163963317871})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49928849935531616})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5510574579238892})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5365371108055115})
store['active_learning_steps'][42]['training']['best_epoch']=10
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.465893359375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6196423768997192})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.44618675112724304})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38882437348365784})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3879435062408447})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3413189649581909})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.31298691034317017})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3028694987297058})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.33111053705215454})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3035634160041809})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.29369497299194336})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.29012489318847656})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2837875783443451})
store['active_learning_steps'][42]['eval_training']['best_epoch']=11
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 13829], ['id', 15191], ['ood', 46393], ['id', 32335], ['ood', 25264]], 'labels': [5, 0, -1, 1, -1], 'scores': [0.8934046670566707, 1.6537540116945761, 2.2212660441735412, 2.593197119850247, 2.7728327102659893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.204501748085022})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5870305299758911})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48683738708496094})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44143304228782654})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4707966446876526})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47458815574645996})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4687861502170563})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.42285224609375}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.59711092710495})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.476182222366333})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4206938147544861})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4268752336502075})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3821626305580139})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3807033598423004})
store['active_learning_steps'][43]['eval_training']['best_epoch']=4
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 12305], ['id', 43952], ['id', 36818], ['id', 24860], ['ood', 10299]], 'labels': [9, 3, 7, 9, -1], 'scores': [0.7983684445686734, 1.4588027785031215, 1.9948478748453535, 2.386687871599679, 2.6410268570445474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1732807159423828})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5897129774093628})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4615921080112457})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43857473134994507})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4644777476787567})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46572989225387573})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5248290300369263})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47208887338638306})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5850380063056946})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9471, 'crossentropy': 0.42664736328125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6292511224746704})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43914711475372314})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40561825037002563})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33177340030670166})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3154972195625305})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.33224254846572876})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30876871943473816})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3041001558303833})
store['active_learning_steps'][44]['eval_training']['best_epoch']=7
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 50461], ['id', 48586], ['id', 45784], ['id', 39575], ['id', 17326]], 'labels': [7, 5, 9, 8, 6], 'scores': [0.778573794522387, 1.4745291836217502, 2.040727802044108, 2.3813643565546974, 2.5791275577800095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.1115180253982544})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5519098043441772})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4597408175468445})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4177987277507782})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4653986692428589})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5131998062133789})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4763392210006714})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9402, 'crossentropy': 0.416631103515625}
