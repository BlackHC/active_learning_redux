store = {}
store['timestamp']=1622158917
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=30']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=30
store['worker_id']=30
store['num_workers']=40
store['config']={'seed': 1267, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.633850574493408})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.952152729034424})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.5820260047912598})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.543158531188965})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2393863201141357})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0953593254089355})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.1558358669281006})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6927, 'crossentropy': 2.441954296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 39253], ['id', 14655], ['id', 19042], ['id', 43880], ['id', 34623]], 'labels': [5, 3, 9, 8, 0], 'scores': [1.3065482885227757, 2.3392298044376543, 3.157917246441688, 3.731628274365887, 4.0936094460674415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.183485984802246})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.6233620643615723})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6982860565185547})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.815523147583008})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.892488956451416})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6758, 'crossentropy': 2.2833953125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 42805], ['id', 30103], ['id', 54851], ['id', 34422], ['id', 39494]], 'labels': [2, 9, 6, 8, 0], 'scores': [1.2556530707705738, 2.318385131947191, 3.130831197311723, 3.7104571176404066, 4.0738607318805835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.8609511852264404})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.140019416809082})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.251436710357666})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.6194591522216797})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.396301507949829})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.4336447715759277})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.5467236042022705})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.6746773719787598})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.6984896659851074})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.3705010414123535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.595313549041748})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.7420098781585693})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.276059627532959})
store['active_learning_steps'][2]['training']['best_epoch']=10
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7214, 'crossentropy': 2.263036328125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 49955], ['id', 16532], ['id', 53666], ['id', 51881], ['id', 8413]], 'labels': [3, 2, 7, 8, 2], 'scores': [1.3667059937214345, 2.4734012243299768, 3.33979508933478, 3.9319915522521267, 4.262326088247367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5835762023925781})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.8837532997131348})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.001816987991333})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.314877510070801})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.97257399559021})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.0655300617218018})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.4008092880249023})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.181102991104126})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.349374294281006})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.751, 'crossentropy': 1.9927935546875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 51762], ['id', 37089], ['id', 37974], ['id', 49448], ['id', 57286]], 'labels': [5, 5, 2, 6, 7], 'scores': [1.3543857550150369, 2.5503201496484866, 3.423210191326133, 3.975118887222533, 4.276374857279425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.2125314474105835})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.5723280906677246})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.8068289756774902})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.7696917057037354})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7632, 'crossentropy': 1.23769365234375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 48668], ['id', 55643], ['id', 15880], ['id', 12117], ['id', 14125]], 'labels': [8, 5, 5, 3, 2], 'scores': [1.1369839400123944, 2.1021587628425715, 2.880439923876618, 3.4713877077520383, 3.8713354324532787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.424565315246582})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.3975584506988525})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.485982894897461})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.5951496362686157})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.7173099517822266})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.737319827079773})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.6924866437911987})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.789, 'crossentropy': 1.54428828125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 49064], ['id', 11904], ['id', 53976], ['id', 39182], ['id', 47089]], 'labels': [8, 8, 9, 4, 4], 'scores': [1.2085926178845923, 2.234331950424397, 3.057923168995302, 3.670537239118702, 4.058368080108529]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5520570278167725})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.4561195373535156})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.6101675033569336})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.8263888359069824})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.9232560396194458})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.9423251152038574})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7953572273254395})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.9043397903442383})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7855, 'crossentropy': 1.8455419921875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 52086], ['id', 49179], ['id', 44944], ['id', 7033], ['id', 25910]], 'labels': [5, 2, 8, 7, 1], 'scores': [1.322668398921506, 2.4769858870057253, 3.29361308506121, 3.8446708739557627, 4.184304393205816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1584711074829102})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.3107296228408813})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.5298899412155151})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6100937128067017})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7829, 'crossentropy': 1.141828125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 49537], ['id', 6474], ['id', 30782], ['id', 28882], ['id', 44732]], 'labels': [2, 6, 9, 2, 6], 'scores': [0.9260831591808056, 1.7258721717327696, 2.407732916504971, 2.972978927726915, 3.423232944246773]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.209913730621338})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.318040370941162})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.490793228149414})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3900060653686523})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.6685453653335571})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8077, 'crossentropy': 1.24196171875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 53656], ['id', 7833], ['id', 7909], ['id', 49406], ['id', 26661]], 'labels': [2, 5, 8, 3, 8], 'scores': [1.0667819515622625, 2.0439052138187583, 2.8027050450299917, 3.410893585142996, 3.8180723121941202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0941773653030396})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1348432302474976})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.3259093761444092})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3499964475631714})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3841009140014648})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.611706018447876})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3920302391052246})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.5093629360198975})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8202, 'crossentropy': 1.35744326171875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 40434], ['id', 56184], ['id', 34508], ['id', 27874], ['id', 19586]], 'labels': [5, 4, 0, 2, 9], 'scores': [1.1911006531044623, 2.247647192833233, 3.0925146941615376, 3.6996110962383746, 4.091619358202761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0775387287139893})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1926536560058594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2953169345855713})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4230926036834717})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.382917881011963})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2829148769378662})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.377934217453003})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.5432820320129395})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.5049002170562744})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8268, 'crossentropy': 1.24078876953125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 27783], ['id', 51986], ['id', 22741], ['id', 26693], ['id', 9037]], 'labels': [3, 2, 3, 4, 3], 'scores': [1.1740827522088302, 2.233752462752529, 3.129089489520622, 3.723050692774793, 4.103213146587915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9329217076301575})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.047762155532837})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.050577998161316})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1036124229431152})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0028386116027832})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0707817077636719})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0823932886123657})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.295409917831421})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8595, 'crossentropy': 0.97117255859375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 134], ['id', 1454], ['id', 5600], ['id', 19942], ['id', 14769]], 'labels': [1, 0, 6, 5, 4], 'scores': [1.2256529174857005, 2.2636819866131073, 3.1381521657624125, 3.732292217123968, 4.122441813506368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1766877174377441})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.145094394683838})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3990094661712646})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5191054344177246})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.4662926197052002})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8256, 'crossentropy': 1.12303623046875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 8459], ['id', 23874], ['id', 3672], ['id', 50294], ['id', 38172]], 'labels': [5, 5, 2, 6, 6], 'scores': [1.0252162452927855, 1.8807213556156608, 2.630428916507695, 3.222079628408311, 3.649678966389298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9257111549377441})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9658037424087524})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0191831588745117})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1341331005096436})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1829979419708252})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2546265125274658})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8607, 'crossentropy': 0.971096484375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 28102], ['id', 35232], ['id', 30457], ['id', 17710], ['id', 12391]], 'labels': [0, 8, 1, 3, 7], 'scores': [1.0890415820633967, 2.078375260117874, 2.8992013634913167, 3.5307690514759003, 3.9625400983738004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8465591669082642})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.769359827041626})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7572870254516602})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8245776891708374})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8785895109176636})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9131985902786255})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9546687006950378})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 1.013124704360962})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.004840612411499})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0281188488006592})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8859995603561401})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8944, 'crossentropy': 0.8704935546875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 58313], ['id', 37521], ['id', 42004], ['id', 42020], ['id', 52319]], 'labels': [0, 5, 7, 9, 2], 'scores': [1.1447414224364003, 2.156021038594684, 3.0291811194370926, 3.6802846934091438, 4.096407548940512]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9849289655685425})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7493839263916016})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7447878122329712})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8115262985229492})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8615355491638184})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8361002802848816})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8501245975494385})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8834165334701538})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8469893336296082})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8328554630279541})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9165055155754089})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.0442297458648682})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8843231201171875})
store['active_learning_steps'][15]['training']['best_epoch']=10
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.777835009765625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 34328], ['id', 55834], ['id', 13709], ['id', 15216], ['id', 13374]], 'labels': [8, 9, 6, 3, 2], 'scores': [1.2814167078270193, 2.4167410252740673, 3.257904180019268, 3.854106223217057, 4.226821656746732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8960577845573425})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8181925415992737})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7925733327865601})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7926130890846252})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9655728340148926})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8423858880996704})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.934033989906311})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.882469892501831})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.865394115447998})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8973, 'crossentropy': 0.77908525390625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 18726], ['id', 57665], ['id', 27299], ['id', 47925], ['id', 31014]], 'labels': [4, 8, 8, 3, 8], 'scores': [1.200357220543435, 2.2575197865310748, 3.126463079247925, 3.7169261330170285, 4.112147605000492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9194682836532593})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7493833303451538})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7478196620941162})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7049423456192017})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8834625482559204})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9157993197441101})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9399170875549316})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.672205322265625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 21174], ['id', 20170], ['id', 41540], ['id', 37339], ['id', 46412]], 'labels': [2, 9, 2, 4, 0], 'scores': [1.0504131439433273, 2.0099806716697213, 2.823722595592571, 3.4677472518142496, 3.9178951157879665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9010144472122192})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6968615055084229})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8361940383911133})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8713655471801758})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8187093734741211})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7849999666213989})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7873626947402954})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8035135269165039})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8181154727935791})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9264830350875854})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.737676220703125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 11482], ['id', 21532], ['ood', 9866], ['id', 21307], ['id', 39016]], 'labels': [8, 5, -1, 4, 9], 'scores': [1.1986184798581336, 2.283355304414075, 3.182563291777183, 3.799628553340252, 4.170170365249746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8665279150009155})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6399790048599243})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6728839874267578})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6834728121757507})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6065278053283691})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5936980843544006})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6336027383804321})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.673512876033783})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7362706661224365})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7213699817657471})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.754239559173584})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.592848291015625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 31184], ['id', 17756], ['id', 38249], ['id', 3730], ['id', 17178]], 'labels': [9, 8, 8, 8, 8], 'scores': [1.2388369313177514, 2.33467961850384, 3.228531056427647, 3.8378435921015113, 4.198465442584267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8623046875})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.726121187210083})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7071157693862915})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7520632147789001})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8061548471450806})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7493846416473389})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7911779880523682})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7554244995117188})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7616801261901855})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8678982257843018})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8323259949684143})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7542666792869568})
store['active_learning_steps'][20]['training']['best_epoch']=9
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.70335859375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 51764], ['id', 57507], ['id', 52392], ['id', 41965], ['id', 44624]], 'labels': [5, 0, 1, 2, 8], 'scores': [1.3551738662967927, 2.5841443751777304, 3.394047580260004, 3.9168042230585245, 4.241274891241108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0518486499786377})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7249743938446045})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7704921960830688})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7276982665061951})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8149842023849487})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7910887002944946})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7807055711746216})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8891608715057373})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9036099910736084})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9793223142623901})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.767358349609375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 47036], ['ood', 7949], ['id', 18962], ['id', 9180], ['id', 39304]], 'labels': [2, -1, 7, 3, 4], 'scores': [1.1778651699869305, 2.208852815368723, 3.081987981379486, 3.7162015781982802, 4.120047439529409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9982478618621826})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6808643341064453})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6301124691963196})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5854550004005432})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6310224533081055})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6555660963058472})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7557591199874878})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7482062578201294})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7248072624206543})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9257, 'crossentropy': 0.57628974609375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 19868], ['id', 52462], ['id', 17518], ['id', 16117], ['id', 4822]], 'labels': [5, 9, 0, 9, 4], 'scores': [1.147425524386271, 2.2001207703918633, 3.023222651855818, 3.653651786090932, 4.036114895986859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0187780857086182})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.615290105342865})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6108043193817139})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6709492206573486})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6538040637969971})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6290032267570496})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8180732131004333})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7714624404907227})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7559350728988647})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.59249873046875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 10210], ['id', 46163], ['id', 44172], ['id', 13998], ['id', 49149]], 'labels': [3, 2, 8, 9, 3], 'scores': [1.1371080290903568, 2.138960630306852, 3.007114062023403, 3.6246759783139098, 4.01708583774891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9096047878265381})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6842688322067261})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.675663411617279})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.609662652015686})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6470136046409607})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7525956630706787})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7840477228164673})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.57214794921875}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 44753], ['id', 58046], ['id', 29899], ['id', 1518], ['id', 43043]], 'labels': [5, 8, 3, 9, 3], 'scores': [1.0181724482714993, 1.9462075216762496, 2.739310492937456, 3.3715728092916777, 3.8177508780441904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1001477241516113})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6739368438720703})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5473844408988953})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6120012998580933})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5885707139968872})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6274527311325073})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9201, 'crossentropy': 0.559696533203125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 48323], ['id', 59309], ['id', 47595], ['id', 59314], ['id', 1674]], 'labels': [2, 8, 7, 9, 9], 'scores': [0.8870865996177808, 1.690751648834202, 2.413737903695772, 3.007742873116901, 3.46682970920061]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2180068492889404})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7089184522628784})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7133792042732239})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.608931303024292})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6719905138015747})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.582219123840332})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6247650384902954})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7197993993759155})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.711050271987915})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9319, 'crossentropy': 0.56029287109375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 6920], ['id', 41333], ['id', 48681], ['id', 31637], ['id', 33505]], 'labels': [3, 1, 2, 5, 2], 'scores': [1.1281008786494304, 2.1488074970397824, 2.9797858491782936, 3.6113341017538483, 4.014333780119144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9389246702194214})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6334474682807922})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5505692958831787})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6476816534996033})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.624748706817627})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5535315871238708})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5851184129714966})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6116678714752197})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6563082933425903})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7383168935775757})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.48755908203125}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 35606], ['id', 1075], ['id', 13830], ['id', 49563], ['id', 20037]], 'labels': [2, 7, 0, 8, 8], 'scores': [1.1709373392347495, 2.2216361567137883, 3.0377606859143214, 3.6286023288681193, 4.027696117970471]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.3233054876327515})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7166176438331604})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6517569422721863})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.617401123046875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5979240536689758})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6813639402389526})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.615396826171875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 45616], ['id', 47513], ['id', 36818], ['id', 29850], ['id', 14787]], 'labels': [5, 0, 7, 7, 9], 'scores': [0.8943050738322298, 1.7189557109425717, 2.4715628880344642, 3.053289061098715, 3.516105668109274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0859013795852661})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6167265176773071})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5877051949501038})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5730950236320496})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5900980234146118})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.616881251335144})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5479567050933838})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6697980165481567})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9267, 'crossentropy': 0.550499365234375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 42428], ['id', 39668], ['id', 20183], ['id', 27898], ['id', 7510]], 'labels': [5, 8, 4, 2, 2], 'scores': [0.9842204775907071, 1.9177005075238305, 2.7098380437539387, 3.348842710664335, 3.8123889436884753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1720703840255737})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6483290195465088})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5919607877731323})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5325435996055603})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6120337247848511})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5540935397148132})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6777200698852539})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6284684538841248})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6482704877853394})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.50569560546875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 37078], ['id', 3762], ['id', 45911], ['id', 19244], ['id', 36417]], 'labels': [8, 8, 3, 9, 6], 'scores': [1.050247260484058, 2.0328613115526615, 2.88210364947299, 3.516547252307099, 3.948524976371859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2773022651672363})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6870794296264648})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5861458778381348})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6205562949180603})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6471004486083984})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6371198296546936})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7129342555999756})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.536584423828125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 262], ['id', 5013], ['id', 36892], ['id', 4185], ['id', 39383]], 'labels': [2, 2, 1, 2, 6], 'scores': [0.9739234422264671, 1.9079661602744626, 2.7209493809136145, 3.3459207967283078, 3.7893012255007754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0650255680084229})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6591334342956543})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5049939751625061})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5437222123146057})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5400750637054443})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5438107252120972})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5183373093605042})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5913998484611511})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5752700567245483})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9405, 'crossentropy': 0.4698224609375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 18398], ['id', 17079], ['id', 38698], ['id', 20172], ['id', 30883]], 'labels': [4, 6, 5, 4, 3], 'scores': [1.1084019334471122, 2.1157054086966363, 2.9324783856894383, 3.547548871668724, 3.963959893806206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0634491443634033})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6481733322143555})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5424715280532837})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4980545938014984})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45407578349113464})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.513813853263855})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5296701192855835})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5445655584335327})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.43984404296875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 12305], ['id', 11292], ['id', 15832], ['id', 28536], ['id', 14697]], 'labels': [9, 1, 9, 3, 8], 'scores': [1.0644047779378036, 2.02363874023753, 2.8249338224796166, 3.427851806802547, 3.8570561333642477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1234184503555298})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6616008281707764})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5595715045928955})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5278064608573914})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.569465696811676})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4928985834121704})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5942969918251038})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5798176527023315})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5258530974388123})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.530469536781311})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6182273626327515})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.670493483543396})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9379, 'crossentropy': 0.488996875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 7886], ['id', 5679], ['id', 20169], ['id', 41218], ['id', 11616]], 'labels': [9, 3, 4, 8, 7], 'scores': [1.0628106934650852, 2.0641746427434695, 2.937136809440201, 3.5681515920871396, 3.991433661050938]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0620367527008057})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5990180373191833})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6113298535346985})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.516109824180603})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5396530628204346})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5825908184051514})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5315693020820618})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5622296929359436})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.585279107093811})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5775026082992554})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.605208694934845})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9401, 'crossentropy': 0.483514306640625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 16600], ['id', 30900], ['id', 18150], ['id', 52294], ['id', 39656]], 'labels': [4, 5, 8, 0, 0], 'scores': [1.0694478476700604, 2.0603654815810426, 2.9254803051378406, 3.5637129112694, 3.988962916674497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.165401816368103})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6152426600456238})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5928263068199158})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5341296195983887})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5250720977783203})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5090752840042114})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49931418895721436})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5143402814865112})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5555136799812317})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5088715553283691})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9483, 'crossentropy': 0.452976953125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 57523], ['id', 18598], ['id', 42787], ['id', 18487], ['id', 4762]], 'labels': [3, 9, 4, 4, 3], 'scores': [1.1397658792833139, 2.1483941243285445, 3.020105367401417, 3.656082562789715, 4.043336235589363]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.3449625968933105})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7415689826011658})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.655725359916687})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5330513715744019})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6185159683227539})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5148181915283203})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5822742581367493})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5589010715484619})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6068732738494873})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9422, 'crossentropy': 0.45568447265625}
