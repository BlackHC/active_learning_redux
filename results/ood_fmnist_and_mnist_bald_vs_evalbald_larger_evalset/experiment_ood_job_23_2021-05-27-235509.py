store = {}
store['timestamp']=1622156109
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=23']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=23
store['worker_id']=23
store['num_workers']=40
store['config']={'seed': 1259, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.3423099517822266})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.882929563522339})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.396960973739624})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.6569442749023438})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.790982723236084})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6036, 'crossentropy': 3.0988708984375}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 3110], ['ood', 2417], ['ood', 17728], ['ood', 4785], ['ood', 13495]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3940929240985704, 2.474182457564792, 3.32871282923385, 3.894629019824306, 4.245991619150085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.4920945167541504})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.1072466373443604})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.6080684661865234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.3917348384857178})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5898, 'crossentropy': 2.45872578125}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 20572], ['id', 55778], ['ood', 45157], ['ood', 28443], ['ood', 59657]], 'labels': [-1, 8, -1, -1, -1], 'scores': [1.2358875464426329, 2.3397915478111395, 3.1211275727939913, 3.671186896055122, 4.017200947739214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.0804529190063477})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.877800464630127})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0248775482177734})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.4743094444274902})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.453268051147461})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.5750255584716797})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6999380588531494})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.674445152282715})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6107, 'crossentropy': 3.7084515625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 11379], ['ood', 34676], ['ood', 27090], ['id', 47545], ['ood', 28371]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.572437212731876, 2.7766183126215593, 3.651755519726324, 4.144826232877403, 4.4028192543263085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.155747890472412})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.678001642227173})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.978407859802246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.325623035430908})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.702357292175293})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.5625576972961426})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5971, 'crossentropy': 3.372821875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 42365], ['ood', 14360], ['ood', 46550], ['ood', 36312], ['id', 44581]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.5280912428212376, 2.668984653477572, 3.5193425510213405, 4.0533190372347345, 4.335972536112228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.1485838890075684})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.1806640625})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.970524311065674})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.255148410797119})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.525029420852661})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.6492562294006348})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.827353000640869})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.690791130065918})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.8674426078796387})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.990841865539551})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5961, 'crossentropy': 4.20640390625}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 32504], ['ood', 17728], ['ood', 14715], ['ood', 25823], ['ood', 24602]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5780262657218551, 2.8615774088022023, 3.7498261789540264, 4.249571975581201, 4.4603743643903435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.2578413486480713})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 2.995058298110962})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.449873924255371})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.6954314708709717})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.586, 'crossentropy': 2.3709232421875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 38583], ['ood', 18564], ['ood', 47636], ['ood', 27983], ['ood', 59657]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3140359303405436, 2.3305899906741248, 3.143983612767628, 3.7262692244134508, 4.061063507207475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.247544765472412})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.0241944789886475})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.8141632080078125})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2389183044433594})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.7802553176879883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.9081473350524902})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.390835762023926})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6073, 'crossentropy': 3.4308125}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 13588], ['ood', 17728], ['ood', 27419], ['ood', 54638], ['ood', 37315]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5392778243485248, 2.765328204852284, 3.635500973411987, 4.144617158607506, 4.3927410415348564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.3897552490234375})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.729111909866333})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.920440673828125})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.3659610748291016})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.6224448680877686})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.898683547973633})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5816, 'crossentropy': 3.364598828125}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 22960], ['ood', 51438], ['ood', 22547], ['ood', 42579], ['ood', 5013]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5180201535534579, 2.6842543476941145, 3.578479520454435, 4.12028591992044, 4.383440685905252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.2703299522399902})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.0553290843963623})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8277578353881836})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.1421852111816406})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.7702484130859375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.901554822921753})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3516135215759277})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.587, 'crossentropy': 3.64587265625}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 21830], ['ood', 23259], ['ood', 58350], ['ood', 58235], ['ood', 30341]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.628714753818719, 2.791175010610543, 3.610530982107491, 4.104775351024639, 4.3639181786047825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.183621883392334})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6267499923706055})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.730558156967163})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.3964438438415527})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.0639493465423584})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.227552890777588})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6037, 'crossentropy': 2.9380205078125}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 25187], ['ood', 30128], ['ood', 39451], ['ood', 3016], ['ood', 27026]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5729261375884374, 2.79725991595085, 3.6026791031700283, 4.117234551160576, 4.3795117442711184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.183478832244873})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.864521026611328})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8184685707092285})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1990880966186523})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6116, 'crossentropy': 2.2752314453125}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 39529], ['ood', 18846], ['ood', 57306], ['ood', 11129], ['ood', 33169]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4976671378402306, 2.5479033803885427, 3.2957780638989327, 3.8282142910986225, 4.156130465663117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.41221284866333})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.1048660278320312})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.735765218734741})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.9294416904449463})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.9934380054473877})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 4.064896106719971})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5925, 'crossentropy': 3.84714921875}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 14716], ['ood', 31895], ['ood', 5536], ['ood', 16911], ['ood', 18736]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3752163592168127, 2.586220390855443, 3.4147348193664033, 3.9637110793711283, 4.290909096914843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.0284507274627686})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.6972551345825195})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.6584362983703613})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.005802631378174})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.609, 'crossentropy': 2.2825322265625}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 20794], ['ood', 18324], ['ood', 16911], ['ood', 32976], ['ood', 8735]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3864864370592986, 2.5609936962764497, 3.3486189720353217, 3.8706648226963107, 4.1888591251162595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.9629608392715454})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.5957274436950684})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.002645969390869})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7518601417541504})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.4675889015197754})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6019, 'crossentropy': 2.7890369140625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 12758], ['ood', 55124], ['ood', 50559], ['ood', 58495], ['ood', 20404]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4681100641056295, 2.601147692192229, 3.4889814333942795, 4.023422049691793, 4.3048296197353295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.6797163486480713})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.917490005493164})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.31508731842041})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.3327648639678955})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.6474390029907227})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.8653979301452637})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 4.055110931396484})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.5891, 'crossentropy': 3.531263671875}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 14716], ['ood', 41353], ['ood', 33673], ['ood', 38789], ['id', 36843]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.541240966206677, 2.6988671269206437, 3.4999611589648776, 4.0267308122496335, 4.314289082920562]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0854856967926025})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.6245388984680176})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.865901231765747})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.954335927963257})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.1914148330688477})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.5684070587158203})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.779933452606201})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6188, 'crossentropy': 3.2890546875}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 53520], ['ood', 18356], ['ood', 5334], ['ood', 25644], ['ood', 27181]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4732473060803106, 2.7118334335851837, 3.521001169614575, 4.03589381224782, 4.324048978930858]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.0763425827026367})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9278883934020996})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.5133397579193115})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.639425754547119})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.474698066711426})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5825, 'crossentropy': 3.0231345703125}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 15871], ['ood', 23421], ['ood', 54814], ['ood', 27328], ['ood', 54397]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.372692235636856, 2.544936429535122, 3.3935709289840332, 3.981304978281054, 4.278410158832253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 2.2995738983154297})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.110079288482666})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.571622371673584})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2713916301727295})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.033114194869995})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.6637816429138184})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6095, 'crossentropy': 2.899075390625}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 54481], ['ood', 1231], ['ood', 39346], ['ood', 58471], ['ood', 29132]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4626799847630232, 2.597004343724164, 3.431529709429695, 3.988224570555249, 4.28880230850944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9691413640975952})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.5678939819335938})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7266149520874023})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.951289653778076})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.002643585205078})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.249728202819824})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.570343494415283})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.598602294921875})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 3.349776171875}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 42365], ['ood', 31062], ['ood', 31650], ['ood', 11230], ['ood', 6838]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4774920623206103, 2.7160252004404573, 3.5811557086344417, 4.114462300349629, 4.366451114579521]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.112243175506592})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.645402669906616})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.979245662689209})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1545257568359375})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6135, 'crossentropy': 2.172641015625}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 35729], ['ood', 54357], ['ood', 4591], ['ood', 25626], ['ood', 38853]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4317027234783408, 2.530035618547492, 3.298139105265938, 3.8062641266692054, 4.1329970790263335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.3294506072998047})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.267134189605713})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.8426904678344727})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.490241527557373})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.831616163253784})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.021925926208496})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.5925, 'crossentropy': 3.202284765625}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 29132], ['ood', 45058], ['ood', 39302], ['ood', 56742], ['ood', 35344]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3462175687501508, 2.426652991868872, 3.323470822402615, 3.853434070954992, 4.180085308125836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.3887555599212646})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.0520401000976562})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.180053472518921})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 3.326871395111084})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.525740146636963})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.5804362297058105})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.5973, 'crossentropy': 3.48784765625}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 18283], ['ood', 31895], ['ood', 5455], ['ood', 34748], ['ood', 28391]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4994316584541885, 2.6844655992938393, 3.5316535153323434, 4.043582372785263, 4.317939423028194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.9415104389190674})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.642953872680664})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.4437904357910156})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.7029097080230713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.191389322280884})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.468919277191162})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.369320869445801})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.622, 'crossentropy': 2.9573681640625}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 35753], ['ood', 31497], ['ood', 55375], ['ood', 4757], ['id', 31705]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.4391847355162861, 2.611796452586531, 3.5439013542843316, 4.048756691870516, 4.3162327612986715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.3129959106445312})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.909475803375244})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.891319751739502})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.790985345840454})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.8738527297973633})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.029350280761719})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.9861810207366943})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 4.172787666320801})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.594, 'crossentropy': 3.947645703125}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 2390], ['ood', 36295], ['ood', 25953], ['ood', 56519], ['ood', 47801]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4094698280523423, 2.6010240220265506, 3.470888328543178, 3.996868466585557, 4.279973007717988]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.6763558387756348})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.2155466079711914})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6118361949920654})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.5844476222991943})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.897495746612549})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9672279357910156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.8850247859954834})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6437, 'crossentropy': 2.8440255859375}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 11386], ['ood', 34551], ['ood', 51600], ['ood', 12180], ['ood', 50538]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5913244460817588, 2.8421430782286103, 3.682144310068015, 4.19189528082978, 4.419475951803852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.221055269241333})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.0811548233032227})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.3136420249938965})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.5716662406921387})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.668381929397583})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.5911, 'crossentropy': 3.175994140625}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 906], ['ood', 32867], ['ood', 51205], ['ood', 47663], ['id', 57486]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.4319785614548448, 2.5183661651707614, 3.340944679383205, 3.885778603580169, 4.212827377862165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.668961524963379})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.144010066986084})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.688699722290039})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.3002240657806396})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.8052663803100586})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.892181634902954})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.942465305328369})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.8577489852905273})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.025509834289551})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1313605308532715})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6454, 'crossentropy': 3.1341326171875}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 27645], ['ood', 19335], ['ood', 34277], ['ood', 22561], ['ood', 10010]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5879400207425474, 2.8088134443962467, 3.712070210788598, 4.191959108667841, 4.4172319094952925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.8567774295806885})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.546044111251831})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.762803554534912})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.846129894256592})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.3250062465667725})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.631, 'crossentropy': 2.4381849609375}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 13927], ['ood', 1682], ['ood', 53136], ['ood', 6364], ['ood', 30123]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3706314283852052, 2.6003195638052476, 3.4443431211833992, 3.959188334718603, 4.260314354464795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.1088290214538574})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.5872764587402344})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9899027347564697})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.787956714630127})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0620150566101074})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.7878224849700928})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.361812114715576})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2898125648498535})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 3.453992578125}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 5117], ['ood', 20648], ['ood', 54264], ['ood', 56348], ['ood', 46905]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4928111835207127, 2.733246267519657, 3.600232787097089, 4.128546501965495, 4.383559100152814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.943666696548462})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.492952346801758})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.667877674102783})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7368059158325195})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.222019672393799})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3199663162231445})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.2262747287750244})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6213, 'crossentropy': 3.0330931640625}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 28437], ['ood', 5222], ['ood', 36357], ['ood', 9523], ['ood', 19645]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5283413295080557, 2.7816786553815662, 3.6499479281647638, 4.162838921443782, 4.411776364616149]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.071352243423462})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.45668363571167})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9298267364501953})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2246861457824707})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.982011318206787})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.1638851165771484})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0881495475769043})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.6344549655914307})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.4131569862365723})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6285, 'crossentropy': 3.1019833984375}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 51265], ['ood', 22518], ['ood', 14649], ['ood', 39956], ['ood', 25311]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4604763321767715, 2.6682277976917823, 3.545798759015227, 4.065336567853411, 4.365542532588593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.9038808345794678})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.334378242492676})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.599686622619629})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.922527551651001})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.0561556816101074})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.182509660720825})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9394350051879883})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.102861166000366})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.432188034057617})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6301, 'crossentropy': 3.263314453125}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 56004], ['ood', 27105], ['ood', 43456], ['ood', 19686], ['ood', 33740]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.581499261458689, 2.788975499623816, 3.627931377300598, 4.145315300588562, 4.395141062224187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9676814079284668})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4593586921691895})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.8996496200561523})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.029144763946533})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.3322014808654785})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6333, 'crossentropy': 2.6680388671875}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 33873], ['ood', 25460], ['ood', 14260], ['ood', 26184], ['ood', 26770]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4198903075296616, 2.5720204215419553, 3.4449135600760528, 3.9770509355195403, 4.270987098339063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.0654919147491455})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.7329578399658203})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1028709411621094})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.1298179626464844})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.4962809085845947})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.646850109100342})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.59305477142334})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.811342477798462})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6158, 'crossentropy': 3.799248828125}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 6358], ['ood', 19931], ['ood', 44127], ['ood', 45504], ['ood', 51276]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.563623287344051, 2.7748899847345037, 3.623649541584002, 4.1323322763213675, 4.40675472769104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.143519401550293})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.577409267425537})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.7712624073028564})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1875803470611572})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.4360105991363525})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6212, 'crossentropy': 2.7609791015625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 45161], ['ood', 42714], ['ood', 45058], ['ood', 50510], ['ood', 27431]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4581836246512154, 2.6505080679372104, 3.583331721021139, 4.09620005662913, 4.390836409969362]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.9865156412124634})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.3769755363464355})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6638622283935547})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.9359498023986816})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9949026107788086})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6365, 'crossentropy': 2.7242865234375}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 19335], ['ood', 12758], ['ood', 19686], ['ood', 46623], ['ood', 27738]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4604867862557276, 2.620827070973627, 3.4667332333932475, 3.9729366119790015, 4.268709111681541]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.00246524810791})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.260890007019043})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.756077527999878})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.891655921936035})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.894961357116699})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3152554035186768})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.110908031463623})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.761414051055908})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6341, 'crossentropy': 3.1427935546875}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 35753], ['ood', 14798], ['id', 53054], ['ood', 11510], ['ood', 52312]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.574447415351648, 2.810598016901319, 3.6775169283551303, 4.175816568679868, 4.40952230267702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.9753363132476807})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.6884965896606445})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.2466683387756348})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.3683886528015137})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.489166736602783})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.6209917068481445})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6053, 'crossentropy': 3.1965412109375}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 14716], ['ood', 18301], ['ood', 22547], ['id', 50210], ['ood', 36329]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.419659713972576, 2.650913962066232, 3.487164706933001, 4.010045229461475, 4.311978702940159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.8145010471343994})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2877721786499023})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.4884517192840576})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.6148104667663574})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9822826385498047})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6306, 'crossentropy': 2.56638359375}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 35729], ['ood', 11154], ['ood', 30511], ['ood', 14164], ['ood', 10521]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4066893565531196, 2.5479784676648136, 3.3703682344912744, 3.891719135267696, 4.227122748216824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9111632108688354})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.8501434326171875})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7623653411865234})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.425478935241699})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.912081718444824})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.1199889183044434})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.723560333251953})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3909759521484375})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.5233404636383057})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.63, 'crossentropy': 3.47358203125}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 19761], ['ood', 38794], ['ood', 46292], ['ood', 49896], ['ood', 5744]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5659587905428975, 2.747715772852829, 3.6459207014427513, 4.1364291641861275, 4.393191688535977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.74837064743042})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.2490553855895996})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.7547967433929443})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8715004920959473})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6271, 'crossentropy': 1.933337890625}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 38167], ['ood', 6875], ['ood', 48463], ['ood', 51279], ['ood', 55730]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2666724855208642, 2.2485886676790985, 2.9792736725313294, 3.536098352061746, 3.9054758786326316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.0871663093566895})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.3734612464904785})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0814595222473145})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.1850035190582275})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1893515586853027})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6132, 'crossentropy': 2.5038515625}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 1682], ['ood', 26405], ['ood', 48323], ['ood', 38906], ['ood', 49896]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2960988815681944, 2.4491991378925455, 3.309216679077192, 3.877228601156361, 4.197008474950674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.025785446166992})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.57783579826355})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.844484567642212})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.430326461791992})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2493844032287598})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.324054479598999})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6272, 'crossentropy': 3.1330599609375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 23469], ['ood', 14715], ['ood', 28226], ['ood', 31779], ['ood', 47448]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.510260818734122, 2.7582090125938308, 3.6437791186783155, 4.149565367976557, 4.389623732552112]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.0356507301330566})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.6418802738189697})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.6579537391662598})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1533403396606445})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.257417917251587})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6281, 'crossentropy': 2.742551171875}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 17762], ['ood', 24589], ['ood', 24602], ['ood', 49429], ['ood', 7891]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4112876781462131, 2.503436855801716, 3.3655927025150003, 3.9270994959311576, 4.235812028375896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.9908008575439453})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5749917030334473})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.0144753456115723})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9540719985961914})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.07242488861084})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.206472635269165})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6288, 'crossentropy': 3.02133984375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 33852], ['ood', 19949], ['ood', 17728], ['ood', 51193], ['ood', 45760]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5936512153674345, 2.739565507841444, 3.5781098086582848, 4.085349604015703, 4.363319982258792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9370396137237549})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.479919910430908})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.6607506275177})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7710824012756348})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1611814498901367})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.203362226486206})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1297972202301025})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.326159715652466})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.166923999786377})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6348, 'crossentropy': 3.424272265625}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 51600], ['ood', 23080], ['ood', 2121], ['ood', 54536], ['ood', 59273]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.527180663207208, 2.8171315074721974, 3.7020530041488975, 4.204539753469677, 4.430587544517837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.019453763961792})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.358402729034424})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6126489639282227})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.808779239654541})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0135879516601562})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.867305040359497})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6334, 'crossentropy': 2.8653146484375}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 906], ['ood', 3336], ['ood', 31514], ['ood', 21837], ['ood', 1688]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5418489058847231, 2.653936792169075, 3.486021199055312, 4.020876559407917, 4.307826801583035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.054029941558838})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.960761070251465})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6264376640319824})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9695162773132324})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.253849506378174})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.024794340133667})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6299, 'crossentropy': 2.7774376953125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 54377], ['ood', 36427], ['ood', 4817], ['ood', 19495], ['ood', 19138]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4576011770368074, 2.630326521271571, 3.5154771778723344, 4.0432834783088385, 4.313481820932106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9032602310180664})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.7256407737731934})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.0217132568359375})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1010923385620117})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6278, 'crossentropy': 2.1024666015625}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 7946], ['ood', 32489], ['ood', 55866], ['ood', 21886], ['ood', 8969]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.393549843089846, 2.4352699357416485, 3.182961132498919, 3.7109593103757614, 4.071181142158428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8228516578674316})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.433925151824951})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.703909397125244})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0262112617492676})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3991589546203613})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2048397064208984})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6379, 'crossentropy': 2.966288671875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 32056], ['ood', 45230], ['ood', 47552], ['ood', 11502], ['ood', 41176]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5510599337477897, 2.677841038862975, 3.520568990209598, 4.065105608559639, 4.339364062907446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9047367572784424})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.329042911529541})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.190235137939453})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.7408559322357178})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6072, 'crossentropy': 2.1750232421875}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 4717], ['ood', 58394], ['ood', 21305], ['ood', 38389], ['ood', 32776]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2448147429509837, 2.2709280932290223, 3.029907530329498, 3.5876376543496002, 3.965960018620395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.8693642616271973})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.2873892784118652})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.609910488128662})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.7573394775390625})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.5896716117858887})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 2.4939951171875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 11386], ['ood', 30322], ['ood', 48323], ['ood', 5684], ['ood', 39619]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5079147006969098, 2.60405130225147, 3.3858521692475696, 3.9106363081343147, 4.236016027724301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.037689447402954})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6885087490081787})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.1191787719726562})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9247007369995117})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.2201194763183594})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2948226928710938})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.574378490447998})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6264, 'crossentropy': 3.309427734375}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 39414], ['ood', 34322], ['ood', 48968], ['ood', 23381], ['ood', 25823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.472240440906966, 2.662059022166477, 3.5224098553484184, 4.0764175174682205, 4.347000640806045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.8631988763809204})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.680330753326416})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.901047706604004})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7332611083984375})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.1087567806243896})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9364633560180664})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.246854782104492})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.1546082496643066})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.438279151916504})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.924406051635742})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2894394397735596})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.69675350189209})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.6849379539489746})
store['active_learning_steps'][53]['training']['best_epoch']=10
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.648, 'crossentropy': 3.34638125}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 42298], ['ood', 56526], ['ood', 6424], ['ood', 5541], ['ood', 6425]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6581304620272945, 2.821233896661772, 3.658918755901875, 4.153210785295386, 4.407910422876993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9358088970184326})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6648521423339844})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.7492880821228027})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.936704635620117})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.137545108795166})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.247119426727295})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2935383319854736})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.163604736328125})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.8223185539245605})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.963870048522949})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.133896589279175})
store['active_learning_steps'][54]['training']['best_epoch']=8
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6469, 'crossentropy': 3.391396484375}
