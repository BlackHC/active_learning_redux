store = {}
store['timestamp']=1622159645
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=31']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=31
store['worker_id']=31
store['num_workers']=40
store['config']={'seed': 1268, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5693359375, 'crossentropy': 2.5655386447906494})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.3853378295898438})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.422015905380249})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.6770973205566406})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.792202949523926})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.6287386417388916})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.973806142807007})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.025975227355957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 4.001963138580322})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3930678367614746})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.130727767944336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.890848398208618})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.151583671569824})
store['active_learning_steps'][0]['training']['best_epoch']=10
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5951, 'crossentropy': 4.014674609375}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 39046], ['ood', 49491], ['ood', 48926], ['id', 27863], ['ood', 52752]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.5427768891260976, 2.7191495764268185, 3.6249959645146532, 4.133310374100874, 4.400564725448359]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.4661014080047607})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.9520769119262695})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.471898078918457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.572042942047119})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.670741081237793})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.8715367317199707})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.9098408222198486})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.6023647785186768})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.837563991546631})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.892331600189209})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.200363636016846})
store['active_learning_steps'][1]['training']['best_epoch']=8
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5952, 'crossentropy': 4.03064453125}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 45794], ['ood', 20087], ['id', 51163], ['ood', 47842], ['ood', 11326]], 'labels': [-1, -1, 0, -1, -1], 'scores': [1.6200243540465658, 2.850286534178308, 3.6992545670738224, 4.187773612736802, 4.412406208882722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.10740327835083})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.0087013244628906})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.182939052581787})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.201164722442627})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.0770463943481445})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.326650619506836})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5962, 'crossentropy': 3.543812890625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 56094], ['ood', 32065], ['ood', 51288], ['ood', 45209], ['ood', 43173]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5758973871565494, 2.703063674921789, 3.6101629881658077, 4.115580515050176, 4.366434655090745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.4215567111968994})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0516653060913086})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.617824077606201})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.9199934005737305})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.914632797241211})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5899, 'crossentropy': 3.1715013671875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 21931], ['ood', 30123], ['ood', 40378], ['ood', 12813], ['ood', 32459]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.573959816193696, 2.8070920351462743, 3.637380628112184, 4.112909256463954, 4.35474682848368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.3121166229248047})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.016075849533081})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.3834681510925293})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.223034381866455})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.5414648056030273})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5915, 'crossentropy': 3.1323451171875}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 19931], ['ood', 46194], ['ood', 40198], ['id', 45510], ['ood', 54547]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.6334739254066264, 2.7134886955259985, 3.460354747242877, 3.979881073114398, 4.259132722106472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.800215721130371})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.570772171020508})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 3.8342318534851074})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 4.001279830932617})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5645, 'crossentropy': 2.772964453125}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 55178], ['id', 18729], ['ood', 6088], ['ood', 43993], ['id', 38902]], 'labels': [-1, 3, -1, -1, 5], 'scores': [1.3191679403102912, 2.2973256476292603, 3.0611990565027307, 3.6089081774481198, 3.981486028968199]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 2.6735401153564453})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.320974349975586})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.725522041320801})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 4.0149054527282715})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 4.280905723571777})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5769, 'crossentropy': 3.678071875}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 12223], ['ood', 2034], ['ood', 14836], ['ood', 16590], ['ood', 424]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4249552466596183, 2.512411819154436, 3.376471779937715, 3.932227541569187, 4.253218754882683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.340822219848633})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.063847303390503})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 4.001707077026367})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.4119629859924316})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 4.128416061401367})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5797, 'crossentropy': 3.37157734375}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 39130], ['ood', 8509], ['ood', 55964], ['ood', 47595], ['ood', 56701]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3996366547946177, 2.624747877884496, 3.473745473726357, 3.9973154440621483, 4.300056579640819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.5636510848999023})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.121847152709961})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.439906120300293})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.21884822845459})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4780592918395996})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.221195697784424})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.262446403503418})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.694779396057129})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 4.380002021789551})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.388951778411865})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.339141368865967})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5987, 'crossentropy': 4.415187109375}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 41354], ['ood', 52274], ['ood', 58235], ['ood', 33007], ['ood', 8134]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5486081929873383, 2.8218970530057437, 3.677876169799326, 4.165616530356356, 4.419738030012933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.3151397705078125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9102118015289307})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.099323272705078})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6255574226379395})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4638381004333496})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5991, 'crossentropy': 3.278791015625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 8645], ['ood', 4226], ['ood', 51216], ['ood', 14619], ['ood', 15456]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3762173372616782, 2.5042883524383996, 3.3510421959622043, 3.8838570582400322, 4.196668846828031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.572795867919922})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.3794803619384766})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.4589219093322754})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.7980895042419434})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.8917055130004883})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5918, 'crossentropy': 3.43975625}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 45794], ['id', 23510], ['ood', 8385], ['ood', 16911], ['ood', 33727]], 'labels': [-1, 1, -1, -1, -1], 'scores': [1.4805263431667974, 2.5406232979916865, 3.3446683836276234, 3.884355795348913, 4.181932574017756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.2703423500061035})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.011855125427246})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.3476691246032715})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.7472009658813477})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.637683391571045})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.068284511566162})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.7198190689086914})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.2132649421691895})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6017, 'crossentropy': 4.16663203125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 48373], ['ood', 28810], ['ood', 8611], ['ood', 6724], ['ood', 44543]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6882855306049276, 2.9845358545895673, 3.8422805732753673, 4.269525000298155, 4.460210727912578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.2252683639526367})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.956040859222412})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.346004009246826})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.926492691040039})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.6707329750061035})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 4.074356555938721})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 4.364915370941162})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.085843563079834})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6111, 'crossentropy': 3.823332421875}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 20098], ['ood', 24328], ['ood', 24940], ['ood', 21448], ['ood', 14418]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6030872678208254, 2.874428136228424, 3.8100290059475617, 4.247370839516713, 4.440420542762734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.494413375854492})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.3224527835845947})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.4561264514923096})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.7346982955932617})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.180876731872559})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.0064849853515625})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.5913, 'crossentropy': 3.50959140625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 37326], ['ood', 20087], ['ood', 21668], ['ood', 1239], ['ood', 14405]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4737774349582216, 2.6860990777172775, 3.5198404262039054, 4.053983818668291, 4.318284742562635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.493593215942383})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.243016242980957})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.9177331924438477})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.1122875213623047})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.336894989013672})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.272467613220215})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.259824752807617})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6026, 'crossentropy': 3.45044453125}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 26382], ['ood', 36553], ['ood', 7113], ['ood', 38796], ['ood', 31638]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.595730330623697, 2.7295117748764346, 3.6043585730563237, 4.072757830929457, 4.3667060708941]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.222754955291748})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.9919750690460205})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.154270648956299})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.455367088317871})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.945089340209961})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.154649257659912})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.134923458099365})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6038, 'crossentropy': 3.5404796875}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 48373], ['ood', 5387], ['ood', 33272], ['ood', 14807], ['ood', 20894]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5095812141594074, 2.700050852209527, 3.58896653229751, 4.113723134855302, 4.381391653832743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.32985782623291})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.7770533561706543})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.310248374938965})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.0552144050598145})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.141141176223755})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6034, 'crossentropy': 2.870296484375}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 21797], ['ood', 27247], ['ood', 38796], ['ood', 32854], ['ood', 40386]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2915727547481368, 2.356711193152475, 3.1639762318039075, 3.760083426817385, 4.111018384781776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.4992971420288086})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.029792308807373})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.7811384201049805})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.686657667160034})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.821131706237793})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.095740795135498})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 4.429743766784668})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.412106513977051})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 4.339888572692871})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5873, 'crossentropy': 4.351555859375}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 5118], ['ood', 4041], ['ood', 32459], ['ood', 56936], ['ood', 3471]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5884296033407947, 2.8645926288724777, 3.7264625025468323, 4.204172378692717, 4.426198323995371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.18792724609375})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.118809223175049})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3077330589294434})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.423794746398926})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.028430461883545})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.097297191619873})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6002, 'crossentropy': 3.491025390625}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 49144], ['ood', 20013], ['ood', 45462], ['ood', 23884], ['ood', 54487]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.463432227422636, 2.657119743518349, 3.519288313945702, 4.047647495101601, 4.345023811347771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 2.8074355125427246})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.341763734817505})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.6872963905334473})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.623687982559204})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.8948371410369873})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.97383975982666})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.5901, 'crossentropy': 3.85629765625}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 21797], ['ood', 26382], ['ood', 56567], ['ood', 18989], ['ood', 51216]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4733421000926679, 2.6314518861551752, 3.503233870024644, 4.04825354302181, 4.344037886201356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 2.6855478286743164})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.97780179977417})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.1008124351501465})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.698622703552246})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.763427257537842})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.9233899116516113})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.267979145050049})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.397078990936279})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.5988, 'crossentropy': 4.02504609375}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 30421], ['ood', 31677], ['ood', 48018], ['ood', 29340], ['ood', 51216]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.496279963738019, 2.7585540603489127, 3.69944661160266, 4.189781834319674, 4.427811796701903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.0514745712280273})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.9655208587646484})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.0657153129577637})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.42331600189209})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.6492981910705566})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.7730884552001953})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.288952350616455})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.013410568237305})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 4.143712043762207})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.231907844543457})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.621, 'crossentropy': 3.34584765625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 28501], ['ood', 38195], ['ood', 12035], ['ood', 42396], ['ood', 59389]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6551512590339632, 2.8735872573714394, 3.7388841962260013, 4.223228996791525, 4.451783093697694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.3220767974853516})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.0806174278259277})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0553765296936035})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.410212516784668})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.838062286376953})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.9713900089263916})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 4.295585632324219})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.689842224121094})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.9588873386383057})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.281802654266357})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.5979, 'crossentropy': 4.234330859375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 9118], ['ood', 30811], ['ood', 52322], ['ood', 36810], ['ood', 13085]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5700704898602673, 2.7902683876595136, 3.6546364466222148, 4.1705832726704335, 4.4116394086887425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 2.6345772743225098})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 3.3133339881896973})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.5988569259643555})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 4.233860969543457})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.668729782104492})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.2682671546936035})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.115976333618164})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.666093826293945})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.5895, 'crossentropy': 3.85536796875}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 38898], ['ood', 59441], ['ood', 31650], ['ood', 50608], ['ood', 8411]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5797383100829763, 2.8747362619225756, 3.7291993865564503, 4.204857927354558, 4.426436222178163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 2.4133832454681396})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.477262496948242})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.702479839324951})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.7842016220092773})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.171520233154297})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.008152961730957})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.274209022521973})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.5977, 'crossentropy': 3.9443015625}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 30421], ['ood', 45462], ['ood', 9003], ['ood', 49058], ['ood', 3980]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.497777341242591, 2.6318228591847523, 3.5211867006672204, 4.061796819808041, 4.3420921194648265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.5250110626220703})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 3.1559462547302246})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.454883575439453})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.984854221343994})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.883127450942993})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.7051591873168945})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.24538516998291})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.8609671592712402})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 4.552094459533691})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 4.178733825683594})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.879541397094727})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6614673137664795})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 4.413684844970703})
store['active_learning_steps'][25]['training']['best_epoch']=10
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.5964, 'crossentropy': 4.489945703125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 45794], ['ood', 41985], ['ood', 24176], ['ood', 53666], ['ood', 23086]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6539146794312312, 2.910062941684557, 3.798973543673637, 4.280090309165303, 4.479850684122839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.441920042037964})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.6608173847198486})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.251997947692871})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.5495409965515137})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4500014781951904})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.033418655395508})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6646790504455566})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.864182949066162})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 4.928989410400391})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.302318096160889})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6093, 'crossentropy': 4.0836484375}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 26382], ['ood', 33630], ['ood', 21061], ['ood', 25627], ['ood', 29681]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.69679937388208, 3.007727536867803, 3.8751418153499877, 4.270278425767826, 4.473756636208439]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.41037654876709})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.380699872970581})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3889408111572266})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.8020284175872803})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.97483491897583})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.511849403381348})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.5768, 'crossentropy': 3.538520703125}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 2034], ['ood', 35960], ['ood', 10321], ['ood', 5684], ['ood', 41713]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4931616755846302, 2.639840431346723, 3.541357305677521, 4.011108688551985, 4.3063342856301885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.1483101844787598})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.9341487884521484})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.1216721534729004})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.5003323554992676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.6955151557922363})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 4.193123817443848})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.5912, 'crossentropy': 3.360054296875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 44904], ['ood', 46441], ['ood', 42198], ['ood', 24602], ['ood', 20087]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3779081619559277, 2.5729102869306946, 3.426156569401547, 3.9788586743941794, 4.283553490130265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.2650837898254395})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.320594072341919})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.261009693145752})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4263975620269775})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.455516338348389})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.7245306968688965})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.082120418548584})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.5935, 'crossentropy': 3.50713203125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 20997], ['ood', 14661], ['ood', 58390], ['ood', 33591], ['ood', 18185]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.534223338399201, 2.7143565254568847, 3.5478643705163133, 4.063420744765862, 4.347934973828596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5654296875, 'crossentropy': 2.6797847747802734})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 2.9736533164978027})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.8534531593322754})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.116046905517578})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.467674732208252})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 4.142514705657959})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 4.083930969238281})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.5723, 'crossentropy': 3.355053515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 21817], ['ood', 24968], ['ood', 1865], ['ood', 11045], ['ood', 36427]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.448145603517034, 2.637161929991003, 3.509262707941371, 4.064458879477531, 4.33683241473075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.5446858406066895})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6118836402893066})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.0982275009155273})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.300483226776123})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.4233009815216064})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.3765439987182617})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.482269287109375})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.8838248252868652})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.702440023422241})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.4314279556274414})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6135, 'crossentropy': 3.93361171875}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 52012], ['ood', 26255], ['id', 13381], ['ood', 5896], ['ood', 50082]], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.5331438190337643, 2.848747103934137, 3.711230713251915, 4.177021824435525, 4.412830817389819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.3449432849884033})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.7002086639404297})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.2601494789123535})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.108508586883545})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.781054735183716})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6146, 'crossentropy': 2.8364505859375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 53290], ['ood', 1954], ['ood', 55329], ['ood', 13318], ['ood', 18215]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4248825470024769, 2.584888996515288, 3.4439369445919734, 3.966727463150307, 4.276615288846303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.3799185752868652})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.31193470954895})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.2636942863464355})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.7457733154296875})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 4.1538238525390625})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6089, 'crossentropy': 3.2717154296875}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 52322], ['ood', 40376], ['ood', 44712], ['ood', 38662], ['ood', 11256]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4773505422698159, 2.577689873180288, 3.4018499986064796, 3.933975246823193, 4.268738898356773]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.1362924575805664})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6522364616394043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2132205963134766})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2909107208251953})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1933064460754395})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.4039053916931152})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.5670948028564453})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.645, 'crossentropy': 3.299305859375}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 41468], ['ood', 36949], ['ood', 37753], ['id', 33586], ['ood', 16590]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.5512289434151798, 2.787072270851908, 3.67649963774472, 4.165581138714909, 4.396609541541761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.204253911972046})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0598249435424805})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1237053871154785})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.21774959564209})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.3033156394958496})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.54947566986084})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6271, 'crossentropy': 3.22829609375}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 25662], ['ood', 15476], ['ood', 45199], ['ood', 54316], ['ood', 39558]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6425008877016731, 2.8817760439496247, 3.761143413363407, 4.2118824381304965, 4.430093625750352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.2165966033935547})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6229474544525146})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0098915100097656})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9867420196533203})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.384449005126953})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1189327239990234})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6335, 'crossentropy': 3.03957109375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 8611], ['ood', 6088], ['ood', 36689], ['ood', 54837], ['ood', 58182]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.511013391772945, 2.7990795015983876, 3.6345406737194885, 4.109013181867809, 4.360950581615823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.8707530498504639})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.456110954284668})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5003106594085693})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0862503051757812})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6239, 'crossentropy': 1.9911564453125}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 14103], ['ood', 48463], ['ood', 31677], ['ood', 6088], ['ood', 1281]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.285936062115391, 2.3176281669471397, 3.0760765733234194, 3.61977386026218, 3.9890016198641502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.9438645839691162})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.7730746269226074})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.8179306983947754})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.1986684799194336})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6251, 'crossentropy': 2.10010625}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 47613], ['ood', 56493], ['ood', 1861], ['ood', 58235], ['ood', 48316]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.431151030256315, 2.600523610487245, 3.3920688162298447, 3.923606483573037, 4.201844094141808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.145784616470337})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.641007900238037})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1320488452911377})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.427245855331421})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6088, 'crossentropy': 2.2428173828125}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 20056], ['ood', 52471], ['ood', 58394], ['ood', 37613], ['ood', 18455]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.387526722296914, 2.4570337813989362, 3.2731868972348392, 3.8226138289731963, 4.151660017583501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.0426411628723145})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6817400455474854})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.753110647201538})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6450304985046387})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.4868462085723877})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.4014172554016113})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.3939080238342285})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.160304546356201})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6291, 'crossentropy': 3.4580703125}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 34012], ['ood', 12064], ['ood', 21668], ['id', 5374], ['ood', 19965]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.623994968230794, 2.8328454886393173, 3.692821114570439, 4.170353520231757, 4.409036957812614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.368048906326294})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.9235076904296875})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0611562728881836})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.351168632507324})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.8530168533325195})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.7831599712371826})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.57661771774292})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6215, 'crossentropy': 3.548765625}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 52308], ['ood', 19911], ['ood', 14163], ['ood', 6935], ['id', 34620]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.5997021987965867, 2.8009334605907785, 3.651767671939468, 4.121096095010341, 4.371047357666731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.0932705402374268})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.8806257247924805})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.059476852416992})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.2934536933898926})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6342, 'crossentropy': 2.130293359375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 14269], ['ood', 13458], ['ood', 2389], ['ood', 31677], ['ood', 19525]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2542169502881144, 2.225598946919813, 3.0026510653828016, 3.554043850378129, 3.934712439723638]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.8085591793060303})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.368725299835205})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3627243041992188})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1179440021514893})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.969686985015869})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.434506416320801})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 2.7557703125}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 11652], ['ood', 4777], ['ood', 11091], ['ood', 40583], ['ood', 44377]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4430465954436504, 2.66113028331083, 3.51893070358469, 4.042617521162213, 4.307333954558857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.0449252128601074})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.983673095703125})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.105449676513672})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.061629056930542})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.4632294178009033})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.8288609981536865})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 4.092690467834473})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.4181268215179443})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.9711179733276367})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6214, 'crossentropy': 3.765452734375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 7649], ['ood', 49347], ['ood', 31683], ['ood', 28445], ['ood', 10918]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5873229210069972, 2.811705159748583, 3.6675381302528676, 4.185114873761286, 4.420289900099249]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.1608939170837402})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.8837804794311523})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.273171901702881})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.713974714279175})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.392162799835205})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.8736870288848877})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.9223976135253906})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.684922933578491})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.6593775749206543})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.745697259902954})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6197, 'crossentropy': 3.897774609375}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 50719], ['ood', 21793], ['ood', 9699], ['ood', 35118], ['ood', 33775]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4943817734169262, 2.745393257360198, 3.628147669975651, 4.120421162636955, 4.3794375885043415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8639779090881348})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5855889320373535})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.851632595062256})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.077193260192871})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.469181537628174})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.0612568855285645})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.501986503601074})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.6320886611938477})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6277, 'crossentropy': 3.306766796875}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 56508], ['ood', 17050], ['ood', 33520], ['ood', 25278], ['ood', 14175]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4015810206029988, 2.6480731996812548, 3.4990638461856634, 4.013909968857188, 4.310613207478833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.091764450073242})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.7991268634796143})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.8556008338928223})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.369699239730835})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.112971544265747})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.3841376304626465})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.845264434814453})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6087, 'crossentropy': 3.582622265625}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 38853], ['ood', 34599], ['ood', 16239], ['ood', 26258], ['ood', 1245]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4242644297551368, 2.703121687228389, 3.5482591666765, 4.073874610608694, 4.366038322131385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.298140525817871})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.756638765335083})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.030075788497925})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.2193775177001953})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.5312747955322266})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6747007369995117})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.9395062923431396})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.9215950965881348})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6108, 'crossentropy': 3.644374609375}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 9385], ['ood', 20737], ['ood', 26937], ['ood', 59826], ['ood', 8338]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5182104889611527, 2.809208222517986, 3.720507351930621, 4.204744981663156, 4.4289037563949805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.055309772491455})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.4882965087890625})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7696547508239746})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.8714356422424316})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.6098690032958984})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.414527416229248})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6338, 'crossentropy': 2.8751947265625}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 9385], ['ood', 24035], ['ood', 13582], ['ood', 51842], ['ood', 36762]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5202682309692341, 2.785648506107224, 3.659708770364759, 4.157382261795799, 4.387068253425066]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9526584148406982})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8382534980773926})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.525394916534424})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0131540298461914})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.378328561782837})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6468396186828613})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.268251419067383})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 3.2385107421875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 7649], ['ood', 8594], ['ood', 46732], ['ood', 39054], ['ood', 4891]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5067982457944837, 2.808460901204193, 3.680947176725315, 4.159803583707271, 4.3996870525103144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.077681541442871})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.747114658355713})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.474252462387085})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.7646403312683105})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.432299852371216})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6062, 'crossentropy': 2.9026158203125}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 29305], ['ood', 56027], ['ood', 31677], ['ood', 54837], ['ood', 14103]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4684907611582283, 2.621414674914319, 3.4914399859181158, 4.0565173464539015, 4.349874280641524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.921250581741333})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.3517379760742188})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.9633655548095703})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.0643131732940674})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2454588413238525})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.605, 'crossentropy': 2.651112109375}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 5357], ['ood', 30051], ['ood', 57912], ['ood', 37288], ['ood', 58394]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4938658353069423, 2.7363653500269614, 3.528295367728152, 4.0545861250758275, 4.330694868216148]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.1224656105041504})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.4264209270477295})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.971482038497925})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.357631206512451})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.4066152572631836})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.5602495670318604})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.4940848350524902})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6236, 'crossentropy': 3.495419140625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 14164], ['ood', 29132], ['ood', 6061], ['ood', 31683], ['ood', 46593]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5152655972054507, 2.80396763860806, 3.6618922672723677, 4.16489346773545, 4.410900451422016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.1090810298919678})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.0406670570373535})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.909121036529541})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.3103601932525635})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.343909740447998})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.457331418991089})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6113, 'crossentropy': 3.152144140625}
