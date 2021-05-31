store = {}
store['timestamp']=1622150564
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=11']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=11
store['worker_id']=11
store['num_workers']=40
store['config']={'seed': 1246, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.499763011932373})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.0954747200012207})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5772807598114014})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.1594882011413574})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5935, 'crossentropy': 2.6559400390625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.3730900287628174})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.3639782667160034})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3606586456298828})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 26382], ['ood', 45219], ['ood', 14416], ['ood', 7570], ['id', 23416]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.136972422306611, 1.8486426999975012, 2.3638469956126427, 2.701111905081901, 2.903544586890378]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.6182048320770264})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.093264579772949})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.4395933151245117})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 4.466087818145752})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 4.064131736755371})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 4.311629772186279})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.591, 'crossentropy': 3.588005078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.398171067237854})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.4126558303833008})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.4651684761047363})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.4827463626861572})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.4523696899414062})
store['active_learning_steps'][1]['eval_training']['best_epoch']=5
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 14542], ['ood', 27643], ['id', 57208], ['ood', 23712], ['id', 29415]], 'labels': [-1, -1, 0, -1, 7], 'scores': [1.2311412489279854, 2.0092503714586103, 2.554088261985406, 2.886226063062951, 3.08129479039654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.2728278636932373})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.9959468841552734})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4286489486694336})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.5640981197357178})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5962, 'crossentropy': 2.6932138671875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.4079824686050415})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.395188808441162})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3735628128051758})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 30295], ['ood', 5531], ['ood', 16681], ['id', 1183], ['id', 51418]], 'labels': [-1, -1, -1, 8, 2], 'scores': [1.2786542615111134, 2.0355570729864936, 2.572711484506982, 2.8561469118277154, 2.9982390657608624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.070286750793457})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.6251754760742188})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.982306480407715})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.307882785797119})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.146437883377075})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.554295539855957})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.387831687927246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.405673027038574})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6252, 'crossentropy': 3.350756640625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2831993103027344})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2774789333343506})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3271257877349854})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2842568159103394})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2869861125946045})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.4179613590240479})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2597019672393799})
store['active_learning_steps'][3]['eval_training']['best_epoch']=5
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 12682], ['ood', 29472], ['id', 55074], ['ood', 1477], ['id', 16466]], 'labels': [-1, -1, 4, -1, 7], 'scores': [1.2233965044872797, 2.099446236690442, 2.736668016759296, 3.112918951351147, 3.26315782637886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.105868101119995})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.814056873321533})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2957496643066406})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.714357852935791})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.9814631938934326})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.458242416381836})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.9671642780303955})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.9487733840942383})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.537552833557129})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6543102264404297})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.836489200592041})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.9460198879241943})
store['active_learning_steps'][4]['training']['best_epoch']=9
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6268, 'crossentropy': 3.851879296875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2168834209442139})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.326549768447876})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2831692695617676})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3908665180206299})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4211597442626953})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3511073589324951})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 51817], ['id', 7999], ['ood', 40832], ['id', 37722], ['id', 13841]], 'labels': [-1, 3, -1, 5, 9], 'scores': [1.0987553543004915, 2.013921650573807, 2.614321661150586, 2.9466937317144346, 3.0951861321026186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.0379385948181152})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.541351556777954})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.5129518508911133})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.791400671005249})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.1322765350341797})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.390352249145508})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.436373472213745})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8868846893310547})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6389, 'crossentropy': 3.20015390625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1526696681976318})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1664634943008423})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1610416173934937})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2374622821807861})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2156848907470703})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.3246524333953857})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 38760], ['ood', 44143], ['ood', 12416], ['ood', 25374], ['ood', 19792]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1832827880342418, 2.147887998201246, 2.7621513192139755, 3.1211165194280426, 3.2753272683843857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7584086656570435})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1347203254699707})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5342893600463867})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7684166431427})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9550819396972656})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.726102828979492})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.655, 'crossentropy': 2.4041541015625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1338074207305908})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1486642360687256})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1461344957351685})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0942325592041016})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1198008060455322})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 53048], ['id', 26529], ['ood', 9056], ['id', 54545], ['ood', 28533]], 'labels': [-1, 6, -1, 4, -1], 'scores': [1.1708067757242588, 2.0390516338688194, 2.5719604028512713, 2.834671994054723, 2.980853362140813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.9850237369537354})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.696725845336914})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0106706619262695})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.91917085647583})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.961789846420288})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6262, 'crossentropy': 2.830562890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2988076210021973})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2145354747772217})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.2419965267181396})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2563539743423462})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 7368], ['ood', 30199], ['ood', 9896], ['ood', 35350], ['ood', 30214]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1592055194732578, 2.0644358743660036, 2.6706717877084927, 2.997048964799288, 3.119121520691923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9076390266418457})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.285935640335083})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.867509365081787})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.919110059738159})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.754680633544922})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.4104549884796143})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.169018268585205})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6389, 'crossentropy': 3.04906484375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2801601886749268})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2410283088684082})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2937685251235962})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2866266965866089})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.24708890914917})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3568787574768066})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 44940], ['ood', 35753], ['ood', 28391], ['id', 59703], ['id', 42741]], 'labels': [-1, -1, -1, 8, 1], 'scores': [1.0898777432143127, 1.9906964570366275, 2.498501874363958, 2.739418056827792, 2.8723855007711725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6341164112091064})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.1827645301818848})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5996479988098145})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.4129271507263184})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.798548698425293})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.8587265014648438})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 3.329594850540161})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.9515163898468018})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 3.0561203956604004})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 3.08756685256958})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6621, 'crossentropy': 3.28816015625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.173692226409912})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1899974346160889})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1685526371002197})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2369742393493652})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2123286724090576})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1661300659179688})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1685407161712646})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2285888195037842})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2951480150222778})
store['active_learning_steps'][9]['eval_training']['best_epoch']=6
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 47636], ['ood', 29996], ['ood', 26496], ['ood', 49164], ['id', 45579]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.3523586544024941, 2.3724789453924147, 2.975853750966926, 3.2310179354533313, 3.3202701701984028]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5753896236419678})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9235955476760864})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.252185106277466})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.6370046138763428})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.608027696609497})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 3.011646270751953})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.8911871910095215})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6653, 'crossentropy': 2.636123828125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2082765102386475})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2728283405303955})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.2223713397979736})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1861183643341064})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2652424573898315})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2043966054916382})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 24108], ['ood', 31891], ['ood', 42139], ['id', 44317], ['ood', 23013]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.0308531256438411, 1.880123442507986, 2.448793593008915, 2.74995062337699, 2.889386174387856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.4879183769226074})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9409888982772827})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.267000675201416})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.2374770641326904})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.8452768325805664})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.466658115386963})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6584, 'crossentropy': 2.3333634765625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.136407494544983})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1141177415847778})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.112558364868164})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0374236106872559})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.11358642578125})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 37887], ['ood', 8714], ['ood', 10319], ['id', 51295], ['id', 26389]], 'labels': [-1, -1, -1, 2, 4], 'scores': [1.2726767064745137, 2.2057872493815767, 2.7719893232346555, 3.0466159262753267, 3.1520936691764945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.6813654899597168})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.27661395072937})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.380593776702881})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.664242744445801})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.835587501525879})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.086578845977783})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6524, 'crossentropy': 2.59896953125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1778244972229004})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1579631567001343})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1688871383666992})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1815853118896484})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1832000017166138})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 28375], ['ood', 28181], ['ood', 35350], ['ood', 25317], ['ood', 24222]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0903966406353724, 1.9685250203642122, 2.495013471083813, 2.7704596892091287, 2.894902988218716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.679758071899414})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.303091049194336})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.179008960723877})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.6218018531799316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.668818712234497})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.8983778953552246})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.729400396347046})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.8371877670288086})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6316192150115967})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6545, 'crossentropy': 3.1385939453125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2551798820495605})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2184947729110718})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2627471685409546})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.27358877658844})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2740999460220337})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3355255126953125})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2585673332214355})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.279008150100708})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 50082], ['id', 57206], ['id', 17799], ['ood', 36908], ['id', 57335]], 'labels': [-1, 2, 8, -1, 6], 'scores': [1.0972796444947948, 1.8756211555710238, 2.460440573256906, 2.864609127280387, 3.0698019573564697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.5323344469070435})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.8160529136657715})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.2234036922454834})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.424426555633545})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5211308002471924})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.6297149658203125})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.435964584350586})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 3.061112403869629})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.4688143730163574})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.73091459274292})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6849, 'crossentropy': 2.5867345703125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1169848442077637})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0612083673477173})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1122243404388428})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0576951503753662})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.097527265548706})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.077709674835205})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0819084644317627})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0866222381591797})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0367765426635742})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 25404], ['ood', 15848], ['ood', 22756], ['id', 9566], ['ood', 26133]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.2227347142035487, 2.0863015293867346, 2.6906300859079426, 3.057633191009618, 3.217663547220079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3714168071746826})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8819317817687988})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.16756272315979})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.253263473510742})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.338212251663208})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.4388763904571533})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6758, 'crossentropy': 2.2338568359375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0378434658050537})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0213687419891357})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9758513569831848})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.041912317276001})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0648319721221924})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 36295], ['ood', 12279], ['ood', 2842], ['id', 53234], ['id', 4085]], 'labels': [-1, -1, -1, 2, 0], 'scores': [1.119994696002796, 2.008864545381125, 2.535311988489516, 2.82070905147142, 2.9509929906910735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3696643114089966})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.801650881767273})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0821194648742676})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.3573591709136963})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.5420918464660645})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.610718250274658})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.5920052528381348})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.8787360191345215})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.877791166305542})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.966801166534424})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6746, 'crossentropy': 2.83002109375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0928531885147095})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1119762659072876})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1746635437011719})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1050269603729248})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0989000797271729})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 14907], ['ood', 36474], ['ood', 24887], ['id', 5967], ['ood', 10030]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.182635228500629, 2.1713049855507647, 2.7390332842652176, 3.0685872432993344, 3.230846924063232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.384523868560791})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.8522450923919678})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.204946994781494})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.223567247390747})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.7261343002319336})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.31314754486084})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6685, 'crossentropy': 2.3247013671875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.183109998703003})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1681270599365234})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1200156211853027})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.107828974723816})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.1299593448638916})
store['active_learning_steps'][17]['eval_training']['best_epoch']=2
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 47320], ['ood', 30128], ['ood', 53880], ['ood', 30688], ['ood', 36923]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.15181557365082, 2.008563520898532, 2.5575672614475247, 2.8581972268147684, 2.990281620031677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.410735845565796})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.7742630243301392})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.2010486125946045})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.2804741859436035})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.4036707878112793})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.420262575149536})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.500770092010498})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.41278076171875})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.836699962615967})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.471637725830078})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.8963186740875244})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.8879780769348145})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.8286924362182617})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.98378586769104})
store['active_learning_steps'][18]['training']['best_epoch']=11
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6791, 'crossentropy': 2.991976171875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1746995449066162})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.225340723991394})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1679500341415405})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1269886493682861})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2142244577407837})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2180612087249756})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1913049221038818})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2147552967071533})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2559025287628174})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1413793563842773})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2521398067474365})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1821889877319336})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2593674659729004})
store['active_learning_steps'][18]['eval_training']['best_epoch']=10
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 40593], ['ood', 51538], ['ood', 53946], ['ood', 56557], ['ood', 39902]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2703392775699003, 2.2262160935954056, 2.880186298418723, 3.170704898428914, 3.2870692713065273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.533719539642334})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.7836394309997559})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.2979559898376465})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.277756690979004})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6370387077331543})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.644104242324829})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.9477193355560303})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6712, 'crossentropy': 2.3328447265625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.149711012840271})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.09404718875885})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1450743675231934})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.120935082435608})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.07320237159729})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 38557], ['ood', 8680], ['ood', 28570], ['ood', 49331], ['id', 47427]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1799218097263577, 2.052007772648258, 2.6268153417104605, 2.901577999770243, 3.029164993525286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.511093258857727})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.829796552658081})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.1129634380340576})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7117514610290527})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.346736431121826})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.555224657058716})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6702, 'crossentropy': 2.193959765625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0802514553070068})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1443285942077637})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0693690776824951})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1282461881637573})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0991936922073364})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 50082], ['ood', 32538], ['ood', 17266], ['ood', 14195], ['ood', 51544]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0540912938450024, 1.8723767957330715, 2.4488285873340194, 2.789771988076973, 2.9452634103081206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.371321201324463})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.8207331895828247})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0913147926330566})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4037888050079346})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.574103832244873})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.4425830841064453})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.5631484985351562})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.721001148223877})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.5714964866638184})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.9119174480438232})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6672, 'crossentropy': 2.9815046875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.204512596130371})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1927673816680908})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.227951169013977})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1934566497802734})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2173140048980713})
store['active_learning_steps'][21]['eval_training']['best_epoch']=2
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 9519], ['ood', 50301], ['ood', 55049], ['id', 47470], ['ood', 43512]], 'labels': [-1, -1, -1, 7, -1], 'scores': [1.2339409108486272, 2.194183838166589, 2.750166130588337, 3.009354138090446, 3.0899174171426154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5508296489715576})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7586042881011963})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.014559507369995})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.4610421657562256})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.8171143531799316})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.829342842102051})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6703, 'crossentropy': 2.176600390625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.187132716178894})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0801844596862793})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.031831979751587})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0537464618682861})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1083717346191406})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 55023], ['ood', 13933], ['ood', 45161], ['ood', 32301], ['ood', 18768]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0505513670636752, 1.8896387034486657, 2.3862913472105234, 2.6578135127776203, 2.7968284907271794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4211105108261108})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7660188674926758})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.228889226913452})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3662900924682617})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.423966884613037})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.767240047454834})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.66723895072937})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.510834217071533})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 3.241154193878174})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6697, 'crossentropy': 2.9201435546875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.149993896484375})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1871790885925293})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1620140075683594})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.155612826347351})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.198731541633606})
store['active_learning_steps'][23]['eval_training']['best_epoch']=2
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 32908], ['ood', 4909], ['ood', 47130], ['ood', 9000], ['ood', 41558]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.067906020227685, 1.9115755531431704, 2.5110786162363254, 2.8678367565004077, 3.0484691677842335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.400529384613037})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.837630033493042})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.162217617034912})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0854504108428955})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.524172782897949})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6739, 'crossentropy': 1.8729322265625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.0933189392089844})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0572305917739868})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0831985473632812})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0496127605438232})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 14813], ['ood', 10319], ['ood', 17941], ['ood', 4510], ['id', 49494]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.9399210243102014, 1.7133097630055216, 2.234332503540214, 2.5427786606222478, 2.690396226293368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3762091398239136})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6792676448822021})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.170750617980957})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.1566834449768066})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.4008569717407227})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3309011459350586})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.4609928131103516})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6926, 'crossentropy': 2.2261640625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.111541986465454})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0303151607513428})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.065270185470581})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0643818378448486})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0403550863265991})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.059882640838623})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 36607], ['ood', 9517], ['ood', 43465], ['ood', 51599], ['id', 53897]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1945007685424676, 2.040844677559496, 2.62010205568299, 2.880421113692327, 2.990816541898175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.407088041305542})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6636638641357422})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.176377058029175})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.101060390472412})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.4424538612365723})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.358926296234131})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.564804792404175})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.5031065940856934})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.497466564178467})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.339442253112793})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.550769090652466})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.9294233322143555})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6989, 'crossentropy': 2.64811328125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0403814315795898})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9944610595703125})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9931298494338989})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0157910585403442})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0443215370178223})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0128505229949951})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0300796031951904})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0449540615081787})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0334062576293945})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 15988], ['ood', 2781], ['ood', 26629], ['id', 12960], ['ood', 41276]], 'labels': [-1, -1, -1, 3, -1], 'scores': [1.220755781797382, 2.264311311156808, 2.9001605928049887, 3.190494309245988, 3.3328705537540557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4383485317230225})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.951131820678711})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.9634642601013184})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3500313758850098})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.3893027305603027})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5722403526306152})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3533217906951904})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.715719223022461})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.9146833419799805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 3.058699369430542})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.691, 'crossentropy': 2.6263630859375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.157010793685913})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1104172468185425})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.092710018157959})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1085796356201172})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1030776500701904})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.080357313156128})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1067464351654053})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1648253202438354})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1044228076934814})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 44213], ['ood', 16353], ['id', 39586], ['ood', 49905], ['ood', 2025]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.1382522723677693, 2.06530166467791, 2.629055660582596, 2.904401574416764, 3.0257464113061054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.457593321800232})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6552150249481201})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.064936637878418})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4683737754821777})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.410705804824829})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.363004684448242})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.7276558876037598})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.601987361907959})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6958, 'crossentropy': 2.5488755859375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0683622360229492})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0817389488220215})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0617029666900635})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1143507957458496})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0567617416381836})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1408748626708984})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0820183753967285})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 59647], ['ood', 30295], ['id', 42244], ['ood', 70], ['id', 34876]], 'labels': [-1, -1, 6, -1, 4], 'scores': [1.1845848868665807, 2.05354889607771, 2.6220731842049885, 2.954584475021039, 3.135483727193906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.4070866107940674})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8370749950408936})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.2096521854400635})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1341075897216797})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.399635076522827})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.6299238204956055})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.486609697341919})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.3338699340820312})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.84920597076416})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.8103015422821045})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6919, 'crossentropy': 2.586940625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0527706146240234})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1135050058364868})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0612006187438965})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.054887056350708})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0751702785491943})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0989654064178467})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.041658878326416})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1140024662017822})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0925748348236084})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 27177], ['ood', 2548], ['ood', 55434], ['id', 43310], ['ood', 49494]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.2772171513362003, 2.2087076417365603, 2.7739755313683547, 3.015760409895952, 3.1108615657308176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3772492408752441})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.657137155532837})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.0322463512420654})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.246386766433716})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.3534789085388184})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6957, 'crossentropy': 1.7130841796875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.068403720855713})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0290756225585938})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0291253328323364})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0353868007659912})
store['active_learning_steps'][30]['eval_training']['best_epoch']=2
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 5361], ['id', 7327], ['ood', 38716], ['id', 57269], ['id', 47337]], 'labels': [-1, 5, -1, 3, 4], 'scores': [0.8872926743398641, 1.5194409500630477, 1.9952919749226874, 2.3077059181709147, 2.4951904772818283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.4919873476028442})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6166644096374512})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.031723737716675})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.059123992919922})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.0912325382232666})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.279273509979248})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.1966731548309326})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.3454198837280273})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.496054172515869})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.60992169380188})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7046, 'crossentropy': 2.430155078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1131529808044434})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0249077081680298})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0174492597579956})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1176762580871582})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0234887599945068})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0901470184326172})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.060758352279663})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.088881492614746})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0919196605682373})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 28176], ['ood', 34106], ['ood', 46891], ['ood', 26770], ['ood', 18768]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2063842868842296, 2.106124395326329, 2.67621946813665, 2.952226687189846, 3.048917858925635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3735833168029785})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.6554030179977417})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0450029373168945})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.2484304904937744})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.486845016479492})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6892, 'crossentropy': 1.6685015625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1243231296539307})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0764288902282715})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0317728519439697})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0278217792510986})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 34453], ['ood', 3278], ['ood', 49137], ['ood', 16909], ['ood', 12714]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0376015942020616, 1.818624380013735, 2.3791133556964734, 2.7180924901079777, 2.9380148885307458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3562180995941162})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6663155555725098})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8928954601287842})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0036349296569824})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.256718635559082})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.342273473739624})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.238908290863037})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.5439395904541016})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.528118371963501})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.7218174934387207})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.5797393321990967})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7012, 'crossentropy': 2.42518046875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1303863525390625})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.097701072692871})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0841801166534424})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0662553310394287})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0729515552520752})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1268484592437744})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0781681537628174})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 46805], ['ood', 45181], ['ood', 24541], ['ood', 39546], ['ood', 15907]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.173557422313934, 2.1632984929788477, 2.7663236740226855, 3.062741774633581, 3.176454985015881]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3137274980545044})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.7953426837921143})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.0000624656677246})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.9429328441619873})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.140237808227539})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.375025987625122})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2835898399353027})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.4795846939086914})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7024, 'crossentropy': 2.1819875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.06452476978302})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.043717861175537})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.03959321975708})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0772998332977295})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0337514877319336})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0697379112243652})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0666677951812744})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 41857], ['ood', 22223], ['ood', 38691], ['id', 50403], ['ood', 18380]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.1575201677751907, 2.1281068534834433, 2.673834833690439, 3.058432816548409, 3.2404045678993456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2802685499191284})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5791624784469604})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.003603458404541})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.161007881164551})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.2010183334350586})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.265390634536743})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.277479410171509})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.4188172817230225})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.405078887939453})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.482353448867798})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7026, 'crossentropy': 2.3753482421875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0836894512176514})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.035874366760254})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0209934711456299})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0658282041549683})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0211167335510254})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0842406749725342})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.064941644668579})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 55599], ['ood', 48424], ['ood', 37962], ['ood', 30087], ['id', 9425]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.071716841467351, 1.8790804858338142, 2.416600330758474, 2.7276910680726747, 2.8778492557918263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3647973537445068})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6230450868606567})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.0594801902770996})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.0358636379241943})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.9608676433563232})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.249894142150879})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.343362808227539})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.369086742401123})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3685531616210938})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.532639503479004})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.6347997188568115})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4645254611968994})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.9009616374969482})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 3.096137046813965})
store['active_learning_steps'][36]['training']['best_epoch']=11
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6999, 'crossentropy': 2.719927734375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.151432752609253})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1128673553466797})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1035059690475464})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.075505256652832})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.110203742980957})
store['active_learning_steps'][36]['eval_training']['best_epoch']=2
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 5728], ['ood', 38390], ['ood', 46203], ['id', 23107], ['id', 59433]], 'labels': [-1, -1, -1, 0, 4], 'scores': [1.123644966925338, 1.9660103907278197, 2.499413899309886, 2.7473108562084914, 2.870482360934001]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3850674629211426})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6419239044189453})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9636898040771484})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.431488513946533})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.3799967765808105})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.5547027587890625})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.27571964263916})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.367689609527588})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.701, 'crossentropy': 2.422983984375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1345634460449219})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0860521793365479})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1166894435882568})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.062089443206787})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.082115888595581})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0956401824951172})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1052827835083008})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 46629], ['ood', 2494], ['ood', 16025], ['ood', 41538], ['ood', 49902]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1985914985584634, 2.085395262831047, 2.7267964941408502, 3.057991030632664, 3.1961407237219355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3390123844146729})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.5750024318695068})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.9979076385498047})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0355515480041504})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.24125337600708})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.393486976623535})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.6045098304748535})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.5638813972473145})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6975, 'crossentropy': 2.367776953125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1298227310180664})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1131261587142944})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.134279727935791})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0996495485305786})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1044306755065918})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0712018013000488})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0615102052688599})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 17405], ['ood', 34106], ['ood', 59377], ['ood', 2332], ['ood', 31827]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1150331470761996, 1.969184945386488, 2.550250923938939, 2.868715689021556, 3.0037448951519288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.3460462093353271})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.6302111148834229})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.963667392730713})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.9838240146636963})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.2987871170043945})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.341193675994873})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.472285747528076})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.7009, 'crossentropy': 2.24224765625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0762050151824951})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0692336559295654})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0548251867294312})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0252864360809326})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0962605476379395})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0476057529449463})
store['active_learning_steps'][39]['eval_training']['best_epoch']=4
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 26163], ['ood', 11829], ['ood', 42405], ['ood', 20494], ['ood', 38989]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1118836080857364, 2.0029230957062225, 2.5446215105700123, 2.81878751289112, 2.944032874303673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3336418867111206})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.4894099235534668})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8350180387496948})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.9042315483093262})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.082533121109009})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.7037, 'crossentropy': 1.60878359375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0864986181259155})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0465314388275146})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0089662075042725})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0127315521240234})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 50117], ['ood', 51387], ['ood', 40901], ['ood', 23901], ['ood', 42390]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.00205585085296, 1.7875705097995205, 2.320357484528442, 2.6705572226482657, 2.8703628990328705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3491231203079224})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5639352798461914})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9391639232635498})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.063432216644287})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.3013596534729004})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.362666606903076})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4030189514160156})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.730340003967285})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.7084, 'crossentropy': 2.3119642578125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1053144931793213})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.038895606994629})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0443096160888672})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0254309177398682})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.0132322311401367})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 0.9999446868896484})
store['active_learning_steps'][41]['eval_training']['best_epoch']=3
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 4171], ['ood', 8074], ['ood', 37303], ['ood', 42514], ['ood', 43802]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1679116353652175, 2.0599856798718648, 2.600544312453497, 2.888599954327148, 3.0317289593159025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2970390319824219})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.6718177795410156})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.8730406761169434})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.186020851135254})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.1555428504943848})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6958, 'crossentropy': 1.651269140625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1812562942504883})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.029191255569458})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0336567163467407})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0096138715744019})
store['active_learning_steps'][42]['eval_training']['best_epoch']=2
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 27586], ['ood', 12733], ['ood', 13776], ['id', 32045], ['id', 19138]], 'labels': [-1, -1, -1, 8, 3], 'scores': [0.9531737782385266, 1.639286590441059, 2.167752509919275, 2.5113262041386095, 2.682658185963839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3704144954681396})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.6166715621948242})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.8972206115722656})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.1208481788635254})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.195007801055908})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 2.291447639465332})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.2498254776000977})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2340917587280273})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.690249443054199})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7199, 'crossentropy': 2.2660158203125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.054382562637329})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0305333137512207})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.988915205001831})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9881280660629272})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9917752146720886})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0245840549468994})
store['active_learning_steps'][43]['eval_training']['best_epoch']=3
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 25374], ['ood', 46295], ['id', 47410], ['id', 34909], ['id', 42559]], 'labels': [-1, -1, 6, 3, 7], 'scores': [1.149392100719462, 1.9700127186489031, 2.5743050796956366, 2.896257928211372, 3.022513894314314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3294696807861328})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.6429177522659302})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8723163604736328})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0484631061553955})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.3749029636383057})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.497028350830078})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6985, 'crossentropy': 1.9704505859375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.110475778579712})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0781223773956299})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0795601606369019})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0163654088974})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1026959419250488})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 16755], ['ood', 14074], ['ood', 13491], ['ood', 31389], ['id', 54652]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.917101397384291, 1.645215224889129, 2.2010350728678247, 2.5497039978103953, 2.7485251892595777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3372693061828613})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5596733093261719})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7321453094482422})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.056779384613037})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.018549919128418})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.225116729736328})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.7077, 'crossentropy': 1.783346484375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0175154209136963})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.985133171081543})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9877039194107056})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9974402189254761})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9858969449996948})
store['active_learning_steps'][45]['eval_training']['best_epoch']=2
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 41802], ['ood', 46139], ['ood', 45206], ['ood', 8962], ['ood', 46067]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0735663069324815, 1.8949360807640296, 2.481731819072234, 2.791479429403002, 2.9493603932958514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2770249843597412})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.4096709489822388})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.6368566751480103})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.9755175113677979})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9691985845565796})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.198808193206787})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.7125, 'crossentropy': 1.7770265625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0609562397003174})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.040299415588379})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9581470489501953})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0101425647735596})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9765641689300537})
store['active_learning_steps'][46]['eval_training']['best_epoch']=5
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 1865], ['ood', 43148], ['ood', 37982], ['id', 54728], ['id', 48185]], 'labels': [-1, -1, -1, 0, 7], 'scores': [0.9903198177651378, 1.7342405066183884, 2.210470908736787, 2.4961281823335035, 2.6391574778327467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.306877613067627})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.5066759586334229})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7768068313598633})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.9336886405944824})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.1630430221557617})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.9701404571533203})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.372849941253662})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.308122158050537})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4424304962158203})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.4631099700927734})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3319320678710938})
store['active_learning_steps'][47]['training']['best_epoch']=8
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6924, 'crossentropy': 2.42186875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0973844528198242})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0253431797027588})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0062661170959473})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0290791988372803})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0323419570922852})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0307810306549072})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0534783601760864})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9929912090301514})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0507782697677612})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.041689395904541})
store['active_learning_steps'][47]['eval_training']['best_epoch']=8
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 13175], ['ood', 27556], ['ood', 55976], ['ood', 27429], ['id', 25185]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.132533751435425, 2.0541362441223474, 2.6700155343234027, 2.9719706183520866, 3.07279529576528]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2602992057800293})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5291123390197754})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7895770072937012})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.017481565475464})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9603806734085083})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.0149779319763184})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.2709579467773438})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.2153186798095703})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.7038, 'crossentropy': 2.1741451171875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0951741933822632})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0187554359436035})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.046688199043274})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0368103981018066})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0673503875732422})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.03312349319458})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0658714771270752})
store['active_learning_steps'][48]['eval_training']['best_epoch']=6
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 15660], ['ood', 57431], ['ood', 8412], ['ood', 13994], ['ood', 13424]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.090263745989676, 2.015447390718218, 2.6118590247180196, 2.9160888363658994, 3.0469640378149485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3317475318908691})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5150651931762695})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.7489612102508545})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.9279041290283203})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.162376880645752})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.296262741088867})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.329141139984131})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.7104, 'crossentropy': 1.9581998046875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0523300170898438})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9664162397384644})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.939315140247345})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9570544958114624})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9568120241165161})
store['active_learning_steps'][49]['eval_training']['best_epoch']=2
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 14015], ['ood', 25520], ['ood', 19923], ['ood', 24708], ['ood', 41160]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0995900013672224, 1.966244588688773, 2.563877981511169, 2.898697488181007, 3.034108376822717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3804049491882324})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.452399492263794})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.716935396194458})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.01458477973938})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.852360725402832})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.149369239807129})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.2753138542175293})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.2091047763824463})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.556480884552002})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.384007692337036})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.705960273742676})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.512969732284546})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.4998531341552734})
store['active_learning_steps'][50]['training']['best_epoch']=10
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.709, 'crossentropy': 2.60061328125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1148613691329956})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0570309162139893})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0455400943756104})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0196433067321777})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.0233337879180908})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0315768718719482})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9978773593902588})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0342633724212646})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0901777744293213})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0398571491241455})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0914623737335205})
store['active_learning_steps'][50]['eval_training']['best_epoch']=8
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 48911], ['ood', 26262], ['ood', 26697], ['ood', 39818], ['id', 25007]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.1843115054053102, 2.0409381275869594, 2.6078027233783603, 2.8948146377240818, 3.0114167325917593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2874441146850586})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.4648826122283936})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.744807243347168})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9234075546264648})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.024951696395874})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.16257905960083})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4341912269592285})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.267247200012207})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.7044, 'crossentropy': 2.09790078125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.14021897315979})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0607185363769531})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0438144207000732})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0614906549453735})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0873656272888184})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.075533390045166})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0525977611541748})
store['active_learning_steps'][51]['eval_training']['best_epoch']=7
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 39848], ['ood', 36763], ['ood', 51399], ['ood', 46198], ['id', 39074]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0643395587300293, 1.9600762512366812, 2.556805525581571, 2.8332987599324966, 2.97559362106258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3847920894622803})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.442455768585205})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7889795303344727})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1423449516296387})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.0452804565429688})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.229797840118408})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.2366135120391846})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.193155288696289})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.14237642288208})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.3085763454437256})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.7723307609558105})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.720379114151001})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.4325146675109863})
store['active_learning_steps'][52]['training']['best_epoch']=10
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.7144, 'crossentropy': 2.413169140625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0997257232666016})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0249769687652588})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0067436695098877})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0150141716003418})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9831527471542358})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.0022631883621216})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.989682674407959})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.990951418876648})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.0404738187789917})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0952247381210327})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.0542917251586914})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.050309419631958})
store['active_learning_steps'][52]['eval_training']['best_epoch']=9
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 7440], ['ood', 9873], ['ood', 46451], ['ood', 34832], ['id', 9546]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.1912689841960618, 2.172942061294206, 2.850885996802215, 3.1880384415164897, 3.312854858108304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2959649562835693})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5002942085266113})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.669982671737671})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.851557970046997})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.015903949737549})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.374263048171997})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.3670849800109863})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.7007, 'crossentropy': 1.9389947265625}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0298030376434326})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0183066129684448})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.021376609802246})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9791405200958252})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0059349536895752})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.024492859840393})
store['active_learning_steps'][53]['eval_training']['best_epoch']=4
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 28104], ['ood', 26069], ['ood', 34661], ['ood', 25187], ['ood', 24310]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9996396533292071, 1.8370779340780454, 2.377974480084924, 2.6791273960474413, 2.815582651557551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.308788537979126})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4596436023712158})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7213497161865234})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.8278474807739258})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.850442886352539})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.0103914737701416})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.0970072746276855})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.717, 'crossentropy': 1.8415861328125}
