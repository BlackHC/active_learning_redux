store = {}
store['timestamp']=1622163144
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=39']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=39
store['worker_id']=39
store['num_workers']=40
store['config']={'seed': 1277, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.7426838874816895})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0123472213745117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9634411334991455})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.29940128326416})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.7117843627929688})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.5224509239196777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.3981142044067383})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.6418628692626953})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3573927879333496})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.60630202293396})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.469632148742676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.2727322578430176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.833652973175049})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.7924389839172363})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.7316153049468994})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.50915265083313})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.953247308731079})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 4.005335330963135})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.828885078430176})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 4.250002861022949})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 4.315397262573242})
store['active_learning_steps'][0]['training']['best_epoch']=18
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6204, 'crossentropy': 4.018483203125}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 47432], ['ood', 32776], ['ood', 16314], ['ood', 41501], ['ood', 4347]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6887741849348008, 2.9838862168054403, 3.7953442455357997, 4.236725035541506, 4.4502149988620685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.4357099533081055})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.0745325088500977})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.146031618118286})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.7301385402679443})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.7225072383880615})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.5510168075561523})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6109, 'crossentropy': 3.409533984375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 17774], ['ood', 51317], ['ood', 14655], ['ood', 15943], ['ood', 55282]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5548319637998667, 2.7611759437127823, 3.6121964519237553, 4.1099960983075325, 4.367654343147261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.135559320449829})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.8536927700042725})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.251716136932373})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.023269176483154})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5964, 'crossentropy': 2.326260546875}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 55616], ['ood', 5276], ['id', 26260], ['ood', 20894], ['ood', 31046]], 'labels': [-1, -1, 5, -1, -1], 'scores': [1.3329829576907306, 2.4486057501400462, 3.238971610903821, 3.756508752539043, 4.104598437881453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.5426764488220215})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.753056526184082})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.343001365661621})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.752368688583374})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.5678985118865967})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5923, 'crossentropy': 3.065641796875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 45148], ['ood', 4785], ['ood', 32459], ['ood', 6830], ['ood', 28517]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6911197407044463, 2.788196540380495, 3.5813033490637736, 4.040198809032437, 4.306672720417263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.3479762077331543})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.8682050704956055})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.3519062995910645})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.610513687133789})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.3443737030029297})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.8581409454345703})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7521915435791016})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5985, 'crossentropy': 3.72635546875}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 23999], ['ood', 17728], ['ood', 56837], ['ood', 55739], ['ood', 48437]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.695838194214665, 2.9382294534903464, 3.7785148694572497, 4.2240437586298, 4.425653586143733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.350975513458252})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.880950450897217})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.0616531372070312})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8535971641540527})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7764759063720703})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5982, 'crossentropy': 2.9731015625}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 53307], ['ood', 8584], ['ood', 40198], ['ood', 4799], ['ood', 32335]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.494747936848299, 2.6191411986641016, 3.4310162755172193, 3.956092567906599, 4.258406549430674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.6031312942504883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1691300868988037})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.5613930225372314})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.369370460510254})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.8419904708862305})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.0584259033203125})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 4.267563343048096})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6022, 'crossentropy': 3.65115234375}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 4829], ['ood', 46194], ['ood', 16928], ['ood', 8639], ['ood', 4785]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.7519477250657491, 2.9791102004078827, 3.7812787842909845, 4.208591840028676, 4.423949886284352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.2850701808929443})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9329051971435547})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.295236110687256})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3070931434631348})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.2686238288879395})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.16479765625}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 1646], ['ood', 7953], ['ood', 4785], ['ood', 11499], ['ood', 46594]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4579489278449627, 2.6269796974763917, 3.4519117717688372, 3.97834189378088, 4.2868695630107965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.338763952255249})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.7292826175689697})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.868495464324951})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.2546725273132324})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3922348022460938})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.615098476409912})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.4858198165893555})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6241, 'crossentropy': 3.2228025390625}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 28517], ['ood', 39997], ['ood', 45161], ['ood', 19529], ['id', 10860]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.5393438426095314, 2.7425997756835825, 3.6172131853137177, 4.128732400050357, 4.36464887842863]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.1716480255126953})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.6326980590820312})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.334595203399658})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.122593879699707})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2087483406066895})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.7404189109802246})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 4.2189483642578125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.9379749298095703})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6103, 'crossentropy': 3.775709375}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 5320], ['ood', 48926], ['ood', 18324], ['ood', 40654], ['ood', 6560]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.58881984123105, 2.7461422965383195, 3.5564794730198965, 4.056654526515498, 4.320141771231301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.3115315437316895})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.678131580352783})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9579811096191406})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0740110874176025})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.2388319969177246})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6172, 'crossentropy': 2.78664140625}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 44044], ['ood', 2268], ['ood', 49058], ['ood', 18324], ['ood', 8591]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3503781452978914, 2.415025624675089, 3.2553092167291453, 3.8242375751548225, 4.15053677042965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.3616180419921875})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.706265449523926})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.913590908050537})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.25832462310791})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.28938364982605})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.575761079788208})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6124, 'crossentropy': 3.1789853515625}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 54588], ['ood', 25210], ['ood', 28900], ['id', 29432], ['id', 23510]], 'labels': [-1, -1, -1, 2, 1], 'scores': [1.467797092855408, 2.6177500097203317, 3.3636304455695747, 3.880320507408923, 4.191458607057836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.0156755447387695})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7425389289855957})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.0732064247131348})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0614101886749268})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6399, 'crossentropy': 1.98875234375}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 56094], ['ood', 24706], ['ood', 36446], ['ood', 1504], ['ood', 40390]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3252187283187757, 2.4252453388826787, 3.21972510991384, 3.76516576918935, 4.0920249565079265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.1584253311157227})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.783376693725586})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.35036039352417})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6043765544891357})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6081, 'crossentropy': 2.3271470703125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 22960], ['ood', 32776], ['ood', 17728], ['ood', 41451], ['id', 50403]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.4047603911504618, 2.4865062759463203, 3.2635153911143515, 3.8056513239176635, 4.139013085910152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.084007978439331})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.45365047454834})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.773766279220581})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.744095802307129})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.028167247772217})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.810134172439575})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0180492401123047})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.3466367721557617})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.279256820678711})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.485835075378418})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.346914768218994})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.648, 'crossentropy': 3.432808203125}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 28948], ['ood', 3970], ['ood', 53038], ['ood', 26561], ['ood', 49824]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5494721462590655, 2.778743119904399, 3.640354163798092, 4.16959510171432, 4.416373447463995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.13413405418396})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6658589839935303})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.329779624938965})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.547886848449707})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.063699722290039})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2319607734680176})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.5173099040985107})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.675670623779297})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.901615619659424})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.8042874336242676})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 3.83065}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 18026], ['ood', 46590], ['ood', 3747], ['ood', 7768], ['id', 7327]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.4496457916050962, 2.710941185279853, 3.578597278477055, 4.085082722661499, 4.351014066858205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.9307998418807983})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.9048757553100586})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.3050670623779297})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1828806400299072})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2053380012512207})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.34324312210083})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.7477779388427734})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.8486852645874023})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.7734246253967285})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7859842777252197})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.746934413909912})
store['active_learning_steps'][16]['training']['best_epoch']=8
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6158, 'crossentropy': 3.96588984375}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 15932], ['ood', 54539], ['ood', 18706], ['ood', 31065], ['ood', 53534]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4948257652913655, 2.785167627833827, 3.6277106023354584, 4.105394263159106, 4.353692463806539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.0770459175109863})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6343307495117188})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1177639961242676})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.0230519771575928})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9892501831054688})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.093148946762085})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.4355812072753906})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.588515520095825})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1283605098724365})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.4327001571655273})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6398, 'crossentropy': 3.43563828125}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 45161], ['ood', 17728], ['ood', 54539], ['ood', 4863], ['ood', 6506]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.525126562170437, 2.7661042787693875, 3.6449077397275786, 4.14798988703164, 4.39613874109455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.8335775136947632})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.3131284713745117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6343231201171875})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.849193572998047})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.896378755569458})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6359, 'crossentropy': 2.472230859375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 51512], ['ood', 49109], ['ood', 46030], ['ood', 49304], ['ood', 39008]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4600751733983537, 2.5751022018342358, 3.358843214315404, 3.9257321769974762, 4.249415636333465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.0932445526123047})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.05792236328125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.6926827430725098})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.2934765815734863})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6187, 'crossentropy': 2.249151953125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 32504], ['ood', 46560], ['ood', 16676], ['ood', 27302], ['ood', 35832]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3250821378395186, 2.391643682076133, 3.114489049007478, 3.6209215734870774, 3.9648406074193625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9073420763015747})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.486727237701416})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.5947256088256836})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1213440895080566})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.3574793338775635})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.300811767578125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.388779878616333})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0941433906555176})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.179067850112915})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.471073865890503})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6045451164245605})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6329, 'crossentropy': 3.34155}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 14289], ['ood', 41101], ['ood', 36050], ['ood', 33774], ['ood', 43404]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5137401715959786, 2.654568367072568, 3.5331250643628236, 4.062946781760991, 4.349338914322811]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.007478713989258})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.844083786010742})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8979430198669434})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.3291873931884766})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6265, 'crossentropy': 2.1744931640625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 6666], ['ood', 21419], ['ood', 53164], ['ood', 43404], ['ood', 12972]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3313294944491456, 2.4215030112169993, 3.1735127912173535, 3.7178825284143304, 4.045624890201964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.1294093132019043})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4714107513427734})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1201865673065186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.413835048675537})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6301, 'crossentropy': 2.16129453125}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 27477], ['ood', 14267], ['ood', 12959], ['ood', 6088], ['ood', 10277]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2830234978131407, 2.3886250351188805, 3.1902305714145713, 3.7069148486592773, 4.0386099786346845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.2438998222351074})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.2055721282958984})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.646388053894043})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.9109983444213867})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.5915, 'crossentropy': 2.295526171875}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 13027], ['ood', 1213], ['id', 38806], ['ood', 49409], ['ood', 56866]], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.2197443438583262, 2.207145545176978, 3.0464250270701934, 3.592946038409454, 3.9672227779199387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.254119873046875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.7637810707092285})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.2213220596313477})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2192063331604004})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.313145160675049})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.419691324234009})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6675634384155273})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.802318572998047})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6045, 'crossentropy': 3.57961953125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 10321], ['ood', 12748], ['ood', 49109], ['ood', 34317], ['ood', 53026]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5153422909692145, 2.792140307374293, 3.649394631756797, 4.14902112370578, 4.400834189193316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.0794644355773926})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.780557632446289})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.2683844566345215})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.144523859024048})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.2428247928619385})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2319812774658203})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.2587552070617676})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.6496763229370117})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.6766817569732666})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.7944021224975586})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.401592969894409})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.4943037033081055})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.6854100227355957})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.815721035003662})
store['active_learning_steps'][25]['training']['best_epoch']=11
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.621, 'crossentropy': 3.559359375}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 12972], ['ood', 40262], ['ood', 45056], ['ood', 16766], ['ood', 15919]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5858986692822237, 2.9687839413575086, 3.793848235545102, 4.230944922228618, 4.434971518411578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.129581928253174})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5992493629455566})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.070694923400879})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.991503953933716})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0524349212646484})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1973304748535156})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.3861770629882812})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6228, 'crossentropy': 3.141565625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 27140], ['ood', 33522], ['ood', 17728], ['ood', 4832], ['ood', 28293]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.36961282966903, 2.5504461440118527, 3.423990470775963, 3.964263810794865, 4.263739967930689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.0067248344421387})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5347325801849365})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.786940813064575})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9534122943878174})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.815659523010254})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.216115951538086})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.166604518890381})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1222381591796875})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6292, 'crossentropy': 3.1964615234375}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 54757], ['ood', 14801], ['ood', 14613], ['ood', 10317], ['id', 26211]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.549513146701874, 2.6966262313325084, 3.578061539299388, 4.104917918518497, 4.355309825284292]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8973114490509033})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4608001708984375})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.669178009033203})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8337581157684326})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8941893577575684})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.0779967308044434})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6273, 'crossentropy': 2.8526943359375}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 33106], ['ood', 7690], ['ood', 57907], ['ood', 24602], ['ood', 56936]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.607562118475143, 2.8016351690715813, 3.687418871140655, 4.188372251593243, 4.438403034478742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.0897650718688965})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.6496498584747314})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1578259468078613})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.7863218784332275})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6097, 'crossentropy': 2.0885201171875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 27219], ['ood', 38461], ['ood', 1241], ['ood', 24620], ['ood', 11947]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2406030482069794, 2.2434864986694243, 3.0146606025758143, 3.522452911207157, 3.8760981453868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8097360134124756})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.533015251159668})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0069189071655273})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.674241065979004})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.0991530418395996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.411940574645996})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.677480936050415})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.4396822452545166})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6111, 'crossentropy': 3.2938625}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 10789], ['ood', 37326], ['ood', 40262], ['ood', 58231], ['ood', 29289]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5673592766902198, 2.840753223446058, 3.7040587447048434, 4.224152357701557, 4.4324329450824695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.285644054412842})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.5966010093688965})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.1378791332244873})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.2450006008148193})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.8924407958984375})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6027, 'crossentropy': 2.910642578125}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 45048], ['ood', 23027], ['ood', 19686], ['ood', 7576], ['ood', 27826]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3260512919978142, 2.4867854713021282, 3.3988343352908164, 3.939644635224637, 4.252651323259274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.1804914474487305})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.65043306350708})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.2850189208984375})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.409086227416992})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.563065528869629})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6193, 'crossentropy': 2.858081640625}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 19786], ['ood', 1221], ['id', 7456], ['ood', 19945], ['id', 9771]], 'labels': [-1, -1, 3, -1, 8], 'scores': [1.35016410230679, 2.5741396136633683, 3.3187753596210126, 3.853334279861171, 4.167888784373059]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.9790823459625244})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.382793426513672})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6087870597839355})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.9476242065429688})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0482678413391113})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.166177272796631})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.232941150665283})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.014221668243408})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6206, 'crossentropy': 3.190548828125}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 39118], ['ood', 42041], ['ood', 28257], ['ood', 25180], ['ood', 56289]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.483632671542896, 2.6940153310169883, 3.5870801084321915, 4.117881824106677, 4.374113952140014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.303711414337158})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.626939296722412})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7707715034484863})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.336714267730713})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.4900636672973633})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 2.779103515625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 42934], ['ood', 29385], ['ood', 13880], ['ood', 36929], ['ood', 2548]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3853250211330455, 2.486207162372045, 3.345101489389907, 3.858676855952176, 4.183251868226013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0402705669403076})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.685283899307251})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9987540245056152})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.2628231048583984})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1458208560943604})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.311431646347046})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.6242623329162598})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.374943733215332})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.594869613647461})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6093, 'crossentropy': 3.614323046875}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 39118], ['ood', 3970], ['ood', 5868], ['ood', 14960], ['ood', 7050]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5803027263984024, 2.838502787592657, 3.7350163698406167, 4.18572081515421, 4.427331713905534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.8947285413742065})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.832855701446533})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.7961597442626953})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.2832183837890625})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.1181821823120117})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0325474739074707})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.3315658569335938})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.5294482707977295})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.583561897277832})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6152, 'crossentropy': 3.1864708984375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 46716], ['ood', 48337], ['ood', 10369], ['ood', 49418], ['ood', 18489]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4777994493607403, 2.735233679908327, 3.622472936487, 4.123546357870893, 4.370841075888013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.4525814056396484})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.08388614654541})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9912776947021484})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.4941041469573975})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.1970529556274414})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.102115631103516})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.502396583557129})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.889003276824951})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6048, 'crossentropy': 3.504387109375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 6650], ['ood', 18324], ['ood', 36173], ['ood', 20493], ['ood', 38365]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4481806265441945, 2.5519382965688138, 3.4072554340235435, 3.9824393101809434, 4.28477156558734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.258744239807129})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.917707681655884})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.415250301361084})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.6155457496643066})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.7546944618225098})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.3819732666015625})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.5891, 'crossentropy': 3.5800453125}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 39321], ['ood', 24620], ['ood', 16676], ['ood', 14272], ['ood', 32144]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4608601834501038, 2.605524034164978, 3.4498922216879997, 3.9972355075440467, 4.317557601203797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.1093785762786865})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.8165605068206787})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.855590343475342})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.6277496814727783})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.9554738998413086})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.520141363143921})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.864377498626709})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 4.311623573303223})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.9212162494659424})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.5977, 'crossentropy': 3.60166953125}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 56746], ['ood', 21138], ['ood', 46716], ['ood', 59158], ['ood', 42309]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4494858936102801, 2.6263817701859753, 3.4857623872409977, 4.026592016151911, 4.326752808643266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.3226943016052246})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.750143051147461})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.0498385429382324})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.242295265197754})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.493422269821167})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.214965343475342})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.2826807498931885})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.599561929702759})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.2682955265045166})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.851893424987793})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6092, 'crossentropy': 3.322128125}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 46623], ['ood', 51248], ['ood', 22675], ['ood', 56479], ['ood', 28274]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4576857467105098, 2.7124175716891457, 3.5713582253239746, 4.128842724651269, 4.4091015045746484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.1549806594848633})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.522726058959961})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.2070541381835938})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.3440611362457275})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.286242961883545})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.607, 'crossentropy': 2.7893634765625}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 23199], ['ood', 38760], ['ood', 18124], ['ood', 14237], ['ood', 53026]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2940702727673574, 2.440333092102574, 3.248797490199107, 3.816894347548465, 4.151595558979592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.051851511001587})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2603187561035156})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0839219093322754})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.8810877799987793})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.2487728595733643})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6152, 'crossentropy': 2.43873046875}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 22722], ['ood', 4727], ['ood', 4717], ['ood', 17728], ['ood', 25460]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.404677215866236, 2.583825099304357, 3.418683049546546, 3.971278517536744, 4.291755194837377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.9697790145874023})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.741994619369507})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.700157403945923})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.1076271533966064})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3907692432403564})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6146, 'crossentropy': 2.8707447265625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 14969], ['ood', 23080], ['ood', 35411], ['ood', 48485], ['ood', 1494]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2611629524149022, 2.4473885929071653, 3.365918948190277, 3.887784172596934, 4.233197697238349]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.1792707443237305})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.867323637008667})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.9656176567077637})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2796478271484375})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.265263557434082})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.742805004119873})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.969622850418091})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.7279045581817627})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.8232622146606445})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6163, 'crossentropy': 3.757955078125}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 23474], ['ood', 30992], ['ood', 3424], ['ood', 4372], ['ood', 40119]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4689594839080953, 2.708683292071623, 3.5898070970387153, 4.12753290007214, 4.382366291069666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.1114649772644043})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.6141605377197266})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.2165069580078125})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.14426326751709})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.664473056793213})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6052, 'crossentropy': 2.73526875}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 27369], ['ood', 32504], ['ood', 12748], ['ood', 42309], ['ood', 22497]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2845752538387352, 2.3957088160847024, 3.261358649957197, 3.8310753837292157, 4.162383169684998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.8568047285079956})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5582127571105957})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9109487533569336})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2499022483825684})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.511364221572876})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.6025688648223877})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.605602741241455})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.278608798980713})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9698047637939453})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6058, 'crossentropy': 3.71321015625}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 22531], ['ood', 14306], ['ood', 24978], ['ood', 23086], ['ood', 6427]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.513676277937667, 2.838409903944856, 3.716652946633035, 4.23024219753194, 4.439406527089073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.8405954837799072})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.82574462890625})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3143863677978516})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.5455710887908936})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.5853, 'crossentropy': 2.10398203125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 49418], ['ood', 32951], ['ood', 6487], ['ood', 17728], ['ood', 42934]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0941843298435392, 2.0498346930809044, 2.778339433879161, 3.3457777145519003, 3.7541004826014994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.162112236022949})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.959062337875366})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.5523695945739746})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.971733570098877})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.47568941116333})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.7068865299224854})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.8665785789489746})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.5843, 'crossentropy': 3.201421484375}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 17295], ['ood', 31020], ['ood', 48712], ['ood', 12091], ['ood', 32022]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4502376710776463, 2.6630576729525517, 3.5821990754222917, 4.080612370142786, 4.343002557120189]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.7998459339141846})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.4822001457214355})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6970109939575195})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.030315399169922})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.3529253005981445})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6155, 'crossentropy': 2.5758529296875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 57327], ['ood', 1682], ['ood', 17728], ['ood', 48176], ['ood', 31794]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4454927706517533, 2.7573612219827526, 3.5763067762037037, 4.047547980924122, 4.323034800478423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.16536283493042})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.744333505630493})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.026136636734009})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.251803398132324})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.5926, 'crossentropy': 2.1467419921875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 14260], ['ood', 55290], ['ood', 53239], ['ood', 16309], ['ood', 42934]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2679496753308572, 2.2307421735503246, 3.003794509458805, 3.5779995418303514, 3.936628800759408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.1702375411987305})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.9314651489257812})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.334171772003174})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.23363995552063})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.53739595413208})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.8613805770874023})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.7464756965637207})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.8343286514282227})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.067150115966797})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.273833751678467})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 4.323048114776611})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.586, 'crossentropy': 4.123998046875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 42623], ['ood', 28572], ['ood', 40425], ['ood', 23916], ['ood', 7768]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5138083295508558, 2.8095634829034104, 3.694319317576107, 4.198228579205353, 4.424302588899381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.0921874046325684})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.9524459838867188})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.9650912284851074})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.647050380706787})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.003522872924805})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 4.274477481842041})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.5978, 'crossentropy': 3.200428125}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 9337], ['ood', 43404], ['ood', 58299], ['ood', 3848], ['ood', 18483]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4498597356296519, 2.5890091705498075, 3.4662412663933875, 4.016965915391028, 4.309323774682149]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.9487426280975342})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.8883767127990723})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.796675205230713})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.227086067199707})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.517331600189209})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.4246983528137207})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.3717310428619385})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.5967, 'crossentropy': 3.332217578125}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 12972], ['ood', 45494], ['ood', 4891], ['ood', 39346], ['ood', 15036]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4592917123271159, 2.669950656793428, 3.486200963487743, 4.038195390081249, 4.33605399203724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.1399340629577637})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.91204833984375})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.835221290588379})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.46722412109375})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.3864378929138184})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.5245518684387207})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 4.239126205444336})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.5973, 'crossentropy': 3.700180859375}
