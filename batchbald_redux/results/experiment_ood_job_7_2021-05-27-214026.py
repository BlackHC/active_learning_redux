store = {}
store['timestamp']=1622148026
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=7']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=7
store['worker_id']=7
store['num_workers']=40
store['config']={'seed': 1241, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.6498241424560547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.324516773223877})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.849571704864502})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7473936080932617})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.9901857376098633})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.185880661010742})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.7801642417907715})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.3328752517700195})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.322925090789795})
store['active_learning_steps'][0]['training']['best_epoch']=6
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5978, 'crossentropy': 4.230361328125}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 18571], ['ood', 4785], ['ood', 17728], ['ood', 15483], ['ood', 36807]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5917378851044912, 2.9196095113776277, 3.787966978615226, 4.245323292868655, 4.46513536240614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 2.766754150390625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.153791904449463})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.1031973361968994})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.129458427429199})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.039654016494751})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.5399866104125977})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.8107175827026367})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.113776206970215})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6148, 'crossentropy': 3.312872265625}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 21797], ['ood', 6088], ['ood', 4905], ['ood', 33171], ['ood', 18324]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4918451571833697, 2.6785059316278113, 3.5753389268915576, 4.103602485049975, 4.388963084991094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.4678478240966797})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.946103096008301})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.1949758529663086})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.470154285430908})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.530111789703369})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.6883058547973633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.9402124881744385})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0624682903289795})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6104, 'crossentropy': 3.624805859375}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 52589], ['ood', 45800], ['ood', 55749], ['ood', 32632], ['ood', 14291]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5429097163762615, 2.756299376483547, 3.588838326840671, 4.077234565576877, 4.3628383979234675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.044661045074463})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.792057991027832})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.088867664337158})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.3862109184265137})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.406219482421875})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.3218979835510254})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6048, 'crossentropy': 3.305668359375}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 33952], ['ood', 59669], ['ood', 18038], ['ood', 54196], ['ood', 5446]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4631714096925277, 2.577454495239013, 3.4656154311082634, 3.9791911433803335, 4.279167935542162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.2221527099609375})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.0095672607421875})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0908775329589844})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.351423978805542})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.4209961891174316})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.402684211730957})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.5235068798065186})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2984800338745117})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6035, 'crossentropy': 3.750501171875}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 38692], ['ood', 28975], ['ood', 59389], ['ood', 14721], ['ood', 33717]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5659890918959718, 2.8371595824946834, 3.748394571682689, 4.241871944521394, 4.439017472684262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.4587883949279785})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.7994394302368164})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2951536178588867})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2355589866638184})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5023481845855713})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.6395320892333984})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.5409977436065674})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6051, 'crossentropy': 3.362557421875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 42714], ['ood', 17271], ['ood', 42648], ['ood', 3791], ['ood', 53068]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5467035477263182, 2.831988028651434, 3.6886585493579656, 4.1541944543283345, 4.394368388926425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.1965856552124023})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9462790489196777})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.246703863143921})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.415605068206787})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.116691827774048})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.5959, 'crossentropy': 3.198365625}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 49275], ['ood', 7431], ['ood', 36283], ['ood', 24643], ['ood', 45161]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3672456825776704, 2.501490708478852, 3.3791700051400886, 3.9384378286882473, 4.239223623012923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.3413591384887695})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.954913377761841})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.2743430137634277})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.728943347930908})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6022, 'crossentropy': 2.3983859375}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 4791], ['ood', 20996], ['ood', 48926], ['ood', 18841], ['id', 24172]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.3863585330282195, 2.4707495344577337, 3.223241231597285, 3.7590348777239413, 4.112046681742261]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.4795432090759277})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.206277847290039})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.2752938270568848})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 3.649099588394165})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 4.014258861541748})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.784212112426758})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.5963, 'crossentropy': 3.34562265625}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 27090], ['ood', 25907], ['id', 10860], ['ood', 25840], ['ood', 27791]], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.4758375222528817, 2.615146232314122, 3.4609759174803845, 3.9964950420762007, 4.285927857315556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.57421875, 'crossentropy': 2.600938320159912})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5763163566589355})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.3993000984191895})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.5996432304382324})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.5719597339630127})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.645294189453125})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6021, 'crossentropy': 3.76240390625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 56336], ['ood', 37084], ['ood', 29434], ['ood', 29132], ['ood', 59819]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4979070107434596, 2.7011711962957734, 3.5039003539143136, 4.028344839632248, 4.303652056572102]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.1560781002044678})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5021305084228516})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0961759090423584})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0759057998657227})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1193437576293945})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6152, 'crossentropy': 2.635329296875}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 32538], ['ood', 2268], ['ood', 35930], ['ood', 37755], ['ood', 18598]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3656398597452053, 2.486425258062776, 3.3170420978005932, 3.8614849292684923, 4.200777840496601]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.228635311126709})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.128477096557617})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2457783222198486})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.498105525970459})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.3717761039733887})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.493227958679199})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.6306490898132324})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.102018356323242})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6, 'crossentropy': 3.542258984375}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 23041], ['ood', 49659], ['ood', 46048], ['id', 2434], ['ood', 55293]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.5357093214094077, 2.6665916523571487, 3.5253276915518015, 4.020969588946333, 4.311634846382244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.1169989109039307})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.5367584228515625})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.097291946411133})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3373749256134033})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6051, 'crossentropy': 2.179008203125}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 47584], ['ood', 48420], ['ood', 58188], ['ood', 12207], ['ood', 36311]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2856867287910596, 2.387788109241513, 3.200676775834781, 3.7262990144008867, 4.076390488814241]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8651618957519531})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.553403854370117})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6208815574645996})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.230642795562744})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.535068988800049})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.9670662879943848})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6061, 'crossentropy': 2.8664080078125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 11591], ['ood', 9635], ['ood', 32355], ['ood', 8565], ['ood', 38365]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5125916209422872, 2.7930415901440258, 3.610809405239616, 4.114045129160877, 4.377277529112764]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.5751864910125732})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.4121625423431396})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.9631848335266113})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.197638511657715})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.379375457763672})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.864797592163086})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.521552562713623})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5973, 'crossentropy': 3.5710859375}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 32504], ['ood', 7851], ['ood', 17324], ['ood', 42595], ['id', 39438]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.4420244100192716, 2.640856816171664, 3.4943316973178717, 4.0248223457831624, 4.327336118403875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.0430290699005127})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.72310733795166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.621701717376709})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8907902240753174})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.152982711791992})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0344724655151367})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.131600856781006})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.730800151824951})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3282506465911865})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6322, 'crossentropy': 3.0323369140625}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 4611], ['ood', 12254], ['ood', 44780], ['id', 21864], ['ood', 8617]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.5386368406529067, 2.6979217621965756, 3.5268366549611487, 4.051690972858196, 4.345526562938584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.196021556854248})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.7406554222106934})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8598592281341553})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.190182685852051})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.499427556991577})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.5665149688720703})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6131, 'crossentropy': 3.0992861328125}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 43086], ['ood', 43630], ['ood', 4827], ['ood', 46676], ['ood', 28399]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4021333165879226, 2.6015126467950096, 3.436646418720187, 3.9697830143561914, 4.264406477814502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.1034843921661377})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.818453311920166})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.876438856124878})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6486992835998535})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.5988, 'crossentropy': 2.39963515625}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 9527], ['id', 19185], ['ood', 39461], ['ood', 56335], ['ood', 32511]], 'labels': [-1, 5, -1, -1, -1], 'scores': [1.2102797240399412, 2.152689550434122, 2.8966758416529466, 3.4370800420515906, 3.821204257771168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.064817428588867})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.5353431701660156})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7281436920166016})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.0811760425567627})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8922207355499268})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.248898983001709})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6332, 'crossentropy': 2.946585546875}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 8593], ['ood', 27802], ['ood', 11591], ['ood', 12035], ['ood', 27197]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4500894664878192, 2.6282534645369986, 3.4978335716592586, 4.021922791136873, 4.313202340093053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.9643440246582031})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.64823842048645})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.569960594177246})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.8133420944213867})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.9783201217651367})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.02199387550354})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.9593753814697266})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0882134437561035})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.229320526123047})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.0942459106445312})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6307, 'crossentropy': 3.39233203125}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 5505], ['ood', 14819], ['ood', 24625], ['ood', 35930], ['ood', 50294]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5293982193334192, 2.7752451725812888, 3.59262630868486, 4.117570515119995, 4.3760362823700465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.0388617515563965})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.890394687652588})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.813032627105713})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.885880947113037})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.5997, 'crossentropy': 2.16577265625}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 56083], ['id', 11862], ['ood', 9379], ['ood', 5525], ['id', 36985]], 'labels': [-1, 1, -1, -1, 5], 'scores': [1.086014721334379, 2.062794172458127, 2.78428976808153, 3.354394409498582, 3.7782550186952326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.1251320838928223})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.869257688522339})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0260496139526367})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.764552116394043})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.2731287479400635})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6271, 'crossentropy': 2.831625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 5357], ['ood', 54196], ['ood', 46716], ['ood', 31046], ['ood', 31947]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2274237279016857, 2.2803625857901775, 3.115431344481828, 3.6886134378025766, 4.068024799899297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.064390182495117})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8076515197753906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.886754274368286})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.089311361312866})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.89023494720459})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7725989818573})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6256, 'crossentropy': 3.090494140625}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 20625], ['ood', 33832], ['ood', 30086], ['ood', 9346], ['ood', 48029]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.39523927887176, 2.563351917865247, 3.4301597066058838, 3.9921149484258693, 4.289279513101215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.104125738143921})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.4684648513793945})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.964695930480957})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.2728917598724365})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.9787659645080566})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3533496856689453})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6362, 'crossentropy': 2.988892578125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 43407], ['ood', 14582], ['ood', 18547], ['ood', 53280], ['ood', 10855]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4912862798482487, 2.560377953536925, 3.3518260787976333, 3.863863699293688, 4.187061820336574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.942576289176941})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.46915864944458})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8096494674682617})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.105332851409912})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.839675188064575})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.23110032081604})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.399301290512085})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.1543173789978027})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.2913336753845215})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.480839729309082})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.48504900932312})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.0512471199035645})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.1475696563720703})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.3699045181274414})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.5865132808685303})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.3486385345458984})
store['active_learning_steps'][24]['training']['best_epoch']=13
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6387, 'crossentropy': 3.520630078125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 49438], ['ood', 9379], ['ood', 59368], ['ood', 39117], ['ood', 40406]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5284553042939897, 2.77330391686412, 3.67064891907283, 4.197256034947521, 4.430209370813861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.9708974361419678})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.757676601409912})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.775871753692627})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.932934284210205})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.7422561645507812})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.889432191848755})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6282, 'crossentropy': 2.733626953125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 48017], ['ood', 53990], ['ood', 48926], ['ood', 3872], ['ood', 22547]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4569121142521038, 2.5061815352084076, 3.3471028296227416, 3.887463361912566, 4.220419924339975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.135455846786499})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6967244148254395})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7619376182556152})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9714155197143555})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.388429641723633})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1762683391571045})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.637, 'crossentropy': 2.843391015625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 12784], ['ood', 12742], ['ood', 37613], ['ood', 9531], ['ood', 30818]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4247632023095358, 2.5849388891131633, 3.401217943361809, 3.956254837849885, 4.271579177736713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.9679322242736816})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.9072823524475098})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.868709087371826})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.931258201599121})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.937875270843506})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.2335715293884277})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3059473037719727})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.5508062839508057})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.6021251678466797})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6030049324035645})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.8712687492370605})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.383328676223755})
store['active_learning_steps'][27]['training']['best_epoch']=9
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6439, 'crossentropy': 3.782033984375}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 44934], ['ood', 39271], ['ood', 29764], ['ood', 56553], ['ood', 39663]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4599777996680707, 2.645238925220934, 3.5191839974438377, 4.048440287700023, 4.3303984157514535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9539854526519775})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.339228630065918})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8598856925964355})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.5651755332946777})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.137824058532715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.900686740875244})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6297, 'crossentropy': 2.8900716796875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 14819], ['ood', 17998], ['ood', 20185], ['ood', 59365], ['ood', 25180]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5129798890350332, 2.699044956778369, 3.5397076744889144, 4.0521131800279235, 4.332827708457513]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8170685768127441})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.198164463043213})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6077890396118164})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.086538791656494})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.911264419555664})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0310425758361816})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.375777244567871})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6215, 'crossentropy': 3.0739478515625}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 14819], ['ood', 32339], ['ood', 59389], ['ood', 39663], ['ood', 44993]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4608116262058932, 2.691673172702549, 3.570978817840011, 4.098865484604952, 4.366945503318159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.15138578414917})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3679208755493164})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8367714881896973})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.857848644256592})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.860830783843994})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.639, 'crossentropy': 2.4396984375}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 10028], ['ood', 35753], ['ood', 1125], ['ood', 28332], ['id', 20982]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.453967762528645, 2.6556275956009388, 3.4466969719602085, 3.958700613062475, 4.249384887796776]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.9985815286636353})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.47141170501709})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.7125191688537598})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.9679508209228516})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.018016815185547})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.840452194213867})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.245450496673584})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.5842838287353516})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.6783552169799805})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6382, 'crossentropy': 2.95247265625}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 56083], ['ood', 13428], ['ood', 44993], ['ood', 54831], ['ood', 29309]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4690578725507577, 2.653647200866317, 3.4933676815011196, 4.0250932210834165, 4.304757888283962]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9754518270492554})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4921538829803467})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4707083702087402})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.605344533920288})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.977893829345703})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.27451753616333})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.412789821624756})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.5727338790893555})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6394, 'crossentropy': 3.1699455078125}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 47973], ['ood', 33102], ['ood', 50514], ['ood', 46717], ['ood', 32763]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.537922818544791, 2.7530102375949066, 3.582957581997052, 4.1108554824550785, 4.385357434505989]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9028034210205078})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.625041961669922})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9092581272125244})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.429931163787842})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9920246601104736})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6275, 'crossentropy': 2.5951580078125}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 16794], ['ood', 12742], ['ood', 41953], ['ood', 54196], ['ood', 29126]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3526899059478978, 2.373710111443437, 3.1716277356978084, 3.7233319963927993, 4.074611598609694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.9775409698486328})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.284389019012451})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.734959363937378})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.6827054023742676})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.961841106414795})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.8486268520355225})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.955564022064209})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9825315475463867})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.963552236557007})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.474919319152832})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6375, 'crossentropy': 3.0853783203125}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 42717], ['ood', 32896], ['ood', 16402], ['ood', 39655], ['id', 45336]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.5422395699804392, 2.7201649181450818, 3.554317559016848, 4.075167227206798, 4.356112085998495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.8402658700942993})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.3913493156433105})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.4636528491973877})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.069676399230957})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.73160982131958})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.5811071395874023})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.060779571533203})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6352, 'crossentropy': 3.116599609375}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 48181], ['ood', 51363], ['ood', 54196], ['ood', 17095], ['ood', 16426]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5267351769356163, 2.6487414499584894, 3.483051215554375, 4.039266185635826, 4.308944804997356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.9180996417999268})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.499217987060547})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.898259162902832})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.209982395172119})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.057274103164673})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 2.5480796875}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 28932], ['id', 19566], ['ood', 53956], ['ood', 18501], ['ood', 17079]], 'labels': [-1, 5, -1, -1, -1], 'scores': [1.2343664975379403, 2.2576329457053452, 3.0733194272046553, 3.6445213657210234, 4.01986939766977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.9906959533691406})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.4543583393096924})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8468093872070312})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.3184475898742676})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.3016278743743896})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.4091200828552246})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6295, 'crossentropy': 2.888805078125}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 23117], ['ood', 4725], ['ood', 10785], ['ood', 32499], ['ood', 59459]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4369787252792963, 2.603961314973744, 3.452539898213292, 3.982139162709265, 4.266305745332147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.0821173191070557})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5705714225769043})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.810720920562744})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.4315900802612305})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.297656297683716})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6142, 'crossentropy': 2.7072361328125}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 50538], ['ood', 48463], ['ood', 22653], ['ood', 4799], ['ood', 3383]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4202521796852734, 2.4850937242406514, 3.2593111247163264, 3.816188506581012, 4.1494463494930365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.919618844985962})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.6815643310546875})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.780032157897949})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.816734790802002})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.7440690994262695})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.746276378631592})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.4655771255493164})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6451, 'crossentropy': 2.987430859375}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 28395], ['ood', 36515], ['ood', 22773], ['ood', 28342], ['ood', 48181]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3959362824501111, 2.531933783094911, 3.4118093212920195, 3.9334252975195856, 4.245248549379918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.9900355339050293})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.436368465423584})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.010066509246826})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.597270965576172})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.19569730758667})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6277, 'crossentropy': 2.4944603515625}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 47945], ['ood', 15895], ['ood', 53000], ['ood', 5854], ['ood', 13522]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3503638590050255, 2.483821672671307, 3.3033994751189812, 3.8483288524472306, 4.17345487137068]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.9854530096054077})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.457676887512207})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.993180274963379})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.759821891784668})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0469653606414795})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.48544979095459})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.4464681148529053})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.2691562175750732})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.2549948692321777})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.314148426055908})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.489267349243164})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6285, 'crossentropy': 3.329290234375}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 36662], ['ood', 16911], ['ood', 46716], ['ood', 50441], ['ood', 47636]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5084642851662289, 2.724108749076244, 3.5981086879348485, 4.11909231130226, 4.384787825003234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.045778751373291})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7859973907470703})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.89005184173584})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9889352321624756})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.931070327758789})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.475689172744751})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.224407911300659})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.082105875015259})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.7981061935424805})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.611851215362549})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.6808762550354004})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6385, 'crossentropy': 3.54692265625}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 27181], ['ood', 12231], ['ood', 22807], ['ood', 12242], ['ood', 12514]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4289685491909099, 2.5886779987153923, 3.4273206263907054, 3.979822584864408, 4.293475373234875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.1485378742218018})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.743286609649658})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.6904053688049316})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.8603081703186035})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3215441703796387})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.447892427444458})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.261324882507324})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6919376850128174})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.395277976989746})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.7166836261749268})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.7069787979125977})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.7060866355895996})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.5844669342041016})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.6354289054870605})
store['active_learning_steps'][43]['training']['best_epoch']=11
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6225, 'crossentropy': 3.845262890625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 9757], ['ood', 56866], ['ood', 49364], ['ood', 10257], ['ood', 21779]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.452852180379081, 2.7322037457804327, 3.6107190964226596, 4.14086883081063, 4.3957658006262985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.2830777168273926})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.722041130065918})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.1272635459899902})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0811891555786133})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.1968815326690674})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.4638519287109375})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.527676582336426})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6255, 'crossentropy': 3.240126953125}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 36767], ['ood', 40119], ['ood', 58182], ['ood', 37740], ['ood', 47303]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5177956739532537, 2.73694995124904, 3.6178473353433667, 4.107370560475381, 4.366923850754409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.9614604711532593})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.589543104171753})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.9001076221466064})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0999512672424316})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.573965072631836})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.621459722518921})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.7812483310699463})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6346, 'crossentropy': 3.2728423828125}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 4717], ['ood', 52332], ['ood', 39663], ['ood', 22531], ['ood', 59459]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5261845494813113, 2.704655280588949, 3.595430172647114, 4.125565501042464, 4.376172599599904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.0991275310516357})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.3528175354003906})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.0974841117858887})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.103059768676758})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0519495010375977})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6223, 'crossentropy': 2.4286884765625}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 14819], ['ood', 24713], ['ood', 10785], ['ood', 52708], ['ood', 37740]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.296826431631512, 2.362848043552206, 3.1863728887592577, 3.7561008945040824, 4.135141426037031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9373183250427246})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.188849687576294})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.7433793544769287})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.837632179260254})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.022575855255127})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.187445640563965})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.093644618988037})
store['active_learning_steps'][47]['training']['best_epoch']=4
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6171, 'crossentropy': 2.9268388671875}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 20671], ['ood', 9589], ['ood', 42598], ['ood', 15518], ['ood', 28]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5218665337901514, 2.7969626312474283, 3.6226009846496243, 4.1128926102134145, 4.35721824118936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9121674299240112})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.240792989730835})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.5036778450012207})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.602959156036377})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6198, 'crossentropy': 1.949223828125}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 46551], ['ood', 29530], ['ood', 31046], ['ood', 36219], ['ood', 3383]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1847359130772777, 2.120262059932707, 2.9035397603830777, 3.4661124971865256, 3.8191442179065707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 2.090803861618042})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.6025497913360596})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6771392822265625})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8981590270996094})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.915910243988037})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3214807510375977})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6306, 'crossentropy': 2.8610376953125}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 42583], ['ood', 32451], ['ood', 59389], ['ood', 52514], ['ood', 42563]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4735874670119897, 2.596060272736355, 3.4821457649763374, 3.982023439363198, 4.266057871552029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.783310890197754})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.679703712463379})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.7384955883026123})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.012077808380127})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.176622152328491})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.1888937950134277})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6347, 'crossentropy': 2.8243154296875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 2105], ['ood', 4759], ['ood', 37233], ['ood', 53000], ['ood', 27413]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3725749695790732, 2.480905225197088, 3.3048740303734085, 3.8657667657720687, 4.200796458902018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.139230728149414})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.3854458332061768})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.0775582790374756})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.1416990756988525})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.26729154586792})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.175394296646118})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.759589433670044})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 4.128276348114014})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 4.284899711608887})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6291, 'crossentropy': 3.328616796875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 2019], ['ood', 13401], ['ood', 59389], ['ood', 1682], ['ood', 10797]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3208074219574728, 2.441791796125619, 3.2996244357061304, 3.8693391882012396, 4.225852945919204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.903242826461792})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.5132346153259277})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.158660888671875})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.241178512573242})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.3998818397521973})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.8339362144470215})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 4.017366409301758})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6224, 'crossentropy': 3.2208681640625}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 47973], ['ood', 16911], ['ood', 29311], ['id', 32583], ['ood', 41981]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.3003908688911876, 2.3812902901736006, 3.249143464505681, 3.805923863653552, 4.1543509105601215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.941860318183899})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.4111452102661133})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.6787099838256836})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.98250150680542})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.3218369483947754})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.6101906299591064})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.5514698028564453})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.6945505142211914})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6269, 'crossentropy': 3.330338671875}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 20671], ['ood', 36427], ['ood', 13079], ['ood', 59447], ['id', 3613]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.4781754902478168, 2.6562117568708334, 3.5245007858030206, 4.018930457289921, 4.296956563749055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.7189795970916748})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1781890392303467})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.1875123977661133})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6052281856536865})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6702067852020264})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6131091117858887})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8430469036102295})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.854567050933838})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.955435037612915})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.992061138153076})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6441, 'crossentropy': 3.1141869140625}
