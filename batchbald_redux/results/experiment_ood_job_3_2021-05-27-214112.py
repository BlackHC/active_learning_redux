store = {}
store['timestamp']=1622148072
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=3']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=3
store['worker_id']=3
store['num_workers']=40
store['config']={'seed': 1237, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.2208540439605713})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.690932512283325})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9579710960388184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.031991720199585})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.7753758430480957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.5379538536071777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1273884773254395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.190985918045044})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.650599241256714})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.607813835144043})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6101, 'crossentropy': 3.36756640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3046681880950928})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.277597427368164})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2589572668075562})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2568724155426025})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2919607162475586})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 53872], ['ood', 30295], ['ood', 32776], ['id', 26975], ['id', 9931]], 'labels': [-1, -1, -1, 2, 8], 'scores': [1.2092000532446185, 2.143379353079135, 2.749982719563958, 3.040223444701887, 3.170273456781832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.27339506149292})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0514168739318848})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.602396011352539})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.704700231552124})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.5691585540771484})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.612, 'crossentropy': 3.20939296875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3267314434051514})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2946593761444092})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3429527282714844})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3845226764678955})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 42085], ['ood', 18776], ['ood', 9458], ['ood', 49367], ['id', 35998]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1226131769865193, 1.997108447012962, 2.5714776964601302, 2.9063389446408143, 3.00053709632878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.8786556720733643})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.845423698425293})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.818272590637207})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.000826358795166})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1175365447998047})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.046030044555664})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.4133968353271484})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6327, 'crossentropy': 3.220895703125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2258294820785522})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2324886322021484})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.170803189277649})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.212857723236084})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.197134017944336})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2808303833007812})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 57807], ['ood', 13760], ['ood', 58558], ['id', 32539], ['id', 43097]], 'labels': [-1, -1, -1, 2, 6], 'scores': [1.1405806071058897, 1.9881036995413246, 2.585362417118602, 2.9194201617877855, 3.0663475839371923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5899081230163574})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4403951168060303})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.855236530303955})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0640628337860107})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1614277362823486})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.4120874404907227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.3785388469696045})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.320167064666748})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0852675437927246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.5936238765716553})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.925403118133545})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.449155569076538})
store['active_learning_steps'][3]['training']['best_epoch']=9
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6419, 'crossentropy': 3.4158015625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2498326301574707})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2142269611358643})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2080838680267334})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2279934883117676})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.281896948814392})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2651996612548828})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1987113952636719})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2756634950637817})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2843317985534668})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2639268636703491})
store['active_learning_steps'][3]['eval_training']['best_epoch']=7
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 36097], ['ood', 20025], ['ood', 19792], ['id', 19153], ['ood', 39510]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.236872141935489, 2.084452260372508, 2.7078510458714136, 3.052239815102106, 3.2190515747240838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.7285921573638916})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.652676820755005})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.123173475265503})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.137381076812744})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.183002471923828})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.1352319717407227})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.2018165588378906})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.102393627166748})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.6481986045837402})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6224, 'crossentropy': 3.48689921875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2263511419296265})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.315485954284668})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2932415008544922})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2973365783691406})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3462984561920166})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2376021146774292})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3937876224517822})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2641336917877197})
store['active_learning_steps'][4]['eval_training']['best_epoch']=5
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 3452], ['ood', 5992], ['ood', 16796], ['ood', 42312], ['id', 50892]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.1730349870949874, 2.035753143282882, 2.6055508689103783, 2.9048980602372927, 3.046026115364061]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.7059996128082275})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.3996758460998535})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.482330322265625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.807861328125})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6814401149749756})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0231714248657227})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 2.8313220703125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1497502326965332})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1635148525238037})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1156184673309326})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.093798041343689})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1434992551803589})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 19531], ['ood', 4138], ['id', 40163], ['id', 23836], ['ood', 42730]], 'labels': [-1, -1, 0, 5, -1], 'scores': [1.1576706690439427, 2.027349343068983, 2.60025710509902, 2.8946933332574742, 3.0166077606026427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.8794198036193848})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.4405674934387207})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.841609001159668})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.3055601119995117})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.426605463027954})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6141, 'crossentropy': 2.5857453125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2458471059799194})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1704192161560059})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2321605682373047})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1846520900726318})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 2146], ['ood', 42361], ['ood', 27781], ['id', 49373], ['id', 5912]], 'labels': [-1, -1, -1, 7, 3], 'scores': [1.0488066625605108, 1.9252092101488145, 2.5101033866460494, 2.810658607547734, 2.9820464110635125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.824570655822754})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.511995315551758})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0183963775634766})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.8186068534851074})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.9089341163635254})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.667311191558838})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 4.036755084991455})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6211, 'crossentropy': 3.30807109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2306609153747559})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.301350474357605})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3087453842163086})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2980742454528809})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2504465579986572})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2273904085159302})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 14262], ['ood', 48453], ['ood', 33426], ['ood', 47573], ['id', 30623]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1885747210988464, 2.0968669020128448, 2.674068277593787, 2.946171712512114, 3.0431016713013657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.8505325317382812})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7043514251708984})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.262986660003662})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.0514793395996094})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.5150303840637207})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 4.023777961730957})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 4.438230514526367})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6343, 'crossentropy': 3.29111015625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2930793762207031})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2476627826690674})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4169657230377197})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2121864557266235})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2857547998428345})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2171987295150757})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 30465], ['ood', 4730], ['ood', 15382], ['ood', 1385], ['id', 27427]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.2301881567367503, 2.1714291440783784, 2.8242467028283147, 3.2119190544082574, 3.345959431405635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.6775020360946655})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.381783962249756})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.1566104888916016})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0364980697631836})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.4834132194519043})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.622, 'crossentropy': 2.4699109375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1514017581939697})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.1790586709976196})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1448535919189453})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1428592205047607})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 27108], ['ood', 33426], ['ood', 59669], ['ood', 32467], ['ood', 19694]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0392472592389272, 1.8607644475318006, 2.437732394470093, 2.7940220596647674, 2.984746412319682]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.6762441396713257})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.3753013610839844})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.9826087951660156})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.133803367614746})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.5511486530303955})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.348647117614746})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.7089271545410156})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6142, 'crossentropy': 3.266201171875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.3092291355133057})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2585976123809814})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3819537162780762})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2991145849227905})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.431609869003296})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2500405311584473})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 22357], ['ood', 44952], ['ood', 14035], ['id', 43583], ['id', 5377]], 'labels': [-1, -1, -1, 0, 5], 'scores': [1.124633178671914, 2.0098112322318364, 2.637586156076271, 2.955000932997301, 3.095711856516826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6517503261566162})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.3137764930725098})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3615965843200684})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0763587951660156})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.7646665573120117})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.8130083084106445})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6112, 'crossentropy': 2.817161328125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.109194040298462})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1932746171951294})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2281808853149414})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2434463500976562})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 16239], ['ood', 33312], ['ood', 9624], ['ood', 42756], ['id', 10796]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1102090971508183, 2.0138960310467846, 2.559209607588616, 2.8305536441871695, 2.9307291039159864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.6851837635040283})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.346038818359375})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.4411306381225586})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3774611949920654})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.8220272064208984})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.9537265300750732})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6383, 'crossentropy': 2.5117556640625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.0998735427856445})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.103649616241455})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0820924043655396})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0710846185684204})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.066970705986023})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 15497], ['ood', 20572], ['id', 45947], ['ood', 46928], ['id', 47740]], 'labels': [-1, -1, 2, -1, 4], 'scores': [1.1309580661739511, 2.0152328571248366, 2.5939653922097925, 2.9306502026609094, 3.0599303792495522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5390900373458862})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.4431381225585938})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.86051082611084})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6838064193725586})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.865410804748535})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.890547752380371})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6226, 'crossentropy': 2.6971955078125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1810860633850098})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.206346035003662})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1602884531021118})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2363035678863525})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.243260145187378})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 48700], ['ood', 47575], ['ood', 51570], ['ood', 37924], ['id', 4386]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.1336534581235111, 2.0679872910932855, 2.6993676797080575, 2.996041737094396, 3.121885759060918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.7983800172805786})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.3547158241271973})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.57118821144104})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7639286518096924})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3925390243530273})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6109, 'crossentropy': 2.4906435546875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1992826461791992})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2170586585998535})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2231800556182861})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.247822642326355})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 25311], ['ood', 50082], ['ood', 29126], ['ood', 29472], ['id', 8168]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0294423059288904, 1.801150322038298, 2.37607718573598, 2.7145329456679663, 2.872612453308469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.6801695823669434})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4315919876098633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.690094470977783})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.23745059967041})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9854650497436523})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3509573936462402})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6009, 'crossentropy': 2.86322421875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.2584939002990723})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.288111925125122})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2650665044784546})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2685487270355225})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3134398460388184})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 14716], ['ood', 25425], ['ood', 51570], ['ood', 50368], ['ood', 15966]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1442041538932046, 2.006064733617027, 2.605895502408477, 2.921851614258057, 3.0706426206955975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.511879563331604})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.3641357421875})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4200172424316406})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.2075705528259277})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.100924253463745})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2267611026763916})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.664665699005127})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4362053871154785})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6051, 'crossentropy': 3.2107853515625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.285746455192566})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.233044147491455})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.1727378368377686})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.3230581283569336})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2641329765319824})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 28856], ['ood', 47154], ['ood', 52578], ['id', 43821], ['id', 25440]], 'labels': [-1, -1, -1, 0, 0], 'scores': [1.1751317220710484, 2.085945693661756, 2.675920988373792, 2.9915344025592026, 3.109777414858593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5088882446289062})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.0223121643066406})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.5533082485198975})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7194740772247314})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.021592378616333})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.152599811553955})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.165201187133789})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1723227500915527})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6105, 'crossentropy': 3.11534453125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1523559093475342})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2145678997039795})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3092418909072876})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2294847965240479})
store['active_learning_steps'][17]['eval_training']['best_epoch']=1
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 19793], ['ood', 17112], ['id', 50517], ['ood', 55382], ['id', 28069]], 'labels': [-1, -1, 5, -1, 1], 'scores': [1.2173385376578738, 2.1785937628181156, 2.7897467871336934, 3.149040575704616, 3.274074827754152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.462873935699463})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.1517322063446045})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4109625816345215})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.691934585571289})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.749220848083496})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6242, 'crossentropy': 2.214634375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1455280780792236})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1584043502807617})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1252161264419556})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1001594066619873})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 22199], ['ood', 15518], ['ood', 22041], ['id', 26012], ['ood', 8204]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.2514154093650665, 2.1124031278030917, 2.7139659516579586, 3.059360263620488, 3.208107540819916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4521708488464355})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3005130290985107})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.5332071781158447})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6200785636901855})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9454915523529053})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6266, 'crossentropy': 2.386844921875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1906421184539795})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2333412170410156})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1791987419128418})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.180487871170044})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 33102], ['ood', 52372], ['ood', 21015], ['ood', 29891], ['ood', 49378]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1599780778873894, 2.0347506472419727, 2.591365429385447, 2.9200909947100815, 3.0876288596872143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.5139501094818115})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.468308448791504})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9380364418029785})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0586633682250977})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.150744915008545})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.4701104164123535})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.518913745880127})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.327239513397217})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.6250498294830322})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.2772889137268066})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6235, 'crossentropy': 3.638538671875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.242171049118042})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2021446228027344})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.280996322631836})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3023418188095093})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2347080707550049})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3003780841827393})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.274338960647583})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.237869381904602})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 8338], ['ood', 17002], ['ood', 42775], ['id', 36976], ['ood', 20596]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.2954916929130817, 2.2952144445904605, 2.845492864723332, 3.103564638654113, 3.192251568714397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4505908489227295})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.064925193786621})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.202627658843994})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.638777256011963})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.952007293701172})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5836572647094727})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6321, 'crossentropy': 2.359969140625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1329408884048462})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.086719036102295})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.0624536275863647})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.065671682357788})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1153857707977295})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 52878], ['ood', 38508], ['ood', 43368], ['ood', 7202], ['ood', 25520]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.165919814817021, 2.1479002088831542, 2.7702610244710844, 3.1562249535224707, 3.316999909755852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3371484279632568})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.101956844329834})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.2242684364318848})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.598867654800415})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.8418614864349365})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9591236114501953})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.2226858139038086})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.3455066680908203})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.119715690612793})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6346, 'crossentropy': 3.1453451171875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3039296865463257})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3834877014160156})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3771610260009766})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2996306419372559})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3068747520446777})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.350299596786499})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2335457801818848})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2652857303619385})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 58475], ['ood', 13538], ['ood', 25374], ['id', 13195], ['ood', 5394]], 'labels': [-1, -1, -1, 4, -1], 'scores': [1.1868484353712674, 2.049347215842069, 2.6860490248717968, 3.010858640538131, 3.2007776201659714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4770114421844482})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1734914779663086})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.2815496921539307})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.807406425476074})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.696622371673584})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.912820339202881})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2637877464294434})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.4145219326019287})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.3464136123657227})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.2216014862060547})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.1377859115600586})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6326, 'crossentropy': 3.3457140625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1617043018341064})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.201324224472046})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.228957176208496})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1962941884994507})
store['active_learning_steps'][23]['eval_training']['best_epoch']=1
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 27393], ['ood', 31929], ['ood', 24045], ['id', 52556], ['ood', 15905]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.4266656202139822, 2.4100345137489056, 3.0270613913218116, 3.311482633679886, 3.397321333001094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.511325716972351})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.117825508117676})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.5661139488220215})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.4824891090393066})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6893420219421387})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0259385108947754})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.193129777908325})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6306, 'crossentropy': 2.7293671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2109500169754028})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2082524299621582})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1677967309951782})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1834132671356201})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1682982444763184})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.171833872795105})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 16896], ['ood', 36337], ['ood', 28112], ['ood', 19825], ['ood', 29891]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.232185124688424, 2.180027850818029, 2.7465588412477615, 3.010815351705613, 3.1452346841014105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4578187465667725})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0570931434631348})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.455589532852173})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.618828535079956})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.1025280952453613})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.756639003753662})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.4160661697387695})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9854836463928223})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.186594009399414})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.995310068130493})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6209, 'crossentropy': 3.519124609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1872198581695557})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2764708995819092})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2425841093063354})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.237805724143982})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.276533842086792})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2347655296325684})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2722738981246948})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 27866], ['ood', 30214], ['ood', 44074], ['ood', 38624], ['id', 1301]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.2552592181559077, 2.236149688011393, 2.906149707860681, 3.2337174712304924, 3.386171474911679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5339834690093994})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.399040699005127})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.2653756141662598})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8950014114379883})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7265961170196533})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.110210657119751})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.012732982635498})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.441652774810791})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.28326678276062})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.3951120376586914})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6386, 'crossentropy': 3.0553859375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1467933654785156})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1459511518478394})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1155993938446045})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2148997783660889})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2160167694091797})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1813302040100098})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1872189044952393})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 5600], ['ood', 23564], ['ood', 2350], ['ood', 16909], ['ood', 48293]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2974056691833409, 2.316964045299092, 2.8883286842930973, 3.1479051876322472, 3.2789124483790957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4531464576721191})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.0716936588287354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5922369956970215})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.230502128601074})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 1.57041142578125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1401817798614502})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1137721538543701})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.0699973106384277})
store['active_learning_steps'][27]['eval_training']['best_epoch']=1
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 7408], ['ood', 58732], ['ood', 14730], ['ood', 26700], ['ood', 22625]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.935745693953091, 1.6667116916345406, 2.1574482832815756, 2.469169984387971, 2.6575921079654243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6390845775604248})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.3316919803619385})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6866350173950195})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.211517095565796})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.8226118087768555})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.5165328979492188})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.2529163360595703})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.201934337615967})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.582094669342041})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.4461777210235596})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.654573917388916})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6284, 'crossentropy': 3.64237734375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1902050971984863})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.272904872894287})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3251674175262451})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2976899147033691})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3924012184143066})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4638272523880005})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3677291870117188})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 48117], ['ood', 12656], ['ood', 52306], ['id', 10545], ['ood', 16957]], 'labels': [-1, -1, -1, 3, -1], 'scores': [1.1633543309898036, 2.1314158263595124, 2.754798054221421, 3.0478730583820033, 3.1608857391354173]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5781086683273315})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.2709808349609375})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.775848865509033})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.758993148803711})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.905407428741455})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.046937942504883})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9245924949645996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.671431064605713})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.601989507675171})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.6540274620056152})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.7400569915771484})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.6491565704345703})
store['active_learning_steps'][29]['training']['best_epoch']=9
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6211, 'crossentropy': 3.820302734375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1991926431655884})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3081318140029907})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.290614128112793})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3581839799880981})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.382448434829712})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3795273303985596})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.327369213104248})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.369369626045227})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.3068044185638428})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2971937656402588})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.272340178489685})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 14331], ['ood', 46668], ['ood', 46864], ['ood', 31930], ['ood', 49955]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2317859971052625, 2.2623798562257496, 2.864232484193134, 3.161864953847206, 3.3028286987521485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4854446649551392})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.947021722793579})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.6076507568359375})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.6296582221984863})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.913217544555664})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.2158894538879395})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.3325915336608887})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.477644681930542})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6175, 'crossentropy': 3.1779767578125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1894385814666748})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2251291275024414})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2638533115386963})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2455570697784424})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1876055002212524})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3027918338775635})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.354469895362854})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 5804], ['ood', 29201], ['ood', 18927], ['id', 51410], ['id', 38898]], 'labels': [-1, -1, -1, 5, 6], 'scores': [1.174690129890695, 2.109644151792985, 2.66031796529363, 2.9368542169103335, 3.0447147257708753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.4550375938415527})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.0358588695526123})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.4721004962921143})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8486835956573486})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.773648738861084})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1859703063964844})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2666192054748535})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.368197202682495})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.82961368560791})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.754542827606201})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.565239429473877})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.63, 'crossentropy': 3.408256640625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2248549461364746})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.261466145515442})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1460614204406738})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2811108827590942})
store['active_learning_steps'][31]['eval_training']['best_epoch']=1
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 18271], ['ood', 49802], ['ood', 3106], ['ood', 47342], ['ood', 27076]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2988764945995366, 2.337242258744003, 2.928518704424473, 3.2414810054751335, 3.3683256052213952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3364604711532593})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.1196448802948})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3331847190856934})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.280848503112793})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6313, 'crossentropy': 1.39344150390625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1859478950500488})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1091883182525635})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.0936882495880127})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 40149], ['ood', 50698], ['ood', 15939], ['ood', 57910], ['ood', 49157]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8150888288035469, 1.48540571504914, 1.9761073592291094, 2.312995332513289, 2.548922254291261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4939827919006348})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8922693729400635})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.516505241394043})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.629491090774536})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1475303173065186})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6648526191711426})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6266, 'crossentropy': 2.5107505859375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1097893714904785})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1396903991699219})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.113311767578125})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.0973844528198242})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0899536609649658})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 39266], ['ood', 26766], ['ood', 47610], ['ood', 55069], ['id', 34155]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.2589651525123993, 2.1545840963312695, 2.732578604247067, 3.024454742867107, 3.175366571275849]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4118332862854004})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9140785932540894})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.20269775390625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4007434844970703})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.881634473800659})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5291197299957275})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6377, 'crossentropy': 2.2651193359375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1466526985168457})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1269619464874268})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0845935344696045})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1430503129959106})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1302151679992676})
store['active_learning_steps'][34]['eval_training']['best_epoch']=2
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 49418], ['ood', 37709], ['ood', 875], ['ood', 8284], ['ood', 15905]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.064830030669879, 1.8906629463143694, 2.469918805977408, 2.737638701781595, 2.855235831577515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5795464515686035})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.1484758853912354})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4215145111083984})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.6589455604553223})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.637699604034424})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.159613609313965})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.4311158657073975})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.258754253387451})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6317, 'crossentropy': 3.0521693359375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1315680742263794})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0885181427001953})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1410548686981201})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2369470596313477})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2029316425323486})
store['active_learning_steps'][35]['eval_training']['best_epoch']=2
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 30648], ['ood', 53017], ['ood', 42984], ['ood', 39742], ['ood', 5394]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.23457387339487, 2.2688089594520524, 2.8005981464369514, 3.074740605228233, 3.218253538682651]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.5271170139312744})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.3057518005371094})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.682203769683838})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.7016961574554443})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.5655674934387207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.936527729034424})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6173, 'crossentropy': 2.719569140625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2136468887329102})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.2136240005493164})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2253777980804443})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1960325241088867})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.173729658126831})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 13890], ['ood', 1974], ['ood', 10657], ['ood', 53236], ['ood', 14741]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.208933042272941, 2.1191409298704222, 2.7487567978818905, 3.104611290988526, 3.2777742602325395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.44260573387146})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.064246416091919})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6197500228881836})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.720247745513916})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.088874340057373})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.208569049835205})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6198, 'crossentropy': 2.7614828125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.1929426193237305})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1621123552322388})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.141739845275879})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2495718002319336})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2248456478118896})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 28957], ['ood', 33364], ['ood', 15057], ['id', 10808], ['ood', 55530]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.2584291198674042, 2.136029521862748, 2.758852640090835, 3.059935329377039, 3.2030129620838013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.405711054801941})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.9023762941360474})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.303633213043213})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.972942352294922})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.884227752685547})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.9241104125976562})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6337, 'crossentropy': 2.3763109375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.1672868728637695})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.0907087326049805})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.123274326324463})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.0825023651123047})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1561341285705566})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 38152], ['ood', 14100], ['ood', 57777], ['ood', 13586], ['ood', 40107]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9660457568874949, 1.7763367743200758, 2.407674320893496, 2.7734396865398363, 2.9514618086337654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.3268060684204102})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.8154785633087158})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.445427417755127})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4868950843811035})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.906310558319092})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6187, 'crossentropy': 2.0550333984375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.167797327041626})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.1210393905639648})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.0933926105499268})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.0745856761932373})
store['active_learning_steps'][39]['eval_training']['best_epoch']=3
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 46581], ['ood', 33222], ['ood', 21613], ['ood', 25209], ['ood', 35638]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0771318928484876, 1.9121995129522253, 2.5223494109179923, 2.882919396292996, 3.0388177133256544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3807196617126465})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.8356454372406006})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9370977878570557})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6861064434051514})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8934683799743652})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.623, 'crossentropy': 2.088784765625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.1663084030151367})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1273497343063354})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.0871374607086182})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0616562366485596})
store['active_learning_steps'][40]['eval_training']['best_epoch']=4
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 49164], ['ood', 22743], ['ood', 30106], ['ood', 37451], ['id', 40971]], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.979393754407178, 1.8025149698286476, 2.3922275921642377, 2.7276598173519773, 2.9119749014985956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3869843482971191})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8861455917358398})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1972901821136475})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.5264015197753906})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7449023723602295})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.801887035369873})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6821718215942383})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.890585422515869})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0031752586364746})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.901216506958008})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.636, 'crossentropy': 2.98908359375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1293693780899048})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1658761501312256})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.168610692024231})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2035109996795654})
store['active_learning_steps'][41]['eval_training']['best_epoch']=1
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 21929], ['ood', 9005], ['id', 47337], ['ood', 29891], ['id', 14016]], 'labels': [-1, -1, 4, -1, 4], 'scores': [0.9676885382015903, 1.841958121400837, 2.4072076771628446, 2.8052439365805295, 2.9540254360569964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4554487466812134})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8530857563018799})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1756837368011475})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.4943013191223145})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6177473068237305})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.6159145832061768})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.6616413593292236})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.964721918106079})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.8824052810668945})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.3499791622161865})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.098727226257324})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.840250253677368})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.889756679534912})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.0729634761810303})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.2384448051452637})
store['active_learning_steps'][42]['training']['best_epoch']=12
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6559, 'crossentropy': 2.8967068359375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1010334491729736})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0823466777801514})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.0731092691421509})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1058306694030762})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0809375047683716})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0765886306762695})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.085515022277832})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0809398889541626})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1466248035430908})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1180529594421387})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 1418], ['ood', 31580], ['ood', 24805], ['id', 14332], ['ood', 7402]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.282700073352409, 2.2194074253918403, 2.898067849921535, 3.2207948070048866, 3.35780479428652]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4015181064605713})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.102531671524048})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.560885190963745})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6233506202697754})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.807443618774414})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.680938720703125})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.1912550926208496})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.3078107833862305})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.020479202270508})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.089570999145508})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 3.225201171875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.2300797700881958})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.261993408203125})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.249490737915039})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1878952980041504})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2763481140136719})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.210785984992981})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.214585781097412})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.257869005203247})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.259821891784668})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 5684], ['ood', 36767], ['ood', 20416], ['id', 20785], ['id', 34723]], 'labels': [-1, -1, -1, 4, 4], 'scores': [1.1478735503299284, 2.1347774617687443, 2.68282535583863, 2.961100520132206, 3.0681272869330067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.4141671657562256})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.899173378944397})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.5500526428222656})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.4847190380096436})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.195692539215088})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.664276123046875})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.617, 'crossentropy': 2.8632123046875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2262134552001953})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2839411497116089})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1497232913970947})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2787812948226929})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2383430004119873})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 15406], ['ood', 12281], ['ood', 54950], ['ood', 35344], ['ood', 17811]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1453764620937315, 2.070285556401229, 2.628925690385514, 2.99814714267882, 3.231196900488044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.339942455291748})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9483346939086914})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.031951904296875})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.26016902923584})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.573906898498535})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.161797523498535})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6637, 'crossentropy': 2.195212109375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.081913948059082})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.063300609588623})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0745935440063477})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1060876846313477})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0101687908172607})
store['active_learning_steps'][45]['eval_training']['best_epoch']=5
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 49508], ['ood', 32607], ['ood', 31688], ['ood', 4645], ['id', 55109]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.1096808103570535, 1.9966043157992912, 2.6005550859580193, 2.9041742190707955, 3.028615490747593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2731139659881592})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8195395469665527})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.047945499420166})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.3978614807128906})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.3381218910217285})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.5365805625915527})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.037841796875})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.970986843109131})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.998143434524536})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6775, 'crossentropy': 2.6437814453125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1133441925048828})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0793490409851074})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0651438236236572})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0777614116668701})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0810867547988892})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0991636514663696})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0491406917572021})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0125278234481812})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 29254], ['ood', 17553], ['ood', 49838], ['id', 14529], ['ood', 1880]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.1169658515698455, 2.001524988526679, 2.6629690360893257, 2.987283391361487, 3.132471877666701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2777824401855469})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.861325740814209})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.1189708709716797})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.5210704803466797})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.8256993293762207})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.848696708679199})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.8214752674102783})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.3650031089782715})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.0905921459198})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 3.3223276138305664})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.3171823024749756})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.2372512817382812})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6726, 'crossentropy': 3.357474609375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1198070049285889})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1796841621398926})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1456512212753296})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1948978900909424})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2179360389709473})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1890621185302734})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2137656211853027})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2470322847366333})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2586308717727661})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1489237546920776})
store['active_learning_steps'][47]['eval_training']['best_epoch']=7
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 44033], ['ood', 30255], ['ood', 25037], ['id', 55508], ['id', 16469]], 'labels': [-1, -1, -1, 2, 2], 'scores': [1.1953570943108334, 2.1309815550912727, 2.701839311653284, 3.002245027951828, 3.1301021179463895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3453516960144043})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.613233208656311})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.092804431915283})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2746353149414062})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.663623332977295})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9280028343200684})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.052039623260498})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6678, 'crossentropy': 2.45671796875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1623661518096924})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.131270408630371})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1063389778137207})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0783507823944092})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.110079288482666})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.107012391090393})
store['active_learning_steps'][48]['eval_training']['best_epoch']=5
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 30790], ['ood', 22067], ['ood', 29979], ['ood', 47595], ['id', 23855]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.1213833296061426, 2.0446611807771515, 2.641270780347118, 2.964654219363117, 3.142204180182887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.346631407737732})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.7343525886535645})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.014195680618286})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3456971645355225})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.3769989013671875})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.495227336883545})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.7989091873168945})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9645142555236816})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.1522932052612305})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.077437162399292})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 3.0372707843780518})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 3.1302828788757324})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 3.787909984588623})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.93495512008667})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.5607426166534424})
store['active_learning_steps'][49]['training']['best_epoch']=12
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6678, 'crossentropy': 3.43605}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1046574115753174})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0585296154022217})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0626577138900757})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1152713298797607})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1334853172302246})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1516149044036865})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.183119535446167})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1603045463562012})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1934385299682617})
store['active_learning_steps'][49]['eval_training']['best_epoch']=6
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 1849], ['ood', 20880], ['id', 2067], ['ood', 14756], ['ood', 18271]], 'labels': [-1, -1, 3, -1, -1], 'scores': [1.2908002875015805, 2.3253886203312475, 2.986450966357692, 3.2741450249724604, 3.399940145697186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3909423351287842})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.9510976076126099})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.173011302947998})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.4753780364990234})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.537252187728882})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8798105716705322})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.9418153762817383})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.0537047386169434})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.1880016326904297})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 3.2586135864257812})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6577, 'crossentropy': 3.0345560546875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1748301982879639})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.148939609527588})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1079152822494507})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.155803918838501})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1446352005004883})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1680792570114136})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1411129236221313})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1092705726623535})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1503574848175049})
store['active_learning_steps'][50]['eval_training']['best_epoch']=6
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 25037], ['ood', 58813], ['ood', 46832], ['ood', 37605], ['ood', 28762]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1238433140321513, 2.0766684676430605, 2.77889027979663, 3.1262265660723294, 3.2734994065339365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3306281566619873})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6903350353240967})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.2310500144958496})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.271568775177002})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.6652402877807617})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.45888090133667})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.719203472137451})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.9802188873291016})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.2608726024627686})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6639, 'crossentropy': 2.6870767578125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.1895626783370972})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0231258869171143})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0794994831085205})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1058835983276367})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.126903772354126})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.057279109954834})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.13092041015625})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1998555660247803})
store['active_learning_steps'][51]['eval_training']['best_epoch']=7
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 32553], ['ood', 31699], ['ood', 51810], ['id', 31119], ['ood', 26023]], 'labels': [-1, -1, -1, 3, -1], 'scores': [1.0178994162680184, 1.8452095235938666, 2.456420778585211, 2.802303568455253, 2.9621566776057584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3447444438934326})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6188690662384033})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.0040831565856934})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.4398181438446045})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.4628472328186035})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.5862131118774414})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.865328311920166})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.8974087238311768})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6836, 'crossentropy': 2.53140390625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0995205640792847})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0399377346038818})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0649418830871582})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1561434268951416})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1345674991607666})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1466343402862549})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1268103122711182})
store['active_learning_steps'][52]['eval_training']['best_epoch']=7
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 16449], ['ood', 13354], ['ood', 30088], ['ood', 39665], ['id', 4174]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.1172490904804906, 1.9934024205547907, 2.6312133550153636, 2.9806270511709876, 3.160261171245348]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.219826579093933})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6547898054122925})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7333965301513672})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.080254554748535})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.3152880668640137})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.4022610187530518})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.5268383026123047})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.562343120574951})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.7622952461242676})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.69580078125})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.767758369445801})
store['active_learning_steps'][53]['training']['best_epoch']=8
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6987, 'crossentropy': 2.5764296875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0266366004943848})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0848135948181152})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0239825248718262})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0527722835540771})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.072861909866333})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1005817651748657})
store['active_learning_steps'][53]['eval_training']['best_epoch']=3
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 54122], ['id', 26529], ['ood', 31756], ['ood', 4110], ['ood', 43842]], 'labels': [-1, 6, -1, -1, -1], 'scores': [1.2318664438274807, 2.123517642131992, 2.7556587599119844, 3.0979309394913512, 3.2691944276311764]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.360292673110962})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4617841243743896})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.154341220855713})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.1390342712402344})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.533139705657959})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6903, 'crossentropy': 1.6369927734375}
