store = {}
store['timestamp']=1622162756
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=38']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=38
store['worker_id']=38
store['num_workers']=40
store['config']={'seed': 1276, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.32376766204834})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5265793800354004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.035111904144287})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1663146018981934})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6967, 'crossentropy': 2.0929498046875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36281], ['id', 24038], ['id', 54851], ['id', 50517], ['id', 36559]], 'labels': [7, 1, 6, 4, 5], 'scores': [1.1895951721906277, 2.2047796310070877, 2.990669162933073, 3.5693851900963995, 3.950426343160368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.2441813945770264})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.436980962753296})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.0566868782043457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9856855869293213})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.913038730621338})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7089, 'crossentropy': 2.049301171875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 46707], ['id', 1290], ['id', 9437], ['id', 8700], ['id', 32591]], 'labels': [2, 3, 9, 3, 8], 'scores': [1.168071581779319, 2.144996494908235, 2.9562021505340157, 3.5451332903292885, 3.9348843751710856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.5211858749389648})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.029961109161377})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.181145429611206})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2193100452423096})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7446, 'crossentropy': 1.43948759765625}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 25301], ['id', 29368], ['id', 56348], ['id', 16959], ['id', 36642]], 'labels': [8, 0, 9, 5, 5], 'scores': [1.0860971912382973, 1.9772037240996991, 2.7408804470928274, 3.331049181287833, 3.7559161434088306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.5068984031677246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.7026290893554688})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.7875347137451172})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.032472610473633})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.055917263031006})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.1749496459960938})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7747, 'crossentropy': 1.56703642578125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 13464], ['id', 7768], ['id', 52971], ['id', 12196], ['id', 23790]], 'labels': [0, 8, 2, 2, 6], 'scores': [1.2076791861545295, 2.2223826553156343, 3.023907130427247, 3.643651572309629, 4.040315715327637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3203096389770508})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.6804120540618896})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5285024642944336})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.692795991897583})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7495245933532715})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7219325304031372})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.7450224161148071})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.875499963760376})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7814, 'crossentropy': 1.7324232421875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 19569], ['id', 39266], ['id', 7924], ['id', 32533], ['id', 55268]], 'labels': [2, 8, 8, 5, 8], 'scores': [1.3037741767641158, 2.3735058439617585, 3.2088368108487675, 3.7955272734491183, 4.146841678109089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3426246643066406})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.6100850105285645})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.7657265663146973})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.870725154876709})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7792, 'crossentropy': 1.20338349609375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 59275], ['id', 11154], ['id', 41714], ['id', 43978], ['id', 6418]], 'labels': [3, 5, 4, 3, 5], 'scores': [0.9394080473287232, 1.7866469520776995, 2.530784405355047, 3.143812773136572, 3.5835876447200974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2496477365493774})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.5968194007873535})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.656750202178955})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.8287348747253418})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.9152607917785645})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.8847451210021973})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.8948631286621094})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.9808647632598877})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.816022276878357})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7923, 'crossentropy': 1.7289275390625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 4831], ['id', 1341], ['id', 45845], ['id', 50090], ['id', 42139]], 'labels': [9, 3, 2, 4, 4], 'scores': [1.2969807533885696, 2.3570339007013903, 3.229123520156664, 3.8265149075858425, 4.18962775314305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2809276580810547})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.517404556274414})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6141663789749146})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.8162617683410645})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.6015517711639404})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.0067265033721924})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.802, 'crossentropy': 1.47479580078125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 48166], ['id', 23104], ['id', 11513], ['id', 14978], ['id', 7979]], 'labels': [7, 0, 3, 2, 8], 'scores': [1.207560218747571, 2.2065458270622966, 3.0393350680982927, 3.655529550996299, 4.058922788283477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1892192363739014})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2013421058654785})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3160995244979858})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2198749780654907})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.551246166229248})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4810764789581299})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8301, 'crossentropy': 1.1869361328125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 10768], ['id', 40221], ['id', 48356], ['id', 18227], ['id', 3691]], 'labels': [4, 2, 2, 3, 0], 'scores': [1.0946665939248215, 2.1033254799072014, 2.925661824283919, 3.5425855069461445, 3.9662959009175545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3199549913406372})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.341278076171875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.6280969381332397})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.5073370933532715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.4483208656311035})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.634847640991211})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8790473937988281})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.7865872383117676})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8282, 'crossentropy': 1.2827966796875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 40589], ['id', 56041], ['id', 36127], ['id', 3795], ['id', 9948]], 'labels': [2, 9, 2, 7, 8], 'scores': [1.123568445391274, 2.1832604896773287, 3.0552711849715415, 3.674801150311877, 4.080062871696188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0581859350204468})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2553373575210571})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3669885396957397})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.463560700416565})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.6505978107452393})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5851283073425293})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8362, 'crossentropy': 1.14990234375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 16488], ['id', 670], ['id', 29132], ['id', 969], ['id', 18150]], 'labels': [9, 3, 8, 7, 8], 'scores': [1.0801203213990092, 2.1027966579449866, 2.954434933499325, 3.609242863665581, 4.008336136284491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.3086841106414795})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.4472527503967285})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.5263181924819946})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5796518325805664})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.6938729286193848})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.8837659358978271})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.993932843208313})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.9288772344589233})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8153, 'crossentropy': 1.53936357421875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 31301], ['id', 22083], ['id', 55834], ['id', 19298], ['id', 58560]], 'labels': [5, 2, 9, 6, 0], 'scores': [1.315539231771715, 2.3577435716186748, 3.2139459109423907, 3.8032353177680367, 4.1596467126406225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1103317737579346})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2183657884597778})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3474810123443604})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.4628043174743652})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4795594215393066})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4254894256591797})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.4722883701324463})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.5563075542449951})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.838, 'crossentropy': 1.25853017578125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 12305], ['id', 13991], ['id', 38974], ['id', 26434], ['id', 9180]], 'labels': [9, 5, 1, 2, 3], 'scores': [1.1983142614274065, 2.2584204651181174, 3.1161396029352932, 3.7467574380022235, 4.131600783030552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.078697919845581})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.13529372215271})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2735381126403809})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.3683966398239136})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.4102237224578857})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3290272951126099})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.444680094718933})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4787838459014893})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.4759891033172607})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.7385363578796387})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3868403434753418})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.4583618640899658})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.30389404296875})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.6865140199661255})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.7574520111083984})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.754072666168213})
store['active_learning_steps'][13]['training']['best_epoch']=13
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8554, 'crossentropy': 1.2197166015625}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 5103], ['id', 424], ['id', 54720], ['id', 45917], ['id', 2242]], 'labels': [2, 9, 1, 9, 6], 'scores': [1.1885809903148643, 2.2915831602931886, 3.1640323689378302, 3.781681650233776, 4.167053221651043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9917569756507874})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0290749073028564})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0707652568817139})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.174797773361206})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.133440613746643})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0936110019683838})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0805820226669312})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.141340970993042})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.260380744934082})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8773, 'crossentropy': 0.91103310546875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 8859], ['id', 224], ['id', 6236], ['id', 34429], ['id', 54065]], 'labels': [8, 1, 6, 4, 7], 'scores': [1.2347064119021507, 2.2950520949777173, 3.1533284449159398, 3.7476759950738536, 4.132651394289154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9911932349205017})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.865431547164917})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8376916646957397})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9280841946601868})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9941577315330505})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8662476539611816})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9830259084701538})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1604609489440918})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9697766900062561})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.751755908203125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 14043], ['id', 38409], ['id', 5679], ['id', 28420], ['id', 26733]], 'labels': [2, 2, 3, 1, 2], 'scores': [1.1911884304536744, 2.2598938554565664, 3.162801536472288, 3.791027530639976, 4.148708765242748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9765086770057678})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8529054522514343})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8681796193122864})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9679974913597107})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0302159786224365})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1320853233337402})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8773, 'crossentropy': 0.7482404296875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 33674], ['id', 34520], ['id', 11708], ['id', 17005], ['id', 42362]], 'labels': [5, 6, 3, 1, 0], 'scores': [0.9584658381793671, 1.845802902595227, 2.6076266840034457, 3.2216109848601135, 3.67917351645837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8889996409416199})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7867414355278015})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8815898895263672})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.777362585067749})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7994197607040405})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8822368383407593})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.969947874546051})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.678048095703125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 14761], ['id', 35946], ['id', 43745], ['id', 49548], ['id', 16072]], 'labels': [3, 4, 8, 8, 5], 'scores': [1.0552622986554194, 1.9928125205858604, 2.816543851895794, 3.460354559185917, 3.888024825317167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0666673183441162})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7395550012588501})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7121221423149109})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8548694849014282})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8741870522499084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8512988090515137})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.593765185546875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 13742], ['id', 59314], ['id', 39656], ['id', 3494], ['id', 11586]], 'labels': [9, 9, 0, 7, 8], 'scores': [0.9543125373488937, 1.8446397235721994, 2.5754056166459254, 3.178151947848068, 3.62271799683288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9448080062866211})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7067835330963135})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8220865726470947})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7747002840042114})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8070527911186218})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.917371392250061})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8544833660125732})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9932422637939453})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.66022666015625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 28040], ['id', 17934], ['id', 7168], ['id', 55739], ['id', 37403]], 'labels': [5, 4, 8, 5, 2], 'scores': [1.105135081479486, 2.1382262277042123, 2.9576690321909593, 3.57916343569474, 3.993165594182658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9403570890426636})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.639643132686615})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7260057926177979})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7040330171585083})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7594457864761353})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8159706592559814})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8397244811058044})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.73304682970047})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7239937782287598})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8323609828948975})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9520224332809448})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.5963876953125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 3810], ['ood', 50403], ['id', 1239], ['id', 31090], ['id', 33612]], 'labels': [3, -1, 8, 4, 7], 'scores': [1.1400824318952036, 2.1385272233423294, 2.995371597769058, 3.6340418350398833, 4.044972183354356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.129516839981079})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7512211799621582})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6943099498748779})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7182772159576416})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.684467077255249})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7487014532089233})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7185991406440735})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6940364837646484})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7610653638839722})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.722305178642273})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7828636765480042})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.820858359336853})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8583580255508423})
store['active_learning_steps'][21]['training']['best_epoch']=10
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.56844775390625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 52097], ['id', 48102], ['id', 43702], ['id', 18143], ['id', 39320]], 'labels': [1, 7, 3, 9, 6], 'scores': [1.2905840649769682, 2.342045739145243, 3.189653391738137, 3.768493421545532, 4.137670827538524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9613958597183228})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7364140748977661})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6968157291412354})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6643815636634827})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7701507806777954})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.751214325428009})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6963707208633423})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7815810441970825})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7772525548934937})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8789314031600952})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.561717041015625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 8714], ['id', 45462], ['id', 56324], ['id', 42444], ['id', 52140]], 'labels': [9, 2, 3, 0, 4], 'scores': [1.204270374040564, 2.2283195713199913, 3.0673605332882223, 3.675138099781032, 4.077933248515571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0231727361679077})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7084919214248657})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5714934468269348})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.660043478012085})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7594690322875977})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7135695219039917})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8013252019882202})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6953514814376831})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.723095715045929})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7580668330192566})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7148886919021606})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.552737060546875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 36409], ['id', 4165], ['id', 25384], ['id', 52319], ['id', 31624]], 'labels': [3, 2, 5, 2, 9], 'scores': [1.162347028049055, 2.1850114722593403, 3.037186122175406, 3.658275496432193, 4.053594920290527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9269504547119141})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6208462715148926})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5321226716041565})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.543027400970459})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6015535593032837})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6611990928649902})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5937246084213257})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9293, 'crossentropy': 0.485861962890625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 29493], ['id', 39480], ['id', 22480], ['id', 55128], ['id', 31063]], 'labels': [8, 9, 4, 8, 2], 'scores': [0.994473523161584, 1.9031873665063217, 2.6906779543029167, 3.298256602780829, 3.7513613488631563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0257513523101807})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.655109167098999})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6074381470680237})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5923880338668823})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5521883964538574})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5794384479522705})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6998364925384521})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6167689561843872})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5559529066085815})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.46564697265625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 52838], ['id', 19188], ['id', 20169], ['id', 17382], ['id', 22154]], 'labels': [4, 1, 4, 6, 3], 'scores': [1.2111988814002288, 2.236468481067524, 3.0803586997347763, 3.6809542668121704, 4.0617882402575685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.984147310256958})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6086397767066956})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.570360541343689})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5892941951751709})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5868072509765625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5122733116149902})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6739577054977417})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5516022443771362})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.563770055770874})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9404, 'crossentropy': 0.439952587890625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 55743], ['id', 19590], ['id', 58832], ['ood', 27540], ['id', 46580]], 'labels': [3, 5, 3, -1, 6], 'scores': [1.0433021899360395, 2.046353664742874, 2.874227560446654, 3.4900430467206043, 3.910434063339233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0317168235778809})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6189719438552856})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5899972915649414})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5424251556396484})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6017687916755676})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5787266492843628})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6140854954719543})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.464720068359375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 17404], ['ood', 27540], ['id', 37469], ['id', 10005], ['id', 19362]], 'labels': [3, -1, 2, 0, 8], 'scores': [1.0109457475331278, 1.9550476042829192, 2.7330042575665097, 3.3203838870243363, 3.7517526230952534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9510452747344971})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5916211009025574})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5425426959991455})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5413414239883423})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5422940254211426})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5468084812164307})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6716581583023071})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9399, 'crossentropy': 0.423292724609375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 19942], ['id', 52179], ['id', 36783], ['id', 44202], ['id', 24479]], 'labels': [5, 0, 0, 8, 8], 'scores': [1.0535233649444948, 2.0114667658680263, 2.7657671644712662, 3.357955499809104, 3.79953679654371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.996447741985321})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5717807412147522})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45571208000183105})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.526817798614502})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49603283405303955})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49952441453933716})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.445033837890625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 26358], ['id', 2548], ['id', 17048], ['id', 22561], ['id', 5684]], 'labels': [3, 4, 0, 6, 6], 'scores': [0.9163845415559635, 1.7569645690327542, 2.511301993597021, 3.092432977970777, 3.539839720326464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.086539626121521})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5641563534736633})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4880690574645996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4928070306777954})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5878974199295044})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5003136396408081})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4696279764175415})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5035359859466553})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5139429569244385})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5285053253173828})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9483, 'crossentropy': 0.4085734375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 5188], ['id', 59286], ['id', 58471], ['id', 12651], ['ood', 37583]], 'labels': [5, 8, 5, 9, -1], 'scores': [1.1326385804422539, 2.164538218815796, 3.0035869520225678, 3.586504461421945, 3.9828016233399257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.122389316558838})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6349858045578003})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5243314504623413})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5188289880752563})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5094450116157532})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4961276650428772})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5160878896713257})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5401595830917358})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5270723104476929})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.555160641670227})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5332741737365723})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6078590154647827})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.416774951171875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 5308], ['id', 25055], ['id', 14896], ['id', 51004], ['id', 6174]], 'labels': [7, 3, 8, 7, 9], 'scores': [1.1128293830050828, 2.124966972584189, 2.97289523406997, 3.5964817647580274, 4.025820686032501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1101932525634766})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6050847172737122})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4955090880393982})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.510161280632019})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4511866867542267})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4740654230117798})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46598634123802185})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43635255098342896})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4794807434082031})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5086355805397034})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49620068073272705})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.498646080493927})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49889078736305237})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5392301082611084})
store['active_learning_steps'][32]['training']['best_epoch']=11
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9504, 'crossentropy': 0.419270263671875}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 5355], ['id', 4822], ['id', 49539], ['id', 35864], ['id', 37704]], 'labels': [-1, 4, 6, 5, 8], 'scores': [1.183209478221886, 2.2545797290923444, 3.1328576261083256, 3.7513246899307973, 4.1425511773887855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9784932136535645})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5054407119750977})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4627264738082886})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42681217193603516})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4371337890625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4824984073638916})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4840787649154663})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4559261202812195})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4592490494251251})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5074161291122437})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5246966481208801})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9501, 'crossentropy': 0.39599248046875}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 54530], ['id', 49187], ['id', 43126], ['id', 31293], ['id', 36834]], 'labels': [-1, 7, 3, 8, 8], 'scores': [1.093824569667684, 2.0889773740296436, 2.944481340509933, 3.5914591439595025, 4.01107295986874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0701994895935059})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5521113872528076})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4898837208747864})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43833571672439575})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4454936385154724})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38832780718803406})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4178963005542755})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43911176919937134})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45321762561798096})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4392679035663605})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4434044361114502})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9559, 'crossentropy': 0.3736485107421875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 19495], ['id', 20630], ['ood', 27540], ['id', 9687], ['id', 53872]], 'labels': [3, 8, -1, 0, 8], 'scores': [1.0911554137344837, 2.090597611181211, 2.916402744538664, 3.5238166173874284, 3.949127006433571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.2154496908187866})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5594552755355835})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46086084842681885})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4311057925224304})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.462646484375})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4710148870944977})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42730146646499634})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9514, 'crossentropy': 0.37863525390625}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 25624], ['id', 42078], ['id', 42703], ['ood', 29376], ['id', 57718]], 'labels': [-1, 4, 0, -1, 7], 'scores': [0.9487212988196414, 1.8324015400888887, 2.5523875259522946, 3.1493989738655, 3.6056888925484483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.047745943069458})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5870633125305176})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5354673862457275})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47641998529434204})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48865842819213867})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46707630157470703})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5247339010238647})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.43945950269699097})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48563650250434875})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4154123067855835})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5411515235900879})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9567, 'crossentropy': 0.3826205810546875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 13428], ['id', 24300], ['id', 8228], ['id', 18487], ['id', 38172]], 'labels': [9, 9, 3, 4, 6], 'scores': [1.0358522568134099, 2.000334565794573, 2.8440326349703327, 3.486139358563463, 3.9269503625481246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2091317176818848})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5356578230857849})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39964330196380615})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4293357729911804})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4161643981933594})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4529514014720917})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9495, 'crossentropy': 0.4034925048828125}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 20869], ['id', 55244], ['id', 37696], ['id', 16043], ['id', 50317]], 'labels': [3, 7, 2, 0, 3], 'scores': [0.9453009548156064, 1.799063935680536, 2.508623297147559, 3.076784712217787, 3.514677222027112]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2553081512451172})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6486034393310547})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4347119927406311})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42971572279930115})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4243309199810028})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4879164397716522})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.419464111328125})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.417244017124176})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42690062522888184})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46376749873161316})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.48520904779434204})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9544, 'crossentropy': 0.375988330078125}
