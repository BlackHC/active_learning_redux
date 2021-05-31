store = {}
store['timestamp']=1622154487
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=19']
store['commit']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['github_url']='311214a34d20da1dd5e1051078f9aa6022268d47'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=19
store['worker_id']=19
store['num_workers']=40
store['config']={'seed': 1255, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 2000, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 7807, 20860, 3681, 21628, 48176, 50727, 39616, 3528, 43419, 28970, 15619, 50035, 25394, 16182, 55460, 1397, 40148, 40970, 47567, 4203, 15751, 30302, 7484, 5403, 28830, 15139, 26135, 35786, 3067, 37912, 51065, 12013, 16972, 55471, 55714, 46607, 36213, 18748, 36238, 21377, 7626, 35244, 33203, 50274, 54825, 3271, 13995, 58882, 16854, 43918, 34553, 30244, 14754, 37225, 35296, 4550, 14668, 7519, 35276, 35936, 53098, 15224, 57336, 13276, 21583, 16705, 3104, 41589, 31241, 14179, 34946, 56381, 51568, 58121, 55356, 16313, 33299, 44984, 55429, 51813, 18415, 7251, 58597, 48148, 50917, 49011, 46294, 17853, 18558, 42527, 4749, 48793, 33762, 35677, 45579, 27951, 44271, 26867, 18823, 45093, 46214, 54526, 9487, 19646, 10717, 52740, 53890, 33973, 56510, 28286, 50581, 51558, 13375, 56897, 10129, 7380, 16911, 46824, 1867, 13545, 36855, 2819, 56842, 49737, 34327, 53174, 42540, 32838, 57785, 46442, 43571, 56400, 35940, 11007, 29178, 13754, 49506, 41591, 27185, 45856, 21922, 54158, 42450, 285, 29143, 5894, 15358, 31683, 56440, 46497, 39144, 31797, 28715, 2676, 49685, 29159, 28487, 46117, 4419, 45883, 1739, 57549, 27352, 3235, 18682, 31586, 13027, 28497, 58434, 1459, 15695, 21140, 31194, 21059, 49947, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45089, 25349, 2876, 16157, 39707, 36289, 5932, 18882, 37986, 33157, 18929, 2336, 15825, 33438, 51589, 41508, 6703, 3531, 47523, 10202, 8585, 28404, 18352, 18359, 57028, 28522, 30238, 10682, 51405, 5416, 38604, 13135, 13513, 31343, 2178, 22429, 60, 54546, 19376, 17023, 52414, 43256, 34695, 34614, 19806, 44920, 22631, 44195, 46830, 41898, 6949, 22363, 28508, 58061, 35424, 25257, 18866, 28935, 17107, 20693, 11800, 7126, 14587, 2625, 440, 36827, 6649, 8824, 6813, 36904, 5054, 40610, 20997, 55858, 33673, 28916, 10240, 33251, 44235, 182, 1476, 4317, 24254, 30727, 14633, 17291, 46197, 73, 11074, 26198, 58265, 46286, 41280, 11879, 32229, 39933, 19827, 49435, 52960, 9806, 33598, 8732, 8385, 37892, 11835, 18726, 43719, 13439, 19595, 55576, 21925, 885, 15813, 43697, 27375, 596, 50237, 1062, 55999, 19334, 47908, 31370, 17178, 10220, 23409, 7209, 32114, 19371, 24903, 57746, 41522, 4065, 853, 40707, 22333, 48535, 44924, 8134, 1655, 31769, 14908, 41174, 28603, 39261, 39224, 33854, 9509, 54045, 56391, 40723, 45405, 21159, 25226, 531, 55424, 41651, 7397, 43003, 36771, 53335, 25057, 16525, 39134, 7078, 17459, 31011, 41224, 32698, 14964, 26755, 48716, 16818, 11562, 27046, 10441, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 29546, 51216, 56115, 33474, 22990, 49378, 12171, 13088, 18018, 38664, 32996, 17878, 40272, 28768, 37366, 6358, 23148, 49567, 37784, 15904, 8882, 39009, 33461, 15845, 42738, 57007, 37053, 36608, 46966, 14652, 6915, 13551, 51112, 26852, 16442, 33198, 2462, 20615, 30893, 8214, 27619, 7275, 33761, 24393, 16631, 20363, 2067, 56245, 8648, 54174, 57057, 14190, 4418, 38899, 49438, 45526, 45981, 57510, 2691, 53164, 48183, 16271, 41971, 22358, 39381, 25862, 12007, 31436, 36584, 55022, 56786, 42084, 25919, 27941, 23132, 20256, 36776, 28201, 37263, 7167, 4767, 58503, 34049, 36808, 33286, 30741, 50909, 54981, 27770, 39218, 48314, 35203, 1079, 27995, 41673, 29257, 12098, 24815, 20732, 17523, 49532, 52754, 56143, 44521, 55870, 26071, 19249, 10849, 46523, 49962, 3407, 6875, 20781, 11887, 56026, 11781, 17735, 54236, 6108, 45391, 39847, 11938, 36583, 3718, 28801, 42075, 37166, 36283, 46999, 9814, 35740, 44407, 39889, 54809, 50966, 48025, 33111, 24935, 30147, 4810, 44251, 46819, 35562, 48591, 27746, 172, 53291, 24, 23617, 47873, 6656, 4329, 25011, 55975, 2644, 8984, 33362, 6891, 49763, 25498, 9927, 31031, 36034, 40985, 6776, 49, 30984, 56387, 30312, 27578, 6736, 34598, 48760, 20959, 17622, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 2773, 54536, 34513, 52890, 52773, 4205, 38704, 19265, 24668, 56723, 3010, 8680, 1690, 1071, 22123, 13738, 48147, 32632, 13161, 41734, 30910, 218, 21057, 36980, 37741, 56561, 23136, 2754, 95, 48021, 36355, 57213, 9848, 27083, 33017, 9825, 34357, 37042, 38006, 9094, 57286, 371, 6767, 33147, 9166, 47621, 10266, 5384, 4354, 39678, 3750, 52154, 13078, 28871, 33756, 24009, 6215, 30861, 17872, 1182, 57939, 26314, 9638, 55592, 593, 50194, 56375, 50320, 10542, 57349, 1399, 16326, 31975, 44888, 5262, 213, 50298, 13588, 21480, 5961, 47800, 23428, 17913, 4795, 31491, 42297, 32212, 5033, 14171, 14547, 6695, 36444, 37395, 19347, 48625, 38091, 36735, 48891, 52765, 21343, 9775, 48635, 36390, 22013, 55461, 3923, 45588, 23929, 42951, 7436, 20833, 11193, 26082, 5620, 41977, 17781, 33892, 5769, 18934, 28114, 58321, 30614, 7568, 15640, 28967, 10123, 2963, 15973, 47087, 48809, 41366, 47818, 30241, 26116, 167, 9793, 52135, 8774, 2285, 36473, 58881, 38179, 31978, 57632, 47611, 50865, 39648, 47976, 19339, 34294, 2572, 16662, 55101, 3758, 48838, 34985, 50937, 5424, 11819, 55777, 46892, 36870, 11517, 24725, 44032, 50001, 4294, 35777, 131, 56426, 52158, 10048, 21795, 3685, 44842, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 46938, 31010, 16704, 5870, 18076, 38817, 42762, 58038, 31833, 38063, 31221, 51418, 27283, 32596, 17948, 29505, 46165, 35374, 55510, 19279, 37055, 47630, 35106, 30771, 43130, 56977, 27077, 48437, 33483, 17142, 6600, 5338, 37950, 22669, 24253, 2169, 29105, 391, 47026, 49620, 29756, 443, 32143, 47622, 45446, 32880, 17728, 43599, 56627, 17870, 6187, 18016, 40399, 23197, 30237, 52141, 47793, 16425, 32506, 45658, 39268, 36030, 18011, 20350, 13669, 18273, 5922, 31868, 56946, 31438, 6529, 55852, 23212, 58195, 42659, 11303, 5755, 39393, 13660, 14631, 46564, 37160, 13945, 50818, 43264, 36267, 3654, 3619, 1598, 44856, 55175, 4649, 25421, 25229, 45948, 6887, 34103, 12178, 51908, 58159, 1961, 50441, 34237, 34370, 37107, 24619, 5936, 7874, 17811, 40802, 7956, 53387, 7768, 21680, 29520, 29087, 28980, 6625, 48127, 37621, 57583, 24172, 44469, 44817, 2212, 1910, 23950, 52137, 52218, 15265, 16560, 44498, 55274, 30280, 52676, 53842, 17902, 15607, 9492, 49517, 42532, 27048, 42587, 51326, 46709, 24491, 40592, 13572, 8812, 57617, 12295, 36099, 17780, 30565, 17041, 55156, 31485, 9132, 35215, 25033, 10461, 41721, 21191, 54774, 23833, 34363, 6948, 36440, 1798, 41242, 38755, 48235, 54031, 10080, 53761, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 14888, 26845, 41136, 10437, 17644, 19857, 38828, 28222, 15143, 31372, 5389, 8284, 35602, 1482, 46499, 23781, 15787, 50579, 47568, 10799, 13860, 55016, 44999, 52950, 9578, 23231, 22938, 2158, 36994, 6571, 12980, 35631, 46433, 7739, 23903, 23338, 32682, 2976, 3816, 42096, 28318, 24410, 22512, 57548, 5792, 15071, 635, 8126, 19875, 42040, 103, 42870, 20776, 56353, 32909, 14585, 12576, 18148, 9032, 31896, 519, 41836, 22300, 58154, 18092, 6185, 10828, 35449, 642, 31311, 15737, 32099, 39980, 22223, 54402, 49688, 33141, 51529, 52458, 20462, 50154, 36022, 58190, 40310, 12193, 11507, 22144, 1926, 9781, 46968, 5126, 13009, 36918, 36740, 31495, 13747, 21731, 14384, 54740, 7065, 18243, 41525, 50821, 50736, 5739, 30566, 23363, 27760, 23310, 41116, 27484, 46015, 8282, 32619, 7953, 10416, 24321, 30680, 34725, 14199, 32271, 55496, 4636, 48736, 35959, 45869, 19302, 55704, 27035, 7620, 936, 31464, 15914, 8254, 18412, 10558, 16448, 58023, 42253, 2588, 21201, 259, 19913, 31172, 21114, 57994, 44522, 18492, 10996, 28560, 36284, 43793, 41866, 43946, 58407, 7939, 12060, 36655, 32568, 5874, 18691, 4905, 30486, 27843, 30434, 53866, 12203, 47111, 37484, 45790, 31472, 49540, 14993, 16680, 58506, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 23002, 7414, 47776, 14241, 38539, 4820, 33069, 38318, 45335, 16975, 57036, 36882, 43457, 41879, 10897, 43375, 1924, 3378, 11836, 32249, 5615, 52072, 40932, 35025, 22259, 1250, 34935, 47110, 36446, 2737, 38185, 30979, 30931, 25616, 57008, 16725, 7442, 13601, 56228, 19885, 28641, 31019, 14920, 52438, 56349, 20542, 52720, 37557, 43477, 11537, 1058, 41353, 58140, 687, 46665, 39370, 53972, 3133, 56834, 20316, 3127, 51925, 916, 14272, 23186, 58378, 29543, 33306, 13362, 31937, 12635, 47299, 2185, 14398, 38702, 14412, 46954, 5528, 22165, 52963, 30056, 39906, 40162, 46896, 54054, 40243, 28760, 29895, 30256, 21578, 23870, 29384, 53426, 8256, 33160, 41979, 22381, 13590, 57651, 23949, 42355, 3709, 53088, 27228, 40666, 53257, 5551, 57902, 31754, 8144, 42345, 37134, 53294, 5305, 46799, 19004, 50299, 14655, 9812, 31006, 29523, 3668, 53737, 3892, 27607, 16987, 1000, 23477, 19637, 39267, 53292, 23368, 3478, 24736, 22070, 52876, 46688, 3224, 44828, 48256, 37806, 24594, 30835, 15191, 8226, 26221, 19425, 26944, 14911, 10971, 54710, 5646, 21485, 45341, 50236, 15216, 1973, 4372, 22797, 24256, 38299, 26132, 26218, 20438, 48775, 22915, 37998, 30419, 13339, 13155, 12773, 32933, 58137, 42662, 50916, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 30134, 19457, 24360, 12140, 24223, 4826, 17753, 25620, 43969, 27468, 32188, 22246, 14450, 30281, 43507, 32857, 28844, 9875, 53560, 22037, 36523, 58080, 49363, 32834, 10344, 27076, 1480, 9560, 51340, 32654, 33106, 35232, 48013, 46114, 14957, 34336, 1241, 22086, 54091, 578, 16837, 32709, 31525, 47102, 2514, 14928, 27370, 56727, 46586, 36315, 38171, 6994, 35500, 41954, 51445, 4267, 50636, 47437, 48744, 11588, 12528, 55739, 2099, 49112, 46614, 39464, 12900, 29025, 13469, 44209, 29251, 6478, 32657, 47847, 49329, 19600, 12052, 47544, 41145, 42018, 44762, 57560, 42283, 30432, 29643, 3435, 1249, 889, 24073, 46623, 49922, 57628, 38213, 7440, 37671, 38705, 8072, 58835, 6147, 47460, 34172, 5655, 49736, 35233, 32557, 30924, 52563, 48403, 20722, 18663, 30755, 16017, 43087, 51595, 55379, 27637, 51319, 45141, 31030, 29555, 54939, 36031, 15673, 28194, 27920, 27539, 682, 46718, 49268, 32315, 40059, 10944, 42127, 51557, 533, 8467, 51827, 38541, 22221, 298, 16888, 14061, 6157, 31951, 20073, 32545, 12479, 18936, 7026, 1718, 54262, 57105, 10979, 54672, 4453, 58031, 21354, 49710, 35319, 38777, 47973, 56608, 53809, 34418, 56893, 43836, 20118, 58405, 40582, 38121, 28763, 20677, 45932, 26934, 12225, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 11552, 44780, 1091, 14669, 50513, 44127, 51794, 55203, 51305, 27865, 7362, 50607, 4561, 37616, 25909, 47465, 22780, 4686, 45245, 2036, 7092, 57432, 47536, 53653, 31224, 44709, 30829, 17217, 46788, 31971, 22686, 32573, 9048, 47583, 21853, 10660, 14498, 38160, 18899, 16200, 33491, 29203, 42186, 36972, 43453, 57714, 25810, 13848, 23723, 40181, 4937, 47685, 1884, 29591, 54663, 17668, 55489, 37175, 27020, 33520, 31037, 58157, 3310, 9149, 24955, 53097, 4628, 50002, 31739, 4779, 46933, 4253, 37922, 34197, 31258, 5046, 38958, 55451, 8780, 55235, 7054, 29189, 22234, 34594, 22584, 27499, 2175, 14290, 10215, 31630, 3384, 17463, 47579, 24394, 20360, 47368, 9712, 35160, 56197, 4315, 9469, 39518, 55006, 52741, 25240, 1374, 9607, 12878, 3242, 53549, 13028, 42277, 55115, 39139, 53195, 53298, 14512, 33176, 15354, 2042, 25849, 21272, 26569, 9425, 41002, 27694, 56339, 753, 33500, 51548, 39705, 31068, 5652, 13705, 34908, 24524, 49131, 25987, 14797, 45593, 56994, 28653, 58477, 40652, 18644, 9615, 34858, 976, 34105, 10630, 9262, 43044, 2648, 27409, 3953, 14588, 58332, 57155, 38763, 52832, 15421, 25115, 33015, 55345, 43173, 15541, 44557, 46809, 701, 17216, 28324, 38608, 22465, 55192, 19346, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896, 54097, 55453, 6051, 50242, 7145, 1707, 52341, 50793, 37544, 52803, 39333, 20497, 27599, 16433, 57801, 47660, 54479, 50948, 19549, 32697, 21552, 36219, 47491, 10358, 37613, 57995, 9909, 2559, 2290, 34007, 41379, 24125, 42306, 35317, 37159, 48865, 4942, 16146, 37647, 350, 9395, 47960, 16889, 27549, 22677, 21368, 23011, 386, 50848, 45538, 26847, 4128, 4027, 47665, 15402, 14990, 55413, 33065, 45332, 22637, 56602, 10524, 1023, 41782, 10361, 27421, 57189, 8861, 24026, 19327, 27401, 55756, 39206, 23829, 39731, 48652, 40768, 2561, 10959, 37267, 4468, 51660, 24371, 42539, 25591, 42651, 22744, 14346, 47286, 17616, 48309, 29599, 7672, 52734, 29000, 54915, 11218, 4392, 19367, 56948, 6630, 52662, 486, 19423, 26966, 30159, 42529, 557, 6475, 11876, 21688, 46116, 34918, 37925, 52883, 53785, 24895, 54758, 23632, 44770, 7346, 11047, 31397, 48445, 21672, 6080, 28599, 57497, 18688, 7188, 28881, 7502, 19447, 47501, 41252, 34629, 21250, 4699, 46454, 27685, 50312, 50811, 36990, 9963, 28986, 36342, 13029, 158, 37215, 19803, 35325, 4029, 48255, 35322, 45757, 28359, 28483, 39749, 6252, 35245, 43693, 55119, 11471, 12554, 16589, 43648, 33395, 37723, 29746, 30442, 19042, 5020, 37311, 4600, 14299]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.6593687534332275})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.235257863998413})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.611591339111328})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.048484802246094})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 3.7208352088928223})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.718778133392334})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5884, 'crossentropy': 3.694909765625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3561656475067139})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.3846526145935059})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.5218037366867065})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.486254334449768})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3354638814926147})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 35464], ['ood', 20113], ['ood', 36752], ['id', 18984], ['id', 34052]], 'labels': [-1, -1, -1, 6, 3], 'scores': [1.1699305705960326, 2.0339175493487245, 2.608273357346776, 2.9287511130301036, 3.0751563906137074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.246762752532959})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.257645845413208})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.863971710205078})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.8772270679473877})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5881, 'crossentropy': 2.5170853515625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.3015849590301514})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.293755054473877})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2909398078918457})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 11424], ['ood', 31259], ['ood', 42472], ['ood', 8711], ['id', 57812]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1128703568813954, 1.8839869662509865, 2.395290801893612, 2.7096135340336716, 2.8694062412045103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 2.4458625316619873})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.70114803314209})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 3.4537954330444336})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.901639461517334})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.978376865386963})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.4488885402679443})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.954939126968384})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.629403591156006})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.286155859375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3623191118240356})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.347158432006836})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3308466672897339})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3500218391418457})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.335484266281128})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3225228786468506})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 30454], ['ood', 27393], ['ood', 51181], ['ood', 44870], ['id', 39261]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.1218433491355504, 1.968463254652708, 2.496534434988382, 2.7528586870561282, 2.856739855418608]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.094977855682373})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.8208141326904297})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8817977905273438})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2962918281555176})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.0474939346313477})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.4066543579101562})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5342588424682617})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.8400423526763916})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6304, 'crossentropy': 3.31817265625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2384722232818604})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1927638053894043})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.219346046447754})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.241760015487671})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2261981964111328})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.215813398361206})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2071677446365356})
store['active_learning_steps'][3]['eval_training']['best_epoch']=7
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 50752], ['ood', 11648], ['id', 32512], ['ood', 10976], ['id', 49962]], 'labels': [-1, -1, 8, -1, 2], 'scores': [1.1861210463638048, 2.10162615470363, 2.7756581106051774, 3.086822484880795, 3.199300160741444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.981881022453308})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.693608045578003})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.0854170322418213})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.0022172927856445})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.908504009246826})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.325815200805664})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.2917025089263916})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.637157917022705})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.623, 'crossentropy': 3.14556328125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1844251155853271})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2019431591033936})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.211306095123291})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2160544395446777})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.206892490386963})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1977579593658447})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1783909797668457})
store['active_learning_steps'][4]['eval_training']['best_epoch']=5
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 17301], ['ood', 23915], ['ood', 14865], ['ood', 6323], ['id', 52594]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.2144525107053112, 2.163788721434933, 2.710352907653296, 3.009606528239819, 3.157747934606907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.2562928199768066})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.706522226333618})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9431471824645996})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.8586325645446777})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.385110378265381})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3522441387176514})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6313, 'crossentropy': 2.8356412109375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.210591435432434})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2278385162353516})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1957509517669678})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2780330181121826})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2354927062988281})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 12468], ['ood', 55423], ['ood', 4797], ['id', 42562], ['id', 38221]], 'labels': [-1, -1, -1, 8, 1], 'scores': [1.1115612155251051, 1.973469743152612, 2.5868875421305892, 2.9064776281803697, 3.093017388637871]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.8114960193634033})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.4783761501312256})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9589104652404785})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.8186306953430176})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1646552085876465})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.5001273155212402})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3130412101745605})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6488, 'crossentropy': 3.0121697265625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1795682907104492})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1560606956481934})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.213315486907959})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1773536205291748})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.243797779083252})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.253068208694458})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 10303], ['ood', 49103], ['ood', 26114], ['id', 15341], ['id', 40570]], 'labels': [-1, -1, -1, 7, 8], 'scores': [1.1935339705635826, 2.0802403300889143, 2.652719982295138, 2.9377661243925317, 3.065942142812532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.737748146057129})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.095937967300415})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.2135958671569824})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.359428882598877})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6122665405273438})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.7048909664154053})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.8510775566101074})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.8248558044433594})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6542, 'crossentropy': 2.925661328125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.180586576461792})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1828255653381348})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1358550786972046})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1482012271881104})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1389617919921875})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1527516841888428})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 27118], ['ood', 29185], ['ood', 14389], ['id', 21615], ['id', 17823]], 'labels': [-1, -1, -1, 2, 3], 'scores': [1.1470262443857355, 2.0112459452905878, 2.586539864458131, 2.957076070083734, 3.133374881673136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.9029695987701416})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.428234100341797})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.5504558086395264})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7698490619659424})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.0086679458618164})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.263026237487793})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6442, 'crossentropy': 2.882976953125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2114136219024658})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1853604316711426})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2632911205291748})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1459965705871582})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1816282272338867})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 27035], ['ood', 18551], ['ood', 21255], ['id', 550], ['id', 59474]], 'labels': [-1, -1, -1, 3, 6], 'scores': [1.1284612141979182, 1.9316748750612018, 2.472907768138068, 2.759668698532588, 2.865789564862058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.559211015701294})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.2485265731811523})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.462287187576294})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7372360229492188})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3666396141052246})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.4009792804718018})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.9871912002563477})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6559, 'crossentropy': 2.88477578125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1404523849487305})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1542778015136719})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.195286512374878})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2304881811141968})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 12003], ['ood', 49204], ['ood', 8882], ['ood', 40573], ['id', 837]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.190836680558665, 2.0696453755682307, 2.633694454221269, 2.9117309823572644, 3.0182872943934322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7579872608184814})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.4154720306396484})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.761190891265869})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.791260004043579})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7130227088928223})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.2105698585510254})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.472698211669922})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.511996030807495})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6472, 'crossentropy': 2.7577935546875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1627438068389893})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2154579162597656})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2107675075531006})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3579906225204468})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2666529417037964})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2522337436676025})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 39751], ['ood', 38262], ['ood', 50728], ['ood', 26699], ['id', 50776]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.0516766841563738, 1.85575874920415, 2.481927108868991, 2.883068754306077, 3.0770743529284195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5599944591522217})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.2960407733917236})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.609278678894043})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.6463241577148438})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6413, 'crossentropy': 1.57009365234375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.1204720735549927})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0873966217041016})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.101118803024292})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 24298], ['ood', 46329], ['id', 53390], ['ood', 49060], ['ood', 11406]], 'labels': [-1, -1, 3, -1, -1], 'scores': [0.8363670005699515, 1.4668299725514422, 1.9317890564041003, 2.263276333237296, 2.482538471496169]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.990431547164917})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.3559412956237793})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.0910253524780273})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.740943670272827})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.2590394020080566})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.6677751541137695})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.4856786727905273})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.510240077972412})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.751526355743408})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.4376649856567383})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.6428511142730713})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 3.56680625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2060521841049194})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2119596004486084})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.261155128479004})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2828009128570557})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.258669376373291})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2923749685287476})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2871278524398804})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3191540241241455})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 14103], ['id', 32592], ['ood', 22276], ['ood', 57387], ['id', 27208]], 'labels': [-1, 5, -1, -1, 6], 'scores': [1.1532725041726972, 2.004549922784188, 2.556428695189786, 2.8165941996803667, 2.9325330980071254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.9251484870910645})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.4520797729492188})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.554936170578003})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7945079803466797})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.1048126220703125})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.23870849609375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.4340615272521973})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6306, 'crossentropy': 2.906234765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.163482666015625})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.188032865524292})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2340936660766602})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2090661525726318})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.207464575767517})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2102434635162354})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 3980], ['ood', 13377], ['ood', 44142], ['id', 15372], ['ood', 31540]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.1027469618381325, 1.9726999671604575, 2.5440534883342303, 2.9017254909233303, 3.067567273689396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.8324403762817383})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.256525754928589})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.770463466644287})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8606374263763428})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.367612361907959})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.385345697402954})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.2013611793518066})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.316685676574707})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.6909313201904297})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.709733486175537})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6428, 'crossentropy': 3.2147669921875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2574498653411865})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1849082708358765})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2701294422149658})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3112413883209229})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2568905353546143})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3417778015136719})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3568754196166992})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.423753023147583})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2837512493133545})
store['active_learning_steps'][14]['eval_training']['best_epoch']=9
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 32182], ['ood', 49207], ['ood', 57439], ['id', 29590], ['id', 23260]], 'labels': [-1, -1, -1, 2, 2], 'scores': [1.1526125687649293, 2.0027108961586313, 2.5998149903751138, 2.934070319997569, 3.105325736282511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6061595678329468})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.9605766534805298})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2597150802612305})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.8346638679504395})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.154567241668701})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.8059229850769043})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6525, 'crossentropy': 2.5763751953125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2125028371810913})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.142080545425415})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.145627498626709})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2009470462799072})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2427420616149902})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 16456], ['ood', 4727], ['id', 32856], ['ood', 22980], ['id', 44003]], 'labels': [-1, -1, 0, -1, 7], 'scores': [1.190239546034742, 2.0358312629393325, 2.6078533138914857, 2.915939067557762, 3.060916998968052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5982356071472168})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.153489112854004})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.6216087341308594})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4740400314331055})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.9689998626708984})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.002427577972412})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3834075927734375})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6437, 'crossentropy': 2.548359765625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.149693489074707})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2109776735305786})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1730458736419678})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2026710510253906})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.205782175064087})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2490859031677246})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 24340], ['ood', 16716], ['ood', 33976], ['ood', 25407], ['id', 33514]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.1918365735154115, 2.035649959293755, 2.59949148756487, 2.9328640606696066, 3.0823741605070882]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5023775100708008})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.113102912902832})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.473759651184082})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.443814754486084})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.734736919403076})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 3.0142784118652344})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.8332767486572266})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.020658016204834})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6676, 'crossentropy': 2.7739443359375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.194528341293335})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.228036880493164})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1714520454406738})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2497361898422241})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.223524570465088})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2057691812515259})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2363065481185913})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 12644], ['ood', 55089], ['ood', 40390], ['id', 2566], ['id', 31723]], 'labels': [-1, -1, -1, 7, 0], 'scores': [1.1130278612249747, 1.9971648484086257, 2.582473639214661, 2.9302921871370398, 3.0474954211645446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.6159389019012451})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.418668508529663})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.643153190612793})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.791463851928711})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.2723960876464844})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.147188425064087})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6377, 'crossentropy': 2.7233498046875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3096939325332642})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2701780796051025})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2368059158325195})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3163478374481201})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2698845863342285})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 19831], ['ood', 20739], ['ood', 54068], ['ood', 37915], ['ood', 24145]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9873326336920814, 1.7973339625932176, 2.380781847510412, 2.7084638703550477, 2.866521326168126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.6424223184585571})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1566386222839355})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7977046966552734})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.673509120941162})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.359684467315674})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6401, 'crossentropy': 2.3112904296875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2350807189941406})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2436513900756836})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2310004234313965})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.215153694152832})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 32182], ['ood', 23797], ['ood', 42259], ['ood', 30298], ['id', 27406]], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.9482451336274473, 1.7043101415521051, 2.2228633397786988, 2.5428610530364626, 2.701446173202325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5806934833526611})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.0384836196899414})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.3318843841552734})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.5794429779052734})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6838104724884033})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.115370512008667})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6455, 'crossentropy': 2.3993029296875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2330822944641113})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1616207361221313})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.196433186531067})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.243345856666565})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2046349048614502})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 54425], ['ood', 53048], ['ood', 39313], ['ood', 21147], ['ood', 8695]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.166904610590229, 2.0234138605991534, 2.5839589958392732, 2.8693415501119848, 2.981136873876876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.688154697418213})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9489171504974365})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.352950096130371})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6872730255126953})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.6337990760803223})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.005478620529175})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6464, 'crossentropy': 2.627039453125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2330348491668701})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2450339794158936})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2717933654785156})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3018622398376465})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2568697929382324})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 54857], ['ood', 29576], ['ood', 37380], ['id', 3748], ['ood', 49757]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.0317631244532817, 1.8145078883682748, 2.3410541595027063, 2.6877179245590135, 2.8690112485748793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.5673867464065552})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.1401491165161133})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.291520118713379})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1744484901428223})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6396, 'crossentropy': 1.5673455078125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1873350143432617})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1072940826416016})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.1201891899108887})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 23797], ['ood', 51183], ['ood', 2773], ['ood', 179], ['id', 52788]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.762647143304632, 1.2839340402205748, 1.719586210484163, 2.0273981277352453, 2.2473064941144267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.6040475368499756})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.9832813739776611})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.189378261566162})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6482458114624023})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.951043128967285})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9948458671569824})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6551, 'crossentropy': 2.3022451171875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2129199504852295})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.123852252960205})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.171367883682251})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2000114917755127})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1648857593536377})
store['active_learning_steps'][23]['eval_training']['best_epoch']=2
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 35817], ['ood', 41169], ['ood', 38587], ['ood', 6159], ['id', 58860]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1071311483192756, 1.897640036312381, 2.4844729059613853, 2.794319421708554, 2.898794499000034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5599042177200317})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1121439933776855})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3814492225646973})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8668293952941895})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.945145606994629})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9200258255004883})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.4761300086975098})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.6452789306640625})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.7123303413391113})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6425, 'crossentropy': 3.122249609375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2387863397598267})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2396667003631592})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2790818214416504})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2495392560958862})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3135015964508057})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.266448736190796})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3071620464324951})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2997422218322754})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 28464], ['ood', 5823], ['ood', 14340], ['id', 6955], ['ood', 5195]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.0132979997536595, 1.8408007773646196, 2.4086071738536106, 2.6767877591114333, 2.8404339397091842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.6189327239990234})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.1475989818573})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.3222734928131104})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.946983814239502})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.670231342315674})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.164184808731079})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0708694458007812})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.025263547897339})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.241929531097412})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6404, 'crossentropy': 3.1678671875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.308990240097046})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.265390157699585})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2915332317352295})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2829540967941284})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2780994176864624})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1995742321014404})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2865666151046753})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3196508884429932})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 54068], ['ood', 40452], ['ood', 12129], ['id', 42040], ['id', 8791]], 'labels': [-1, -1, -1, 5, 4], 'scores': [1.0906770340701268, 2.0103029673762856, 2.5977397566890508, 2.8872606247453056, 3.01864873437629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5465075969696045})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.8307290077209473})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.0895028114318848})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.693124771118164})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.685959815979004})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 1.9943142578125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1552915573120117})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.119592547416687})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1875373125076294})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.1025620698928833})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 11181], ['ood', 28285], ['ood', 50096], ['ood', 53048], ['ood', 53693]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.998554725379476, 1.7244393158712943, 2.2431771349637044, 2.575319095828588, 2.7644492127416074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.331486701965332})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.9527122974395752})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.239089012145996})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.208364963531494})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.7464160919189453})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.867428779602051})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.730532169342041})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.667, 'crossentropy': 2.400961328125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2086338996887207})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0840802192687988})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.139992594718933})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1260504722595215})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1648887395858765})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1000704765319824})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 2761], ['ood', 58310], ['ood', 16676], ['id', 30872], ['id', 2786]], 'labels': [-1, -1, -1, 6, 2], 'scores': [0.9830602960957104, 1.6880078367698874, 2.2295887698624197, 2.5242902212825262, 2.6978259703225635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4422922134399414})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8591299057006836})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.198972225189209})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.5864996910095215})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.360302448272705})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.877197742462158})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.663, 'crossentropy': 2.2156126953125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1102274656295776})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0554001331329346})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0324037075042725})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.0970066785812378})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.083977222442627})
store['active_learning_steps'][28]['eval_training']['best_epoch']=2
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 44072], ['ood', 42379], ['ood', 20476], ['ood', 2], ['id', 16131]], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.9943158027387122, 1.744091563116128, 2.2530622078281324, 2.5765706046246004, 2.7186952260473047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3951289653778076})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8896093368530273})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8407819271087646})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3252668380737305})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.4539828300476074})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.5892531871795654})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6663, 'crossentropy': 2.072709765625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0923141241073608})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1105775833129883})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.042612075805664})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.093592882156372})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0929203033447266})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 13428], ['ood', 5127], ['ood', 20945], ['ood', 12254], ['id', 13786]], 'labels': [-1, -1, -1, -1, 4], 'scores': [1.026875413113387, 1.8812714901001812, 2.4638040002560224, 2.826212994235024, 2.982065426960273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.4411925077438354})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.077134609222412})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.3534440994262695})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6746370792388916})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.9490761756896973})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.151394844055176})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.038815975189209})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.1573100090026855})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 3.2409892082214355})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6598, 'crossentropy': 3.0416771484375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1877434253692627})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1287243366241455})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.164262294769287})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1386361122131348})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.172359824180603})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.212946891784668})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1955608129501343})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2023634910583496})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 50391], ['ood', 41871], ['ood', 20375], ['id', 58626], ['ood', 3809]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.1504585511010432, 2.014595525818508, 2.589982944585477, 2.895839017256031, 3.07055035591459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4589805603027344})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.0560874938964844})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.407186985015869})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.377962589263916})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.762038469314575})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.7703421115875244})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.896723508834839})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.8383877277374268})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 3.1461105346679688})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.258331298828125})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.224491596221924})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6735, 'crossentropy': 2.88471796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1412780284881592})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.090787649154663})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1617834568023682})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2012782096862793})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1576008796691895})
store['active_learning_steps'][31]['eval_training']['best_epoch']=2
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 32999], ['ood', 10524], ['ood', 16869], ['id', 45176], ['ood', 27268]], 'labels': [-1, -1, -1, 1, -1], 'scores': [1.1296611814573876, 2.0437775268888374, 2.5845931822579633, 2.8551151738108604, 2.964042184316374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3039815425872803})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.7647414207458496})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.1854453086853027})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.5159080028533936})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.519618272781372})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.020404815673828})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.965728998184204})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6336, 'crossentropy': 2.568709375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.219163417816162})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1640653610229492})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2120933532714844})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1502983570098877})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1919337511062622})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1253678798675537})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 49138], ['ood', 146], ['ood', 8702], ['id', 46216], ['id', 32713]], 'labels': [-1, -1, -1, 8, 9], 'scores': [1.0782329454817763, 1.894023824571026, 2.468707450304206, 2.8111275310604213, 2.963991935446164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4542816877365112})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.8166680335998535})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.107121229171753})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.264369249343872})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8040478229522705})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.6301348209381104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.1767661571502686})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6598, 'crossentropy': 2.5388505859375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1315581798553467})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.095263957977295})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1336352825164795})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1102662086486816})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1165082454681396})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1296284198760986})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 44072], ['ood', 45407], ['ood', 30509], ['ood', 20959], ['ood', 23462]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0822352060937315, 1.9676662472923017, 2.5205665512673168, 2.7957988511003062, 2.926880716510243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.478649377822876})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8921771049499512})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.246936559677124})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.4460043907165527})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.053412675857544})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8933215141296387})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.037001848220825})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6297, 'crossentropy': 2.7241009765625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2926195859909058})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.158055305480957})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1784491539001465})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1832748651504517})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2170124053955078})
store['active_learning_steps'][34]['eval_training']['best_epoch']=2
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 49175], ['ood', 18838], ['ood', 34974], ['ood', 14400], ['ood', 35403]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1376979689281679, 2.059223322671576, 2.6538691990087786, 2.9904116601173945, 3.1671083346120312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.359379529953003})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.7714693546295166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.309974431991577})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.960237503051758})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.889101982116699})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.0476808547973633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.3981730937957764})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 2.79994921875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.201452612876892})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.0856568813323975})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1637496948242188})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2199010848999023})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.207861304283142})
store['active_learning_steps'][35]['eval_training']['best_epoch']=2
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 14283], ['ood', 16956], ['ood', 35883], ['ood', 14018], ['id', 56420]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.13136148477609, 1.9919291466176805, 2.493779095772811, 2.7370545628638547, 2.8244661442978067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4774792194366455})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.095432758331299})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.606612205505371})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.9290761947631836})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.299243927001953})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6239, 'crossentropy': 2.169354296875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2403870820999146})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.1627559661865234})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.219980239868164})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.1927307844161987})
store['active_learning_steps'][36]['eval_training']['best_epoch']=1
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 57628], ['ood', 33728], ['ood', 21487], ['ood', 59657], ['ood', 21012]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9809281717416365, 1.7340086012007903, 2.2991741625986535, 2.5853848614137007, 2.725834666399667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.445299506187439})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.9240105152130127})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.1983461380004883})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.576572895050049})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.734819173812866})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1723995208740234})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.9858524799346924})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.094574213027954})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.841768741607666})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.102527379989624})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6471, 'crossentropy': 2.945015234375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0961302518844604})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1671254634857178})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.171100378036499})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1642816066741943})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2711399793624878})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2666170597076416})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.208979845046997})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2136670351028442})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.206626296043396})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 20119], ['ood', 11154], ['ood', 32525], ['ood', 26444], ['ood', 28633]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9960912998678944, 1.800718823320628, 2.3738734382398485, 2.695362058323477, 2.876922684431517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3754279613494873})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.8710672855377197})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.218925714492798})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.512315273284912})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.663564682006836})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.736790180206299})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.1962099075317383})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0300323963165283})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6516, 'crossentropy': 2.68527265625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1355412006378174})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.178278923034668})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1345895528793335})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1127381324768066})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1088815927505493})
store['active_learning_steps'][38]['eval_training']['best_epoch']=2
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 17777], ['ood', 19347], ['ood', 32616], ['id', 11444], ['id', 58256]], 'labels': [-1, -1, -1, 6, 9], 'scores': [1.0898283182174637, 2.0143207844142745, 2.532987878932248, 2.829240231887768, 2.9581022287564274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4175140857696533})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.5459553003311157})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.9872549772262573})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.194779396057129})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4602303504943848})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.329622268676758})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.5660266876220703})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.668, 'crossentropy': 2.3454857421875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0871431827545166})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.077167272567749})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.062445878982544})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.042520523071289})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.025269627571106})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0560979843139648})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 3495], ['ood', 29126], ['ood', 10350], ['ood', 45284], ['id', 24581]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.0848616182050135, 1.9149003692917468, 2.514131662722152, 2.8609893690300687, 3.05269351952235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2311956882476807})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6377767324447632})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.016519784927368})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.2386491298675537})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.5429697036743164})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6601, 'crossentropy': 1.722772265625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.0751399993896484})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.046483039855957})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0199925899505615})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0363821983337402})
store['active_learning_steps'][40]['eval_training']['best_epoch']=2
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 46295], ['ood', 50517], ['ood', 21197], ['ood', 38496], ['ood', 18212]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.988230933259743, 1.7594875506128043, 2.3073272081337466, 2.632764994501402, 2.7912413972111105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3180452585220337})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.6485987901687622})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.2207064628601074})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.3317947387695312})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.470366954803467})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.6727657318115234})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.7624430656433105})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.9141592979431152})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.6469998359680176})
store['active_learning_steps'][41]['training']['best_epoch']=6
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6802, 'crossentropy': 2.799686328125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1109322309494019})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.127027988433838})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0746235847473145})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0679680109024048})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0704984664916992})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.149198293685913})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1272950172424316})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0865697860717773})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 59065], ['ood', 19404], ['ood', 42839], ['ood', 21147], ['id', 44728]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0297024771200711, 1.886985527175451, 2.4423709109851846, 2.7545306390524456, 2.9212996701006126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2223398685455322})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.6276687383651733})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.0665934085845947})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.080392837524414})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6625, 'crossentropy': 1.26769443359375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0928328037261963})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0739474296569824})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0324573516845703})
store['active_learning_steps'][42]['eval_training']['best_epoch']=3
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 38627], ['ood', 18273], ['ood', 8591], ['ood', 29871], ['ood', 31779]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7723878964735049, 1.3964774295638724, 1.8694858884112495, 2.2111475712497324, 2.472237325257243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3263585567474365})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.6266627311706543})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.019705295562744})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3329358100891113})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.3078272342681885})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6546, 'crossentropy': 1.80783125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1465247869491577})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0711137056350708})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.05228590965271})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0579988956451416})
store['active_learning_steps'][43]['eval_training']['best_epoch']=2
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 50494], ['ood', 14283], ['ood', 22194], ['ood', 51016], ['ood', 22135]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9280739658643928, 1.6966990044343393, 2.223434520828147, 2.541616695566791, 2.721676901938711]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.325181484222412})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6059930324554443})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.220287322998047})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.3123416900634766})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.3754563331604004})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6553, 'crossentropy': 1.7456734375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0817866325378418})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0292571783065796})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0453522205352783})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.0585641860961914})
store['active_learning_steps'][44]['eval_training']['best_epoch']=2
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 42707], ['ood', 20695], ['ood', 20057], ['ood', 10383], ['ood', 45376]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9535149903639137, 1.710637131999674, 2.2630132876256726, 2.5914428230455506, 2.747325179839226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.323148250579834})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.555586814880371})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.968794584274292})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.2657880783081055})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.456139087677002})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6622, 'crossentropy': 1.7140341796875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0614559650421143})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0460034608840942})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.024013638496399})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9782007932662964})
store['active_learning_steps'][45]['eval_training']['best_epoch']=2
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 14283], ['ood', 51415], ['ood', 32393], ['ood', 5127], ['ood', 51495]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9344308817133824, 1.673424877838754, 2.1950129778638, 2.5048690934278586, 2.6509466521925447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.23680579662323})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.6307365894317627})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.9860320091247559})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.277158737182617})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.392493724822998})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6664109230041504})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.5347940921783447})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.524820327758789})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.705233097076416})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.6025390625})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.622735023498535})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.762298822402954})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.124532699584961})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.8686578273773193})
store['active_learning_steps'][46]['training']['best_epoch']=11
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6769, 'crossentropy': 2.9749240234375}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0515046119689941})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0492777824401855})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0661418437957764})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0177206993103027})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.098029375076294})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1437063217163086})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1080288887023926})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0793371200561523})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1221919059753418})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0828769207000732})
store['active_learning_steps'][46]['eval_training']['best_epoch']=7
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 28467], ['ood', 53598], ['ood', 31892], ['id', 45096], ['id', 55897]], 'labels': [-1, -1, -1, 2, 1], 'scores': [1.0090760165306303, 1.8432222390206805, 2.3919676207037615, 2.6242628977233293, 2.738389476609097]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3159565925598145})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.568901777267456})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.9961209297180176})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.234738349914551})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4546587467193604})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6646, 'crossentropy': 1.6457998046875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0889736413955688})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0051915645599365})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0038293600082397})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0131597518920898})
store['active_learning_steps'][47]['eval_training']['best_epoch']=2
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 37276], ['ood', 50086], ['ood', 51342], ['id', 11486], ['id', 40470]], 'labels': [-1, -1, -1, 1, 2], 'scores': [0.8562206740690605, 1.5556271608910253, 2.112091479899763, 2.445593063046065, 2.6353472984223387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2468971014022827})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.57435142993927})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8695783615112305})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.1312851905822754})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.4684760570526123})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.1402173042297363})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6577, 'crossentropy': 2.1190974609375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0684874057769775})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0617506504058838})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.04167640209198})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.998350977897644})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0567026138305664})
store['active_learning_steps'][48]['eval_training']['best_epoch']=4
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 44072], ['ood', 16426], ['ood', 48356], ['ood', 8960], ['ood', 41217]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0540666199771107, 1.8513524519878994, 2.4101666292521866, 2.681730087881938, 2.838038072606384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2445321083068848})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.692917823791504})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.9830065965652466})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.2236289978027344})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.2674131393432617})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.4809775352478027})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6601, 'crossentropy': 2.0373568359375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.1256864070892334})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0184781551361084})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 0.9928303956985474})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.048901081085205})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0260112285614014})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 42741], ['ood', 37276], ['ood', 55395], ['ood', 50615], ['id', 12640]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.0700774986825257, 1.875504566864438, 2.3874076610649215, 2.6459337366381233, 2.76925641518791]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2855210304260254})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.5627670288085938})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.996497392654419})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.0245859622955322})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.279912233352661})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.532222270965576})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.5923922061920166})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6718, 'crossentropy': 2.2841474609375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1030160188674927})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9754586219787598})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1012179851531982})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.014143466949463})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0403647422790527})
store['active_learning_steps'][50]['eval_training']['best_epoch']=2
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 32668], ['ood', 28275], ['ood', 14071], ['ood', 16630], ['ood', 52169]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.063134777099623, 1.874895432110065, 2.467612543021722, 2.8029577615887202, 2.978828530894745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2614237070083618})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6600154638290405})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.8691420555114746})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.1269688606262207})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6595, 'crossentropy': 1.28182197265625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.10573410987854})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 0.9991258382797241})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0088939666748047})
store['active_learning_steps'][51]['eval_training']['best_epoch']=3
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 6536], ['ood', 55395], ['id', 1254], ['ood', 14655], ['ood', 39151]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.8243249987627723, 1.4048264888176152, 1.8663066405998965, 2.2152993004222896, 2.4354840654944487]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.326857089996338})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.5938091278076172})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.0436453819274902})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1788599491119385})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.43049955368042})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6784238815307617})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6679, 'crossentropy': 2.1481328125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.05647611618042})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0562583208084106})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0807758569717407})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0542266368865967})
store['active_learning_steps'][52]['eval_training']['best_epoch']=1
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 17271], ['ood', 41802], ['ood', 8978], ['id', 47337], ['ood', 24131]], 'labels': [-1, -1, -1, 4, -1], 'scores': [1.0431871339272, 1.8416905285763168, 2.4440911634792215, 2.763012170593698, 2.89853514385581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2490684986114502})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.5791406631469727})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8686078786849976})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.259378433227539})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.303407669067383})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.6584548950195312})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7603793144226074})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.678020477294922})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.6195311546325684})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6649, 'crossentropy': 2.585871484375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0664829015731812})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0961132049560547})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0128437280654907})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.065964937210083})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.137627363204956})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0733435153961182})
store['active_learning_steps'][53]['eval_training']['best_epoch']=3
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 40595], ['ood', 19686], ['ood', 44324], ['id', 50634], ['ood', 52079]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.1131534591970143, 1.9965612851077392, 2.582480800330603, 2.9093959494533372, 3.0877031524922725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2156352996826172})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4883182048797607})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9961154460906982})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.230971097946167})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6709, 'crossentropy': 1.2483654296875}
