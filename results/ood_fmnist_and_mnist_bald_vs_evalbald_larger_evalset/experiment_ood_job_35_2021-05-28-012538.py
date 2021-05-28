store = {}
store['timestamp']=1622161538
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=35']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=35
store['worker_id']=35
store['num_workers']=40
store['config']={'seed': 1273, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.432244062423706})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.689999580383301})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.5170540809631348})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.013506889343262})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.8712189197540283})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.9788312911987305})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 4.223658561706543})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 5.060093402862549})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 4.440949440002441})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.288861274719238})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5928, 'crossentropy': 4.22281015625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.4889185428619385})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3756730556488037})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.4403181076049805})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5712106227874756})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.572408676147461})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.5026757717132568})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5235986709594727})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 20752], ['ood', 45161], ['id', 11446], ['id', 54591], ['id', 14425]], 'labels': [-1, -1, 5, 2, 2], 'scores': [1.0472063599104091, 1.8443968098260504, 2.44029072075448, 2.769864535776132, 2.9454324390305873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.3118367195129395})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.002103805541992})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2779104709625244})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.260876178741455})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.595, 'crossentropy': 2.429073828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2317051887512207})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.2710365056991577})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2635760307312012})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 51622], ['ood', 3220], ['id', 13034], ['ood', 34366], ['ood', 7541]], 'labels': [-1, -1, 7, -1, -1], 'scores': [0.9735990543413113, 1.714695238251331, 2.2452284047662383, 2.62344636380507, 2.8275797071190114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.3660459518432617})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.116588592529297})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.243464231491089})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.526677131652832})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.890517234802246})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 4.079356670379639})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.827871799468994})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.09923791885376})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.15589714050293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 4.416295051574707})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5844, 'crossentropy': 4.05393515625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.4422844648361206})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3582863807678223})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4551246166229248})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5170934200286865})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4679040908813477})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 37639], ['ood', 54617], ['ood', 4850], ['id', 48159], ['id', 44411]], 'labels': [-1, -1, -1, 4, 2], 'scores': [1.236702522463176, 2.154192559077637, 2.7050005656443483, 2.9379135897604085, 3.045914965822643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.160592794418335})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.359287738800049})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6580913066864014})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.365227699279785})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.087384223937988})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5846, 'crossentropy': 3.642453515625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.6422491073608398})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.6648393869400024})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.7385777235031128})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.8730201721191406})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 48706], ['ood', 52514], ['ood', 26745], ['ood', 26538], ['ood', 13467]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1374171727749776, 1.9115966053720093, 2.4770717356710623, 2.7467577297099597, 2.8855881199610893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.403052806854248})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.177459716796875})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.490530490875244})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.920510768890381})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 4.085207939147949})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.2187275886535645})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.577, 'crossentropy': 3.567696484375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.5646677017211914})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.542417049407959})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.6292381286621094})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.671079397201538})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.6593232154846191})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 11585], ['ood', 19294], ['ood', 55821], ['ood', 55278], ['id', 57524]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0886273504883488, 1.8779565308223374, 2.434291615448302, 2.763829726284211, 2.9087170049674214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.4778146743774414})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.3925254344940186})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.316628932952881})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.8042006492614746})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.6260788440704346})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 4.039602279663086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 4.374601364135742})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 4.790233612060547})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 4.222163677215576})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 4.712597370147705})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.764339923858643})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 4.825730800628662})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 4.396413803100586})
store['active_learning_steps'][5]['training']['best_epoch']=10
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5872, 'crossentropy': 4.556716015625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.60201096534729})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.739701271057129})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.792634129524231})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.7058911323547363})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 57545], ['ood', 3200], ['ood', 37900], ['ood', 19687], ['id', 37427]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1339410789292352, 1.9511950407202114, 2.5296895858213917, 2.8276876673355478, 2.93838023999192]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.3546223640441895})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.342670202255249})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.4898433685302734})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3619887828826904})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.642913818359375})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7153003215789795})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.3586530685424805})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5909, 'crossentropy': 3.778888671875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.5222067832946777})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.555647611618042})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5670390129089355})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5348780155181885})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5862948894500732})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5645085573196411})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 31530], ['ood', 8466], ['ood', 12676], ['ood', 37613], ['id', 21063]], 'labels': [-1, -1, -1, -1, 9], 'scores': [1.2029895516782654, 2.1021142023567627, 2.7092834393868443, 3.044731202585176, 3.1711427996557555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.2045016288757324})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.356417179107666})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.4735898971557617})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.8474929332733154})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.935730457305908})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5745, 'crossentropy': 3.49475703125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.6437413692474365})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.5448720455169678})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.5645662546157837})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.5761048793792725})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 13446], ['ood', 44444], ['ood', 7383], ['id', 57620], ['id', 3613]], 'labels': [-1, -1, -1, 5, 1], 'scores': [1.2147750848524743, 2.0304228768540726, 2.6212915267994132, 2.954423191158888, 3.1509683529600583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.082811117172241})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.676483631134033})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.454524517059326})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.4222946166992188})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.8306899070739746})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5945, 'crossentropy': 2.893223828125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.5649042129516602})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.42873215675354})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4396616220474243})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.4182716608047485})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 30295], ['ood', 37858], ['ood', 50998], ['ood', 24284], ['id', 51418]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0169822966159816, 1.7788740251638573, 2.314918154794568, 2.6662129037457447, 2.7927687674315935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.29917311668396})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 3.5446994304656982})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.396973133087158})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 4.05652379989624})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 3.999591827392578})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 4.172522068023682})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 4.30495548248291})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 4.163203239440918})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.294691562652588})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.68218994140625})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.566, 'crossentropy': 4.705305078125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.4229168891906738})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 1.5978801250457764})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.6662508249282837})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.6967973709106445})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.91758394241333})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.8403574228286743})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 46379], ['ood', 2236], ['ood', 35857], ['ood', 2861], ['id', 22934]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1318241938750402, 2.053041827332731, 2.681264738918501, 3.104341503559933, 3.2562224346692528]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.9892363548278809})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.7902369499206543})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.369614601135254})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.892031669616699})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.8835554122924805})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5738, 'crossentropy': 3.1369185546875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.5732715129852295})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.6095082759857178})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.5836776494979858})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.509268045425415})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 19252], ['ood', 7437], ['ood', 47999], ['ood', 7479], ['ood', 46548]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1301366177516163, 1.9004275339179686, 2.5036271900942726, 2.833454705008135, 2.9924480137463805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 2.2981343269348145})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.2672553062438965})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 3.558553695678711})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 4.378427982330322})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.852653741836548})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 4.506882667541504})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 4.194095134735107})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5595703125, 'crossentropy': 4.989022254943848})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5576, 'crossentropy': 4.283198046875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.643216848373413})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.7370517253875732})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.6895650625228882})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.8171093463897705})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.862212896347046})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.8334522247314453})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.882163405418396})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 12239], ['ood', 17774], ['ood', 31381], ['id', 1583], ['ood', 23136]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.2771357546947457, 2.193586320905295, 2.7804759578855176, 3.090764728049307, 3.2179580206199496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.0250372886657715})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.674989700317383})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.175198793411255})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.508232831954956})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.776585102081299})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.809600353240967})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.579147265625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.6763156652450562})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4884138107299805})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.5821304321289062})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.757779598236084})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.6987932920455933})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 48622], ['ood', 30878], ['ood', 46048], ['ood', 49743], ['id', 20195]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1626278096431308, 2.04698802601531, 2.5933125207740826, 2.8854004537149747, 3.0000448828332127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.018829107284546})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8872146606445312})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0489630699157715})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.9172191619873047})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.8513593673706055})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.014809608459473})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6086, 'crossentropy': 3.56647421875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.5662970542907715})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.6544839143753052})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5418224334716797})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.6913591623306274})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.6298046112060547})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 30128], ['ood', 17325], ['ood', 7685], ['ood', 35604], ['ood', 4683]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1102295191079192, 1.9538818425929638, 2.5129696527003453, 2.838715100925861, 3.011320132507196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9835889339447021})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.736478328704834})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.8757519721984863})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.380157947540283})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6228, 'crossentropy': 2.0297787109375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3068876266479492})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3381328582763672})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.30186128616333})
store['active_learning_steps'][14]['eval_training']['best_epoch']=2
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 42519], ['ood', 47913], ['ood', 23377], ['ood', 52242], ['ood', 6323]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9549535969718785, 1.6946438560716444, 2.2619929661155966, 2.588571632019608, 2.802042275798505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.1552858352661133})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.835582733154297})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.2410941123962402})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3765640258789062})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6012, 'crossentropy': 2.3225615234375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4936532974243164})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4645180702209473})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3996102809906006})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 20013], ['ood', 18755], ['ood', 36327], ['id', 53634], ['ood', 13682]], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.983218654296524, 1.6224171261636893, 2.1081746884393944, 2.4833927814679955, 2.7122021900783997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.9374161958694458})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.6833748817443848})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.336991786956787})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 3.42537784576416})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6309268474578857})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5913, 'crossentropy': 2.9723947265625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5389366149902344})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.419568657875061})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5047749280929565})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4807813167572021})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 41895], ['ood', 6948], ['ood', 54001], ['ood', 16802], ['ood', 44564]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1869347816417402, 2.061125083585876, 2.6682380205503593, 2.9843348824433207, 3.086196153670267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 2.1810247898101807})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.5366578102111816})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.145496368408203})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.6740431785583496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.6444244384765625})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5957, 'crossentropy': 3.019995703125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.5327033996582031})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.5924146175384521})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.5836002826690674})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4651296138763428})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 25438], ['ood', 37609], ['id', 50389], ['ood', 25644], ['ood', 31831]], 'labels': [-1, -1, 0, -1, -1], 'scores': [1.0998862978492534, 1.9485048508045617, 2.4832589061046617, 2.830815988798353, 3.0012084838361073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.693239450454712})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.8284947872161865})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.061441421508789})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.113452196121216})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6097, 'crossentropy': 1.9089080078125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2736737728118896})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.255183458328247})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1616754531860352})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 4871], ['ood', 22724], ['ood', 7774], ['ood', 11364], ['ood', 51820]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9369128670612101, 1.672186089878278, 2.203747721756886, 2.594255683930994, 2.828742945682823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.127213954925537})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.1934523582458496})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.6002368927001953})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.7189314365386963})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 4.246237754821777})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.8229775428771973})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.929177761077881})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 4.602779865264893})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 4.160888195037842})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6006, 'crossentropy': 3.956650390625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4941439628601074})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4318292140960693})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5705065727233887})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.6604499816894531})
store['active_learning_steps'][19]['eval_training']['best_epoch']=1
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 6287], ['ood', 100], ['ood', 52862], ['ood', 52478], ['id', 1364]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.346054158945147, 2.2349004235363217, 2.787998811081528, 3.045329037501089, 3.1224533169525754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.0457425117492676})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.626192808151245})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.4349923133850098})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4383316040039062})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.681224822998047})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.7693710327148438})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.6484732627868652})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.311296463012695})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 4.00858359375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.646385908126831})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.588834285736084})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5880417823791504})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.6055371761322021})
store['active_learning_steps'][20]['eval_training']['best_epoch']=1
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 25823], ['ood', 48568], ['ood', 15737], ['ood', 23437], ['id', 7867]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1192610236363199, 2.1194949158789727, 2.7648187253054974, 3.0509487891238996, 3.1276421769308635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.093940496444702})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.6746413707733154})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.7401411533355713})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.5281929969787598})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.4233927726745605})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5871987342834473})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6051, 'crossentropy': 3.1472677734375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.317622423171997})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3785555362701416})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2887234687805176})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4312663078308105})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.49750816822052})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 1449], ['ood', 20964], ['ood', 12416], ['ood', 19656], ['ood', 31730]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2135500673286788, 2.195611357264761, 2.7342557412910233, 3.064466637306343, 3.1988102642134315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.092167854309082})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.4711523056030273})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.9149913787841797})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3834969997406006})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.597397804260254})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.8471946716308594})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.729249954223633})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6038, 'crossentropy': 3.477160546875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.377402424812317})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5187954902648926})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4937262535095215})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5271942615509033})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5186561346054077})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 6921], ['ood', 48420], ['ood', 8655], ['ood', 39325], ['id', 53789]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.3582463965098124, 2.2801240106749607, 2.9209459187855877, 3.2156426593189, 3.301785704270473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.8590126037597656})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.8178365230560303})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.1770577430725098})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.518954038619995})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 4.062784671783447})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.7810444831848145})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 4.049221992492676})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.455326080322266})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.210426330566406})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.5893, 'crossentropy': 4.289803125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.508361577987671})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5094693899154663})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.645500659942627})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.9367244243621826})
store['active_learning_steps'][23]['eval_training']['best_epoch']=1
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 30160], ['ood', 50079], ['id', 27685], ['id', 2217], ['ood', 35863]], 'labels': [-1, -1, 8, 3, -1], 'scores': [1.2227382699511322, 2.1132130187572953, 2.6291684575919145, 2.8671639730402143, 2.953000601269535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.9375779628753662})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.324936866760254})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9125757217407227})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1425137519836426})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.377354145050049})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.5478453636169434})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.758885383605957})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.828643798828125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6089513301849365})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6189, 'crossentropy': 3.810651953125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.432526707649231})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4547624588012695})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4440455436706543})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4498212337493896})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6037416458129883})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.5361424684524536})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5959579944610596})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5210257768630981})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 6804], ['ood', 34619], ['id', 47927], ['ood', 16026], ['ood', 13031]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.2302480739063317, 2.2008782384234853, 2.809696845245748, 3.0703672588913413, 3.1623058549802856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5771484375, 'crossentropy': 1.946750521659851})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.6057558059692383})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.053341865539551})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 3.3740694522857666})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.899735927581787})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.5715, 'crossentropy': 2.92725}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.502493977546692})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.432415246963501})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 1.4730850458145142})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.5206680297851562})
store['active_learning_steps'][25]['eval_training']['best_epoch']=2
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 10747], ['ood', 53413], ['ood', 12047], ['id', 6602], ['id', 35508]], 'labels': [-1, -1, -1, 0, 5], 'scores': [1.0458615056906255, 1.861115166207965, 2.451927054589369, 2.849718932453868, 3.0358616364013677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.9046881198883057})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.9046473503112793})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.1614465713500977})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.1614155769348145})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.782759189605713})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.8967361450195312})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5859551429748535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.158230781555176})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 4.63731575012207})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6006, 'crossentropy': 4.228344921875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4479572772979736})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.6240346431732178})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.699073076248169})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7342902421951294})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5384012460708618})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.8579562902450562})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.857248306274414})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 35196], ['ood', 2313], ['ood', 13084], ['ood', 41668], ['ood', 32668]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.144094983400019, 2.149375695761525, 2.7413044546981773, 3.0229394485806402, 3.1436933146387798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.9972654581069946})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 2.38283109664917})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 3.163099765777588})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.5285072326660156})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.3749046325683594})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.8315789699554443})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 4.282627105712891})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.510500907897949})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.687716484069824})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 3.5554089546203613})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.8691513538360596})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6037, 'crossentropy': 3.9101609375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4102277755737305})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5046976804733276})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.467947006225586})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.507737398147583})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.6803048849105835})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.575495719909668})
store['active_learning_steps'][27]['eval_training']['best_epoch']=3
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 5308], ['ood', 21453], ['ood', 22665], ['id', 31179], ['ood', 42909]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.1843573710862532, 2.16977752741613, 2.7164410758504616, 2.9627839238096003, 3.036118024499406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.8115413188934326})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.34182071685791})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.123654365539551})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.240626811981201})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.809314727783203})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.9175405502319336})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.4701056480407715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.739962577819824})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.4888782501220703})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 4.037813663482666})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6277, 'crossentropy': 3.635558203125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4592108726501465})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5396709442138672})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4863815307617188})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.638838529586792})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5249799489974976})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.6969552040100098})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 36817], ['ood', 7210], ['id', 1776], ['ood', 55792], ['ood', 8116]], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.2487059368150797, 2.234584883072002, 2.841296345021342, 3.1822290237528943, 3.35811772075193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.7575050592422485})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.404723882675171})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.7779269218444824})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.509709358215332})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.0743088722229004})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6109, 'crossentropy': 2.522229296875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.4410197734832764})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3715605735778809})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.434098243713379})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.410555362701416})
store['active_learning_steps'][29]['eval_training']['best_epoch']=2
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 2126], ['ood', 17583], ['ood', 44740], ['ood', 18166], ['ood', 8682]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1366217834172088, 2.0481909593883203, 2.639814541219765, 2.9578745614029733, 3.1381095078120556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.8448741436004639})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.2288856506347656})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.5838327407836914})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.803237199783325})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.280451774597168})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.3854875564575195})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.633, 'crossentropy': 2.7161951171875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4468156099319458})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4407589435577393})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4699680805206299})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3724031448364258})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4942047595977783})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 59476], ['ood', 59390], ['ood', 53008], ['ood', 26533], ['ood', 19714]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1859954148378051, 1.982840312697225, 2.539792652952716, 2.864980309127776, 2.9996771597909433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.7686131000518799})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.583984375, 'crossentropy': 2.8802003860473633})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.8247251510620117})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.932377815246582})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.524732828140259})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.495372772216797})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.58211612701416})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.61, 'crossentropy': 3.322177734375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.4789023399353027})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3352103233337402})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.378143548965454})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4263402223587036})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.4655187129974365})
store['active_learning_steps'][31]['eval_training']['best_epoch']=2
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 21233], ['ood', 26741], ['ood', 50408], ['ood', 8116], ['ood', 44400]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3299672747104179, 2.3247012942305485, 2.980942637841837, 3.3179459501171724, 3.4739922594087305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.77553129196167})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3371267318725586})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.512448310852051})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1628477573394775})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.977654457092285})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6293, 'crossentropy': 2.6294650390625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3392713069915771})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.368085503578186})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.34968900680542})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.400958776473999})
store['active_learning_steps'][32]['eval_training']['best_epoch']=2
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 37027], ['ood', 19364], ['ood', 6526], ['id', 50210], ['ood', 54973]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.1596875856790914, 1.997776095495829, 2.6479192463392627, 2.97537408480901, 3.1282632432065656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.765031099319458})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.1793243885040283})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8259541988372803})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.608976125717163})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.0446114540100098})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.4733805656433105})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1314685344696045})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.7071847915649414})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6364, 'crossentropy': 3.2031353515625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4290430545806885})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.365980625152588})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4308854341506958})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3573088645935059})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3125141859054565})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3804216384887695})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5087716579437256})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 41191], ['ood', 14163], ['ood', 38956], ['ood', 13682], ['ood', 16192]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2694042372866212, 2.18778571973336, 2.782476918607114, 3.051021900477311, 3.1643184055636944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6613383293151855})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.300076961517334})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0926337242126465})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.748717784881592})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9892616271972656})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.651, 'crossentropy': 2.50938828125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2819764614105225})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3247087001800537})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2272140979766846})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.247598648071289})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 46811], ['ood', 57932], ['ood', 49644], ['id', 10800], ['ood', 26586]], 'labels': [-1, -1, -1, 3, -1], 'scores': [1.1244093869570135, 1.9399873734166704, 2.454604074656481, 2.743191699565143, 2.926214781298965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.5673208236694336})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.1094789505004883})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.5485827922821045})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.811044454574585})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4289705753326416})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6221, 'crossentropy': 2.2020875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2462797164916992})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.212190866470337})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1696727275848389})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.130150318145752})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 42934], ['ood', 29043], ['ood', 21814], ['ood', 59394], ['ood', 13031]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1274704899673411, 1.956160969895648, 2.540374073269513, 2.78835263031183, 2.903898829673457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.6493568420410156})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.328911781311035})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.0114388465881348})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9125423431396484})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.4345850944519043})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.3857717514038086})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.7383391857147217})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.8723583221435547})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 4.048723220825195})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.410689115524292})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6419, 'crossentropy': 3.997584765625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.6036579608917236})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.6705660820007324})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.7154569625854492})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.6749804019927979})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5867109298706055})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6260809898376465})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.6983962059020996})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7099075317382812})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.9731004238128662})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 1987], ['ood', 39356], ['ood', 5545], ['ood', 43272], ['id', 29501]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.3026030880035335, 2.223546117182563, 2.796406261235667, 3.048393043986917, 3.1360008143327063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.7653542757034302})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.27846097946167})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.653893232345581})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0200648307800293})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.4773106575012207})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.233588218688965})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 3.0127358436584473})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.3213679790496826})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.86881685256958})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.602538585662842})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6421, 'crossentropy': 3.299634765625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.428436040878296})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3492738008499146})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4738446474075317})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3509304523468018})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4283394813537598})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4462180137634277})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4732353687286377})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 11032], ['ood', 12934], ['ood', 34500], ['ood', 22218], ['id', 33735]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.2082923591254255, 2.1828108529149457, 2.8094001712030456, 3.147096918058933, 3.2849685016522416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.7268073558807373})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.9981656074523926})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.303218364715576})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.796173572540283})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8986682891845703})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6529, 'crossentropy': 2.23096171875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4685158729553223})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3431086540222168})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3376352787017822})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3534917831420898})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 46585], ['ood', 59929], ['id', 26038], ['ood', 52898], ['ood', 13031]], 'labels': [-1, -1, 3, -1, -1], 'scores': [1.0063432237806489, 1.7445029771502152, 2.2559767786910276, 2.5696312951135134, 2.7598619368582185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.5417335033416748})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.313469648361206})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.452198028564453})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.459857702255249})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.985264301300049})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0385897159576416})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.204204797744751})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6487, 'crossentropy': 2.6427244140625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2509303092956543})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3355510234832764})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.36557137966156})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3270347118377686})
store['active_learning_steps'][39]['eval_training']['best_epoch']=1
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 58628], ['ood', 15932], ['ood', 24752], ['ood', 31996], ['ood', 8901]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2214509680571664, 2.170935871869145, 2.7400205563629054, 3.025775108720155, 3.1475293358899963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.553602695465088})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1789069175720215})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.666353225708008})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9627413749694824})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.173701763153076})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.381342649459839})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.5714685916900635})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.8638501167297363})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 4.034029960632324})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.2853264808654785})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 4.082404136657715})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6395, 'crossentropy': 3.828064453125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4253900051116943})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.312989592552185})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3560717105865479})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.6588010787963867})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4899029731750488})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5354936122894287})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.6338856220245361})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4915848970413208})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 42934], ['ood', 46522], ['ood', 44740], ['ood', 5394], ['id', 34848]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1155004405145175, 2.0270440954216205, 2.6445370763470883, 2.9681624701982994, 3.1385973291014224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4231958389282227})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.870047688484192})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.240612506866455})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.966294527053833})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.563014030456543})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6478, 'crossentropy': 2.1088732421875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2195816040039062})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.158602237701416})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1444660425186157})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.199471354484558})
store['active_learning_steps'][41]['eval_training']['best_epoch']=2
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 34429], ['ood', 36187], ['ood', 14201], ['ood', 28633], ['id', 27800]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.0139034692374667, 1.8176286840681564, 2.3508153649147188, 2.695452896091945, 2.880664329265369]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.5440607070922852})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.2295713424682617})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.033341407775879})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8320629596710205})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1792526245117188})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1076645851135254})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.3940536975860596})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6418, 'crossentropy': 3.0710943359375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.407127857208252})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3746771812438965})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.41904878616333})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4345414638519287})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3903770446777344})
store['active_learning_steps'][42]['eval_training']['best_epoch']=2
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 15019], ['ood', 21140], ['ood', 15519], ['ood', 28454], ['ood', 36702]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.097191495367346, 1.9415352745226273, 2.5333828012119595, 2.8440839240686433, 2.9989265188991947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4817874431610107})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.362487554550171})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8835678100585938})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.7760443687438965})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.972153663635254})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.374555826187134})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.338688850402832})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.428771734237671})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.5155029296875})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 4.150296211242676})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6429, 'crossentropy': 3.345962890625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4123291969299316})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3894572257995605})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.428745150566101})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4444540739059448})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4612114429473877})
store['active_learning_steps'][43]['eval_training']['best_epoch']=2
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 59472], ['ood', 32968], ['ood', 12075], ['ood', 18779], ['ood', 27874]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1205164035240156, 2.0734838999868814, 2.7479398334524667, 3.082627001642413, 3.2384386749772807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.8008496761322021})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.533604145050049})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.539212703704834})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.808786392211914})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.722830295562744})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.415235996246338})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.338587999343872})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6384, 'crossentropy': 3.150198046875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4240634441375732})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3319549560546875})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.5451656579971313})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.5560240745544434})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.436072587966919})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5273282527923584})
store['active_learning_steps'][44]['eval_training']['best_epoch']=6
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 58380], ['ood', 41408], ['ood', 24338], ['ood', 30044], ['ood', 39983]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.152566735051223, 2.0565891328210926, 2.6270232105063815, 2.9949877402518377, 3.173988731790015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5338821411132812})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.136183738708496})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.403233051300049})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7934157848358154})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.255711317062378})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.3799891471862793})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.6820333003997803})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.108499050140381})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.638, 'crossentropy': 3.1715236328125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3945846557617188})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3320286273956299})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.418265461921692})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3820840120315552})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.4173883199691772})
store['active_learning_steps'][45]['eval_training']['best_epoch']=2
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 39576], ['ood', 42405], ['ood', 11648], ['ood', 54624], ['ood', 59007]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1168327126886302, 2.0576735991716064, 2.6520608584630834, 2.9423081991033975, 3.0674840037802893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4182441234588623})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.0070736408233643})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.618833065032959})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.7560911178588867})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.7451562881469727})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.697416067123413})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.8820414543151855})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.78298020362854})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.4012138843536377})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.211862087249756})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.70326566696167})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 4.409432411193848})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6568, 'crossentropy': 3.612586328125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5169891119003296})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4031920433044434})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3148894309997559})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.3562437295913696})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.4472748041152954})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.487386703491211})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.515159249305725})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4807418584823608})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.4719940423965454})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.5330901145935059})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.5646662712097168})
store['active_learning_steps'][46]['eval_training']['best_epoch']=9
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 5679], ['ood', 16697], ['ood', 704], ['id', 51540], ['ood', 8507]], 'labels': [-1, -1, -1, 9, -1], 'scores': [1.2679283009850415, 2.227510406835193, 2.7736411140062938, 3.031330209449644, 3.1402365528696556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5480782985687256})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.024280309677124})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.5455360412597656})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7638630867004395})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.397780656814575})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.4357895851135254})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.946125030517578})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.7856240272521973})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.6111950874328613})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.688502311706543})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6403, 'crossentropy': 3.315915625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3635960817337036})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3573267459869385})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.443015456199646})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.4524123668670654})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.4792070388793945})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3438775539398193})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.5363833904266357})
store['active_learning_steps'][47]['eval_training']['best_epoch']=4
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 7779], ['ood', 32827], ['ood', 380], ['ood', 15905], ['ood', 26095]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1831293567782306, 2.1718380388140166, 2.808380512785564, 3.1256864617596225, 3.251290768570816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4754078388214111})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.8881608247756958})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.434464931488037})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5478603839874268})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.9025022983551025})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6489, 'crossentropy': 2.0582904296875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2225961685180664})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1082019805908203})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1025092601776123})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1263505220413208})
store['active_learning_steps'][48]['eval_training']['best_epoch']=2
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 17301], ['ood', 30791], ['ood', 34829], ['ood', 9381], ['ood', 31454]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1887872629454106, 2.0404438568653465, 2.6910622013740344, 3.054808002277742, 3.180719450623805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.6014606952667236})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.0933244228363037})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.71785831451416})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.3704605102539062})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.980699062347412})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6427, 'crossentropy': 2.2423505859375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.237727403640747})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2424410581588745})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1800916194915771})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.270117163658142})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 41716], ['ood', 9466], ['ood', 26541], ['ood', 55932], ['ood', 7933]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0562973676776766, 1.8715006735058246, 2.482913703426563, 2.815206500235954, 2.9562299328650052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.6341031789779663})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5643720626831055})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5852885246276855})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1080474853515625})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.0799753665924072})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.5457699298858643})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.4721503257751465})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.9488799571990967})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.969423770904541})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.810293436050415})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.583028793334961})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.806492805480957})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 4.548044204711914})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 4.31459379196167})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 4.4812421798706055})
store['active_learning_steps'][50]['training']['best_epoch']=12
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.657, 'crossentropy': 4.007665625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.50399649143219})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.358628749847412})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3698534965515137})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5241258144378662})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.451408863067627})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.5662983655929565})
store['active_learning_steps'][50]['eval_training']['best_epoch']=3
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 760], ['ood', 33233], ['ood', 57543], ['ood', 22121], ['id', 5323]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.2867374240201888, 2.2535176388770153, 2.812999842792844, 3.1144062757880695, 3.2212399734757113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4730932712554932})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.192533016204834})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7524847984313965})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.4487833976745605})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0212268829345703})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 3.0363926887512207})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.208242654800415})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6467, 'crossentropy': 2.8091630859375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2654118537902832})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2428245544433594})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1865571737289429})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.294820785522461})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2319321632385254})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2263439893722534})
store['active_learning_steps'][51]['eval_training']['best_epoch']=5
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 3064], ['ood', 33720], ['ood', 10400], ['ood', 19975], ['ood', 48562]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1747818313818457, 2.1335944379976275, 2.763725787249713, 3.0762516500858563, 3.2156513704632914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.585455298423767})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.272439956665039})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.4308853149414062})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6636152267456055})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.7294394969940186})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.840540647506714})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.0857458114624023})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.2353272438049316})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6489, 'crossentropy': 2.932632421875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3613113164901733})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3317723274230957})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4003264904022217})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3696997165679932})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3928231000900269})
store['active_learning_steps'][52]['eval_training']['best_epoch']=2
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 47522], ['ood', 12234], ['ood', 4061], ['id', 47987], ['ood', 1404]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.2802045309327936, 2.224119374188434, 2.895131805952359, 3.1522175210190637, 3.254190544986778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.5008509159088135})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9730808734893799})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3790786266326904})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.376281261444092})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.828981876373291})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6564, 'crossentropy': 2.19326953125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2528204917907715})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.0713505744934082})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1267895698547363})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1449925899505615})
store['active_learning_steps'][53]['eval_training']['best_epoch']=2
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 44475], ['ood', 7933], ['ood', 27970], ['ood', 26095], ['ood', 36320]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0441527630382486, 1.8576211121278061, 2.41325486707788, 2.777497731275668, 2.988597797075588]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.4405546188354492})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.025787591934204})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4109930992126465})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.7193610668182373})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.818997859954834})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.027327060699463})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.981232166290283})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.2145586013793945})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.5949244499206543})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.448596477508545})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6538, 'crossentropy': 3.187724609375}
