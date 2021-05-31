store = {}
store['timestamp']=1622152571
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=14']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=40
store['config']={'seed': 1249, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 2625, 56375, 22165, 20350, 16705, 3104, 58157, 7672, 57628, 24955, 35449, 4392, 5054, 7440, 56948, 28760, 34172, 16313, 23212, 25919, 55429, 51813, 30924, 14633, 28201, 11507, 17913, 11074, 24895, 4767, 48148, 14171, 18558, 33286, 27499, 19827, 27920, 37395, 48625, 41252, 7065, 34629, 18243, 11835, 27995, 37107, 21343, 51827, 15813, 38541, 43697, 55006, 596, 9812, 28986, 44521, 55870, 14061, 8282, 7380, 1000, 23477, 13028, 32545, 39267, 42540, 21272, 56026, 56400, 30614, 54262, 35940, 54236, 16589, 10979, 10123, 4453, 44498, 29178, 48809, 35319, 1655, 19913, 47818, 33500, 47973, 13705, 17902, 10996, 24524, 53789, 14797, 45593, 26132, 13057, 54809, 46497, 48775, 55424, 18644, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 55756, 46830, 635, 56627, 32657, 57714, 25810, 47544, 1884, 47793, 31896, 55592, 3435, 593, 5528, 13276, 14346, 17616, 58154, 29599, 30056, 3310, 49922, 9149, 6649, 14179, 19367, 15737, 25862, 20997, 4628, 49688, 58121, 58195, 44984, 557, 24254, 20256, 73, 47800, 58597, 3654, 51595, 44770, 49011, 22234, 11879, 1598, 5126, 28599, 52960, 25229, 45948, 53088, 27951, 44271, 27228, 682, 48314, 48891, 50821, 41673, 37134, 24815, 20732, 21250, 27375, 46799, 19004, 30566, 23363, 23310, 56897, 3668, 16888, 26071, 37215, 46015, 16911, 6625, 10849, 46824, 27607, 1867, 3242, 31370, 17178, 10220, 2212, 14512, 52137, 11887, 34327, 32838, 7026, 57746, 3224, 6252, 10558, 17735, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 22358, 34946, 6813, 36904, 44888, 12007, 55858, 39980, 54402, 33141, 23870, 50154, 53426, 6475, 46564, 34918, 18663, 46197, 42355, 50818, 36267, 36808, 22584, 6080, 4649, 49435, 13747, 7502, 33598, 54981, 19447, 8385, 35203, 50441, 57902, 19646, 12098, 5936, 10717, 53294, 53890, 39518, 41116, 55461, 25240, 1374, 9963, 23929, 27484, 4029, 12479, 53292, 39139, 53298, 5620, 24736, 4636, 33892, 53174, 35959, 18936, 39749, 41522, 11781, 26569, 28967, 57105, 12554, 15265, 55274, 15973, 2588, 26221, 56608, 167, 56893, 31769, 49506, 45856, 41174, 40582, 36283, 39261, 50236, 41866, 285, 25987, 1973, 58280, 51326, 46709, 24491, 57632, 1310, 21205, 42101, 531, 48025, 36655, 24935, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 50194, 52963, 16271, 38213, 10828, 18273, 31975, 31311, 54054, 40243, 39381, 6630, 31438, 6147, 28916, 56381, 33299, 18415, 5961, 12193, 43087, 23632, 22144, 21672, 36740, 14547, 9806, 54939, 28881, 25421, 30741, 2175, 50909, 35677, 12178, 53257, 39218, 38091, 47579, 34370, 13439, 19595, 55576, 56197, 40802, 56510, 28286, 50811, 10129, 3892, 20833, 48127, 12878, 46523, 36855, 6875, 44817, 23950, 24903, 9425, 48256, 8254, 45391, 39847, 42253, 56339, 37723, 38777, 30241, 10971, 21922, 8774, 36473, 23150, 38179, 56391, 7939, 12060, 22915, 41651, 37998, 43003, 1090, 36099, 37147, 9615, 32933, 55156, 33635, 3402, 45790, 50916, 16662, 21191, 31194, 2611, 54774, 55101, 3758, 54892, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 3709, 9781, 46968, 31397, 29555, 55175, 15673, 14290, 33762, 40666, 14384, 51908, 5551, 49268, 40059, 20360, 18726, 9712, 46454, 13375, 29523, 42951, 7436, 19249, 53737, 19803, 53549, 31951, 24172, 34725, 3407, 42277, 23409, 2819, 3478, 32271, 17781, 1718, 15640, 11471, 2963, 16560, 36583, 21114, 29746, 14911, 57994, 19042, 37311, 28603, 15607, 10656, 33854, 4372, 40592, 21159, 20438, 25226, 50966, 29345, 7397, 47611, 31797, 58477, 4905, 46117, 4419, 30486, 30565, 21436, 30434, 25057, 19339, 39134, 24, 43044, 41721, 21140, 16680, 58184, 21059, 48838, 30805, 14792, 23833, 55777, 44517, 33702, 32223, 36440, 17125, 1798, 4294, 36038, 22953, 131, 25387, 1404, 55763, 30976, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 37160, 11876, 23949, 21688, 37925, 16017, 43264, 32212, 58503, 5033, 46286, 55379, 7346, 51319, 13009, 44856, 42527, 36918, 7188, 36444, 27539, 8732, 45093, 46214, 10944, 43719, 8144, 47368, 42345, 533, 885, 35160, 4315, 27760, 14655, 36990, 56143, 298, 36342, 32619, 35325, 10416, 7209, 52218, 27035, 46442, 936, 15914, 27694, 853, 24594, 54672, 30280, 48535, 3718, 31172, 37166, 53842, 52135, 46999, 14299, 9492, 29143, 9509, 31683, 54045, 31978, 8812, 23461, 57617, 18691, 29159, 27843, 35562, 58137, 47976, 9262, 15695, 6656, 14588, 11449, 21085, 49763, 14964, 53386, 36034, 6776, 40684, 33071, 44897, 10080, 38989, 8023, 11937, 17622, 58383, 18222, 35423, 51119, 42288, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 46954, 22300, 57349, 46623, 6185, 46896, 29000, 31241, 31868, 38705, 56946, 30256, 58835, 10240, 51568, 29384, 6529, 49736, 33160, 27941, 52563, 48403, 8780, 37263, 52883, 30755, 58265, 32229, 17853, 39933, 57497, 21731, 3384, 19347, 26867, 37892, 1079, 24394, 29257, 49532, 9469, 52741, 53387, 50581, 51558, 6157, 29087, 37621, 47908, 11193, 20073, 35322, 55115, 23368, 26082, 15354, 32114, 5769, 28359, 7620, 35245, 7568, 43693, 16448, 753, 47087, 259, 34418, 13754, 41591, 27185, 15216, 26934, 5894, 15358, 39889, 56440, 22797, 40723, 56994, 53335, 34858, 17041, 16106, 976, 172, 31586, 31472, 27409, 53011, 3953, 10186, 55975, 19842, 32698, 37281, 46892, 36870, 26755, 24725, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 52458, 34197, 11303, 13660, 55451, 46116, 55235, 53785, 31491, 29189, 11047, 27637, 3619, 45141, 31030, 34049, 31495, 48793, 10215, 6887, 45579, 17463, 46718, 1961, 52765, 42127, 54526, 7874, 36390, 22013, 50237, 31006, 9607, 29520, 7953, 19334, 57583, 16987, 48255, 57785, 46688, 41002, 18412, 37806, 30835, 15191, 49710, 8134, 28801, 9793, 5020, 34908, 20118, 38121, 21485, 2285, 42450, 36284, 43946, 12225, 55215, 36771, 39648, 12396, 37484, 16525, 42662, 34105, 25033, 25764, 28497, 51015, 14993, 7617, 36974, 2327, 25011, 21093, 55355, 25498, 53817, 30984, 47064, 14602, 43197, 27046, 49662, 54031, 29595, 34598, 48760, 45007, 26256, 23100, 47867, 4163, 12574, 25371, 50941, 26042, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 54758, 48445, 34594, 18688, 36031, 28194, 47501, 36735, 18823, 41525, 31754, 34237, 8467, 24619, 21925, 9775, 17811, 5305, 22221, 33973, 4699, 50312, 3923, 1062, 21680, 55999, 28980, 49962, 30680, 13545, 53195, 44469, 33176, 49737, 20781, 45757, 55496, 28483, 2042, 45869, 19302, 43571, 18934, 25849, 28114, 58321, 40707, 43648, 33395, 58023, 19425, 21201, 31068, 30442, 43836, 54710, 58405, 4600, 28560, 49517, 42532, 58881, 26218, 39144, 50865, 28715, 30147, 2300, 28487, 12203, 27746, 18682, 735, 55575, 10461, 15705, 23617, 17459, 13420, 18395, 55261, 57155, 31031, 22172, 44032, 24681, 29360, 56205, 23961, 39770, 27602, 16963, 10441, 50093, 14604, 44570, 7746, 53607, 6044, 32827, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669, 54915, 11218, 8072, 31739, 182, 1476, 51529, 35233, 36022, 5755, 42529, 41979, 32557, 58190, 57651, 5046, 38958, 26198, 42297, 7054, 50917, 41280, 46294, 4749, 6695, 34103, 31630, 27770, 54740, 58159, 32315, 51557, 9487, 52740, 17523, 50736, 5739, 48635, 27685, 50299, 7956, 52754, 45588, 13029, 158, 7768, 24321, 19637, 1910, 14199, 56842, 41977, 19371, 48736, 22070, 52876, 55704, 31464, 44828, 4065, 55119, 11007, 58031, 22333, 41366, 52676, 26944, 42075, 5652, 44522, 20677, 54158, 45932, 43793, 49131, 27048, 35740, 44407, 58407, 42587, 12667, 13572, 33111, 32568, 13155, 12295, 12773, 2676, 49685, 57549, 48591, 46508, 3235, 27900, 58434, 7078, 58506, 44419, 44968, 6891]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1137166023254395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2941315174102783})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.829442024230957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3553199768066406})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7571659088134766})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6892, 'crossentropy': 2.0950228515625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 35350], ['id', 50500], ['id', 31360], ['id', 33749], ['id', 1364]], 'labels': [5, 3, 2, 5, 9], 'scores': [1.2307744586193117, 2.282540997176583, 3.0755919696235274, 3.63468708438898, 3.9981167690351143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.2535336017608643})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.181300640106201})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.0975236892700195})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.3956823348999023})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.1516690254211426})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6625, 'crossentropy': 2.7121130859375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 7979], ['id', 19298], ['id', 27302], ['id', 27641], ['id', 18137]], 'labels': [8, 6, 7, 2, 0], 'scores': [1.232567200775499, 2.291487831041961, 3.138132921781219, 3.728092851415317, 4.0967860462266605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.814634084701538})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.2518770694732666})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.3039064407348633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.4202804565429688})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.718, 'crossentropy': 1.712512109375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 14655], ['id', 19641], ['id', 19942], ['id', 22567], ['id', 12196]], 'labels': [3, 9, 5, 3, 2], 'scores': [1.249400602084899, 2.257285748274203, 3.0045389949135615, 3.560498371388231, 3.956202246969566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.9717793464660645})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8589633703231812})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.137234687805176})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.4699254035949707})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2798309326171875})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7301, 'crossentropy': 1.729548046875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 44882], ['id', 5702], ['id', 23734], ['id', 1563], ['id', 8027]], 'labels': [9, 3, 5, 2, 5], 'scores': [1.2241253008851691, 2.2061760495042684, 3.0044840562103845, 3.6057338076061347, 4.002571687940546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.677764654159546})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8714991807937622})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.0714499950408936})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3132896423339844})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.4932920932769775})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7274, 'crossentropy': 1.7397212890625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 5175], ['id', 45826], ['id', 58312], ['id', 12285], ['id', 27069]], 'labels': [4, 5, 5, 4, 0], 'scores': [1.203937478631301, 2.1969960625689158, 2.9157750441966144, 3.4653063692310244, 3.8542647114959587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.2486348152160645})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.5804288387298584})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.671482801437378})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.7232427597045898})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7689, 'crossentropy': 1.16416064453125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 57736], ['id', 30646], ['id', 59731], ['id', 24716], ['id', 3791]], 'labels': [8, 9, 5, 5, 2], 'scores': [1.03295561377954, 1.8979139696300464, 2.584930735509073, 3.1521305073029993, 3.5947218045483753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.5473004579544067})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8295505046844482})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.3338780403137207})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.5886569023132324})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.406843662261963})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7506, 'crossentropy': 1.556386328125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 56472], ['id', 30441], ['id', 27429], ['id', 20857], ['id', 59101]], 'labels': [7, 1, 0, 7, 8], 'scores': [1.0010570602279287, 1.8923859699600118, 2.669771671227066, 3.277594425652194, 3.7196390174800484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3371996879577637})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.498025894165039})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.3908286094665527})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6461375951766968})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.142444610595703})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.8834139108657837})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.968409538269043})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.9380738735198975})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.9905436038970947})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 2.2139205932617188})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.932884931564331})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.385491132736206})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 2.0194544792175293})
store['active_learning_steps'][7]['training']['best_epoch']=10
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8035, 'crossentropy': 1.7204353515625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 21219], ['id', 39593], ['id', 24589], ['id', 11708], ['id', 2765]], 'labels': [2, 9, 8, 3, 0], 'scores': [1.1977885158373787, 2.292845497090786, 3.209768581460203, 3.8572956225859993, 4.218380697871975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2166200876235962})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.426997423171997})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.668318271636963})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.7833664417266846})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.5324082374572754})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.623577356338501})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.2509841918945312})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.172469139099121})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.6770343780517578})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8343, 'crossentropy': 1.3414126953125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 37048], ['id', 14825], ['id', 44898], ['id', 19524], ['id', 27503]], 'labels': [9, 3, 2, 2, 2], 'scores': [1.2401253638983432, 2.2863321651364927, 3.1624176215138764, 3.7641743085173935, 4.153666551839967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.1929142475128174})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.4687936305999756})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.7683944702148438})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.9570155143737793})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.9504308700561523})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.7560350894927979})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.9854261875152588})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.1648831367492676})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.9701459407806396})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.05255126953125})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8032, 'crossentropy': 1.5487451171875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 12337], ['id', 15973], ['id', 20322], ['id', 17079], ['id', 54077]], 'labels': [0, 8, 1, 6, 3], 'scores': [1.2388390864492447, 2.3354649229194875, 3.210653895385235, 3.8010399259586016, 4.165700348957809]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1380772590637207})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.2205758094787598})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.5331618785858154})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.5573168992996216})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.5911037921905518})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8062, 'crossentropy': 1.0658728515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 46832], ['id', 34328], ['id', 8978], ['id', 39963], ['id', 57632]], 'labels': [7, 8, 2, 4, 2], 'scores': [0.9822875030290998, 1.888240345156436, 2.6806105792490875, 3.2947107621182443, 3.7307251077374133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.1393307447433472})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.18972647190094})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.487470030784607})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3481099605560303})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3841569423675537})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.5735387802124023})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5307624340057373})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.6716147661209106})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8337, 'crossentropy': 1.20385498046875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 13827], ['id', 56440], ['id', 27972], ['id', 14649], ['id', 23849]], 'labels': [3, 4, 8, 0, 7], 'scores': [1.1720764904574512, 2.2010824247723675, 3.0386819168187653, 3.6760277139744666, 4.079163590182638]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0765933990478516})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0933208465576172})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2876243591308594})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3524036407470703})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2040181159973145})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4436577558517456})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.279894471168518})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.206110954284668})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3676345348358154})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.5653162002563477})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.314685344696045})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3237338066101074})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 2.0438950061798096})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.932878017425537})
store['active_learning_steps'][12]['training']['best_epoch']=11
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8549, 'crossentropy': 1.1365599609375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 32880], ['id', 33013], ['id', 36286], ['id', 33388], ['id', 54573]], 'labels': [0, 5, 4, 8, 2], 'scores': [1.2203631665625803, 2.317178431092362, 3.1866544293910852, 3.8248484054034844, 4.185983779417233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.051345705986023})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.140953540802002})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.122415542602539})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.3272374868392944})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2746236324310303})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3958420753479004})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8617, 'crossentropy': 0.8883345703125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 57728], ['id', 20230], ['id', 29132], ['id', 1985], ['id', 14722]], 'labels': [9, 4, 8, 6, 0], 'scores': [1.0575274737714075, 1.965352433160704, 2.7296251481108325, 3.330754603867316, 3.7657091218494774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9014132618904114})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8819600343704224})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9593120813369751})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0354206562042236})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9947145581245422})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9898800253868103})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8772, 'crossentropy': 0.7810703125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 35864], ['id', 41718], ['id', 21315], ['id', 14290], ['id', 24479]], 'labels': [5, 8, 8, 4, 8], 'scores': [1.0786465861273948, 2.00271980042187, 2.79674253533648, 3.391470489972729, 3.82453082734241]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9943808317184448})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9305962920188904})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9954960346221924})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9991282224655151})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1226741075515747})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1260437965393066})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2329652309417725})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2234188318252563})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1718703508377075})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8666, 'crossentropy': 0.9478095703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 46616], ['id', 3370], ['id', 25466], ['id', 39668], ['id', 30444]], 'labels': [8, 4, 5, 8, 6], 'scores': [1.193453776559627, 2.272680882363587, 3.178643485852035, 3.8103413362488956, 4.178385804192058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9427633285522461})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8872578144073486})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8750228881835938})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0183167457580566})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1444132328033447})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0146867036819458})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0578691959381104})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.186936378479004})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2089462280273438})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1646932363510132})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3320562839508057})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8744, 'crossentropy': 0.959682421875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 36126], ['id', 10925], ['id', 17777], ['id', 58036], ['id', 4797]], 'labels': [5, 6, 3, 0, 8], 'scores': [1.2405896522934161, 2.360232299699651, 3.2695918253173364, 3.883643859214036, 4.220872187793398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9448299407958984})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7412548065185547})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7367943525314331})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7557622194290161})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8439195156097412})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9390571117401123})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8646714687347412})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.640277490234375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 16572], ['id', 7033], ['id', 602], ['id', 8214], ['id', 13548]], 'labels': [4, 7, 8, 7, 4], 'scores': [1.1255991153269995, 2.127775072838807, 2.9709789035344993, 3.6023503004303183, 4.0072507776621755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9033987522125244})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6379215717315674})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.718421459197998})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7358768582344055})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7773745059967041})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7380261421203613})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9043, 'crossentropy': 0.63979580078125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 53872], ['id', 36984], ['id', 59314], ['id', 34495], ['id', 35962]], 'labels': [8, 5, 9, 2, 6], 'scores': [1.0769524347778623, 2.0380892406979747, 2.8672056356800555, 3.4820669704746186, 3.908224201101733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0530152320861816})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6723417043685913})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7054309844970703})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7987399101257324})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7013323307037354})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7728906869888306})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7994312047958374})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.862041711807251})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8201875686645508})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.634433642578125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 46088], ['id', 6474], ['id', 9687], ['id', 3810], ['id', 14279]], 'labels': [6, 6, 0, 3, 8], 'scores': [1.0762698591600623, 2.071523835980275, 2.8924104219135742, 3.5214725918922385, 3.952593523391048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9945074319839478})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6716481447219849})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6850101947784424})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6730128526687622})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7614962458610535})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6735655665397644})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7137367725372314})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7600222229957581})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8084458112716675})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7563724517822266})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7834402322769165})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8129074573516846})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8387587070465088})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.924616813659668})
store['active_learning_steps'][20]['training']['best_epoch']=11
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.685281787109375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 46368], ['id', 28371], ['id', 49515], ['id', 42070], ['id', 42931]], 'labels': [8, 3, 2, 3, 3], 'scores': [1.2290326376056453, 2.348717276183307, 3.2181953957060045, 3.848914499663554, 4.210745482746788]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0257370471954346})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6684420108795166})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6681971549987793})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7129650115966797})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7198895215988159})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.6083447265625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 6894], ['id', 45602], ['id', 51764], ['id', 48397], ['id', 1239]], 'labels': [3, 5, 5, 5, 8], 'scores': [0.9095616320253155, 1.748772577904358, 2.4737582771336726, 3.0480172051902095, 3.488295270412097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0881574153900146})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7182698249816895})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6181749105453491})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7137047648429871})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6559725999832153})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6748312711715698})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.56100126953125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 58976], ['id', 45047], ['id', 42221], ['id', 35196], ['id', 33812]], 'labels': [5, 2, 5, 7, 6], 'scores': [0.9873753744732925, 1.8811526778313685, 2.639070134374772, 3.241465097605446, 3.694378514201425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1114888191223145})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.662185549736023})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6007653474807739})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5562838315963745})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.663751482963562})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.657384991645813})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.707948625087738})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9235, 'crossentropy': 0.524044091796875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 57665], ['id', 21636], ['id', 25462], ['id', 4822], ['id', 28757]], 'labels': [8, 2, 6, 4, 3], 'scores': [0.9735499270433905, 1.853690461213664, 2.6082782817942913, 3.227962355884957, 3.68910390015286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0865392684936523})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5724056959152222})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5277175307273865})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5774447321891785})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5706758499145508})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6298284530639648})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6348230838775635})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.649451732635498})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.608407199382782})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.632167398929596})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5991083383560181})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6182081699371338})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7265599966049194})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6188075542449951})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6404285430908203})
store['active_learning_steps'][24]['training']['best_epoch']=12
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.62720869140625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 12297], ['id', 47870], ['id', 48360], ['id', 31512], ['id', 47220]], 'labels': [9, 9, 3, 2, 6], 'scores': [1.2995513769017326, 2.4302016710125685, 3.344418422058233, 3.9008452574616514, 4.237548527103988]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2471269369125366})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7902668714523315})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5989788770675659})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6354100704193115})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.665958046913147})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6779487133026123})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6198193430900574})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.542285009765625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 20169], ['id', 28632], ['id', 42209], ['id', 11600], ['id', 36268]], 'labels': [4, 7, 9, 2, 5], 'scores': [1.0187844068436784, 1.9699364962736432, 2.771741188930177, 3.372153911807777, 3.8003635362903454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2009453773498535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6552111506462097})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6149918437004089})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6214070320129395})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6828464269638062})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.631887353515625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 1127], ['id', 29899], ['ood', 25624], ['id', 17756], ['id', 5679]], 'labels': [7, 3, -1, 8, 3], 'scores': [0.7998964590374371, 1.521394265179362, 2.1829519747195567, 2.7357967396796017, 3.192169913901342]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.3240857124328613})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6722251772880554})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6020254492759705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5989245176315308})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6415121555328369})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7246193885803223})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6869215965270996})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.56326240234375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 46126], ['id', 18487], ['id', 43224], ['id', 1812], ['id', 59747]], 'labels': [3, 4, 3, 4, 5], 'scores': [1.0492426662252659, 2.040178429647791, 2.8874446703647623, 3.503599176448791, 3.9218844268994966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3794758319854736})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6875886917114258})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5674508810043335})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6491376161575317})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5887959599494934})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6294693946838379})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7013987302780151})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6977198719978333})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7338075637817383})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.56538193359375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 7789], ['id', 42703], ['id', 5536], ['id', 43176], ['id', 52169]], 'labels': [1, 0, 8, 2, 2], 'scores': [1.1286174726912803, 2.15108375467004, 2.9959181738310043, 3.610487693812323, 4.020460530169668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1868386268615723})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6178694367408752})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5474972724914551})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6255587339401245})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6118606328964233})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6216709613800049})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.642509937286377})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.553415673828125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 47513], ['id', 13942], ['id', 31308], ['id', 24300], ['id', 42428]], 'labels': [0, 4, 8, 9, 5], 'scores': [0.9743920292990407, 1.8632961589419867, 2.629649329168423, 3.2531408787955307, 3.7050109459208374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.253678321838379})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5824823379516602})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5637302398681641})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.588568925857544})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5564562678337097})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.560615625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 43206], ['id', 34481], ['id', 26072], ['id', 37574], ['id', 8443]], 'labels': [5, 3, 1, 5, 2], 'scores': [0.746114865309806, 1.443031427497853, 2.094000255645156, 2.661423575837821, 3.129229489222908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3834567070007324})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6332001686096191})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5270454287528992})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5367596745491028})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5053540468215942})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5463486909866333})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6036383509635925})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5489796996116638})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6175394058227539})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9379, 'crossentropy': 0.51581640625}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 34828], ['id', 8853], ['id', 1573], ['id', 16676], ['id', 52674]], 'labels': [-1, 2, 2, 3, 6], 'scores': [0.9821379063369959, 1.9172342761788808, 2.710045500636177, 3.3499519417580483, 3.8004378257106417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2511506080627441})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6575729250907898})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5245037078857422})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5267240405082703})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5907167196273804})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5880920886993408})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5930948853492737})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.51754375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 31014], ['id', 8405], ['id', 43560], ['id', 34520], ['id', 17549]], 'labels': [8, 3, 5, 6, 0], 'scores': [0.978567637217185, 1.885425532213152, 2.654170486678365, 3.2556997062347106, 3.7001536228556944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.1459872722625732})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.607923150062561})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.526034951210022})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5382242202758789})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5587248206138611})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.534178614616394})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.583569347858429})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6197789907455444})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5728667974472046})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.51022822265625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 46132], ['id', 23423], ['id', 56014], ['id', 3692], ['id', 40066]], 'labels': [7, 9, 5, 7, 4], 'scores': [1.0710554041463938, 1.9908050055289088, 2.7599794109514413, 3.36289232727294, 3.8116267684502994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4333255290985107})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.699413537979126})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5467045307159424})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5072965621948242})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5276323556900024})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5370668172836304})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.50900126953125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 56006], ['id', 21532], ['id', 8459], ['id', 5762], ['id', 39561]], 'labels': [3, 5, 5, 2, 2], 'scores': [0.8933824001273825, 1.6921942483143093, 2.405340944719586, 3.0114083475743065, 3.4853473518216127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.341062307357788})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6847656965255737})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6085259914398193})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5383669137954712})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.539967954158783})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5416642427444458})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5269898176193237})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.519052294921875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 22083], ['id', 32519], ['id', 59335], ['id', 21700], ['id', 20150]], 'labels': [2, 5, 4, 7, 3], 'scores': [0.9551285221666592, 1.8193265984330154, 2.594780928806361, 3.2018813331534535, 3.6610984352428524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3416833877563477})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6026774048805237})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5557994842529297})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5145414471626282})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5011008977890015})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5665597915649414})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5408321619033813})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5325130224227905})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9342, 'crossentropy': 0.50151845703125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 39818], ['id', 6582], ['ood', 53990], ['id', 32513], ['id', 53324]], 'labels': [1, 8, -1, 4, 9], 'scores': [1.0259745574996995, 1.9453734725027663, 2.7171924942003196, 3.3273990420025417, 3.762985820055208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2585878372192383})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6742384433746338})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5654051303863525})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.509019136428833})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5143125653266907})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5156533718109131})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5108529925346375})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5120280981063843})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.576257586479187})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.574466347694397})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9455, 'crossentropy': 0.4324650390625}
