store = {}
store['timestamp']=1620295762
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=10']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=40
store['config']={'seed': 12, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.1685566902160645})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5789003372192383})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.7932701110839844})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.9554247856140137})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6665, 'crossentropy': 1.9989484375}
store['active_learning_steps'][0]['acquisition']={'indices': [27120, 14817, 29343, 47983, 47683, 49107, 30566, 13464, 23347, 14644, 7979, 47889, 39685, 1319, 12223, 29433, 22169, 28838, 22769, 4723], 'labels': [2, 0, 5, 5, 5, 5, 5, 0, 8, 0, 8, 5, 0, 8, 2, 5, 2, 9, 2, 5], 'scores': [1.1918222308158875, 1.1301896572113037, 1.1220045685768127, 1.1128677129745483, 1.1087294220924377, 1.1064873933792114, 1.106163501739502, 1.098732352256775, 1.0981265902519226, 1.0960128903388977, 1.095155119895935, 1.0910265445709229, 1.0894176959991455, 1.087466537952423, 1.0843819975852966, 1.0812607407569885, 1.078421950340271, 1.0779612064361572, 1.076472282409668, 1.0706312656402588]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.2133398056030273})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.8901219367980957})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.455322027206421})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.5828914642333984})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6703, 'crossentropy': 2.0568515625}
store['active_learning_steps'][1]['acquisition']={'indices': [53989, 22661, 3300, 35051, 8413, 29390, 8411, 49505, 15751, 41469, 33027, 28520, 13491, 20179, 1563, 26629, 44882, 15853, 14063, 56726], 'labels': [2, 2, 2, 2, 2, 9, 2, 6, 2, 2, 2, 7, 2, 2, 2, 3, 9, 2, 2, 9], 'scores': [1.0243889689445496, 1.001585066318512, 0.994175136089325, 0.9851362705230713, 0.9835084080696106, 0.9708168506622314, 0.968447744846344, 0.9631419777870178, 0.9532678723335266, 0.9457035064697266, 0.941021740436554, 0.940600574016571, 0.9401561617851257, 0.9398587942123413, 0.9397129416465759, 0.9388657212257385, 0.9379436373710632, 0.9376702904701233, 0.9349236488342285, 0.9321103096008301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.0693869590759277})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.738682270050049})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5504589080810547})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.9532272815704346})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.628, 'crossentropy': 1.8490259765625}
store['active_learning_steps'][2]['acquisition']={'indices': [29368, 34899, 23315, 39285, 38615, 19187, 19335, 42763, 23289, 36427, 12345, 42517, 981, 48575, 3524, 24176, 52891, 17185, 59617, 57300], 'labels': [0, 7, 0, 3, 7, 7, 3, 7, 0, 3, 3, 5, 7, 7, 6, 3, 3, 7, 7, 3], 'scores': [0.8034302592277527, 0.7981460094451904, 0.7834282517433167, 0.7824123501777649, 0.7714636921882629, 0.768488347530365, 0.7672848701477051, 0.7622858285903931, 0.7601226568222046, 0.7599442601203918, 0.7576754093170166, 0.7557616233825684, 0.7535200119018555, 0.7511983513832092, 0.7508209943771362, 0.7472527027130127, 0.7454445362091064, 0.7450027465820312, 0.7439171671867371, 0.7438815236091614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7331922054290771})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6897085905075073})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.2507381439208984})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.072632074356079})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.418292999267578})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7332, 'crossentropy': 1.6074337890625}
store['active_learning_steps'][3]['acquisition']={'indices': [40573, 42239, 2933, 28455, 54077, 15973, 52971, 8700, 34429, 15679, 13991, 10997, 12247, 8714, 47089, 11113, 24295, 6844, 5605, 19531], 'labels': [4, 4, 5, 5, 3, 8, 2, 3, 4, 2, 5, 4, 4, 9, 4, 4, 4, -1, 3, 4], 'scores': [1.0471718311309814, 1.045625627040863, 1.036929190158844, 1.0325868725776672, 1.0323023200035095, 1.0253102779388428, 1.024404764175415, 1.0205716788768768, 1.0159812569618225, 1.0125163793563843, 1.009098768234253, 1.0044660568237305, 1.00333172082901, 1.00288325548172, 1.0006883144378662, 1.0003708004951477, 0.9967623353004456, 0.996277391910553, 0.9914268255233765, 0.9901183843612671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.1213808059692383})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4133514165878296})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.440986156463623})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5722686052322388})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7816, 'crossentropy': 1.0302681640625}
store['active_learning_steps'][4]['acquisition']={'indices': [15250, 13114, 5728, 17100, 29185, 10210, 56479, 20093, 10513, 46329, 18671, 36197, 8958, 49656, 36951, 2835, 44706, 2845, 50688, 29224], 'labels': [3, 3, 3, 3, 3, 3, 5, 5, 8, 3, 7, 7, 3, 9, 7, 7, 5, 8, 3, 3], 'scores': [0.8386817574501038, 0.8257114887237549, 0.8201805353164673, 0.8141834139823914, 0.8117470741271973, 0.7889001369476318, 0.7845691442489624, 0.7840442657470703, 0.7679340243339539, 0.7661229372024536, 0.7646892666816711, 0.7577080130577087, 0.7523895502090454, 0.7520655393600464, 0.7515712976455688, 0.7481311559677124, 0.7479628920555115, 0.7460651397705078, 0.7458067536354065, 0.7423197627067566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0723695755004883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.115954875946045})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3017864227294922})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.241204023361206})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7896, 'crossentropy': 0.97650576171875}
store['active_learning_steps'][5]['acquisition']={'indices': [49537, 125, 670, 5679, 3791, 13588, 3719, 55128, 45161, 30738, 47741, 24533, 49354, 36508, 56213, 34122, 19298, 16084, 39662, 23190], 'labels': [2, -1, 3, 3, 2, 8, 2, 8, 8, 8, 5, 8, 0, 5, 2, 5, 6, 5, 8, 8], 'scores': [0.7419954538345337, 0.7354490160942078, 0.7345888614654541, 0.7208539247512817, 0.7197586297988892, 0.6961368322372437, 0.6906948685646057, 0.6884006261825562, 0.6820131540298462, 0.6785333156585693, 0.6766839623451233, 0.6762920618057251, 0.6745327115058899, 0.6745156645774841, 0.6695519685745239, 0.6687443852424622, 0.6675888299942017, 0.6673134565353394, 0.6659688353538513, 0.6650779247283936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1743764877319336})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.083526372909546})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0824103355407715})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2627158164978027})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.264749526977539})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2695749998092651})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8405, 'crossentropy': 0.99021455078125}
store['active_learning_steps'][6]['acquisition']={'indices': [37237, 609, 37849, 54875, 53187, 58286, 8459, 8725, 711, 41269, 27831, 35507, 30441, 27629, 35168, 38311, 24711, 5429, 17457, 3331], 'labels': [1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'scores': [1.1095792055130005, 1.1073951721191406, 1.1073196530342102, 1.1051334738731384, 1.1039894819259644, 1.1024816632270813, 1.0997756123542786, 1.0981441736221313, 1.092099368572235, 1.0905613899230957, 1.0891047716140747, 1.085847020149231, 1.0851063132286072, 1.0798562169075012, 1.0751879215240479, 1.0740669965744019, 1.0734556913375854, 1.0700379610061646, 1.0674511790275574, 1.0658630728721619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.0921475887298584})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0993252992630005})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1757972240447998})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0429210662841797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0965632200241089})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2320153713226318})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3309831619262695})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8698, 'crossentropy': 0.86441396484375}
store['active_learning_steps'][7]['acquisition']={'indices': [42703, 23059, 2385, 16039, 41367, 46116, 39834, 17043, 39333, 49499, 16053, 44109, 59919, 5821, 38647, 18031, 6540, 22763, 37305, 30047], 'labels': [0, 1, 9, 9, 7, 2, 9, 1, 9, 1, 9, 1, 1, 7, 9, 4, 2, 6, 1, 1], 'scores': [1.0845775604248047, 1.0741634368896484, 1.029506266117096, 1.0294076204299927, 1.0234764218330383, 1.0205446481704712, 1.0175417065620422, 1.0168054103851318, 1.0163325071334839, 1.016068547964096, 1.0154801607131958, 1.0150237083435059, 1.0129945874214172, 1.0119829177856445, 1.0114977359771729, 1.0112115740776062, 1.0082575678825378, 1.0031880140304565, 1.0029941499233246, 1.0021241903305054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0297707319259644})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8274927139282227})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.760800838470459})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9280853271484375})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8186150193214417})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9600350856781006})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.640164892578125}
store['active_learning_steps'][8]['acquisition']={'indices': [7596, 26415, 58258, 47473, 19021, 50343, 31557, 51286, 39453, 21307, 25014, 17299, 52247, 16045, 57769, 42153, 57575, 36894, 10992, 26686], 'labels': [4, 0, 7, 0, 6, 6, -1, 0, 2, 4, 4, -1, 0, 0, -1, 0, 0, 0, -1, 0], 'scores': [1.0354134440422058, 0.971434473991394, 0.9382880330085754, 0.9355529546737671, 0.9352670907974243, 0.9320124387741089, 0.9310269355773926, 0.9246861934661865, 0.9246631860733032, 0.9241913557052612, 0.9221221208572388, 0.921376645565033, 0.9189128875732422, 0.9145106077194214, 0.9140973091125488, 0.9082897305488586, 0.9056581258773804, 0.9028759002685547, 0.9017825126647949, 0.901739239692688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.916869580745697})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8790433406829834})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8142923712730408})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7877655029296875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9450160264968872})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7489691972732544})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8745529651641846})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9435080289840698})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9550315141677856})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.652303125}
store['active_learning_steps'][9]['acquisition']={'indices': [39585, 34328, 37696, 42746, 32323, 23350, 18003, 24278, 35276, 29723, 51722, 19557, 42121, 47297, 22853, 38920, 41133, 35654, 37129, 48349], 'labels': [8, 8, 2, 2, 5, 8, 2, 3, 5, 5, 4, 8, 5, 8, 8, 7, 8, 1, 8, 2], 'scores': [1.0952243208885193, 1.0590358972549438, 1.0367543697357178, 1.021226406097412, 1.0185197591781616, 1.013164758682251, 1.0120407342910767, 1.0042647123336792, 1.0022110342979431, 1.0013059377670288, 0.9988111257553101, 0.9983013272285461, 0.9863759279251099, 0.980695903301239, 0.9783133864402771, 0.9758491516113281, 0.9749883413314819, 0.9743660092353821, 0.9697113633155823, 0.9694027304649353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8700615167617798})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5702379941940308})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.566190242767334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6504848003387451})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6119718551635742})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5487133264541626})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5794970989227295})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6283456087112427})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6339861154556274})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9357, 'crossentropy': 0.4878294921875}
store['active_learning_steps'][10]['acquisition']={'indices': [47914, 8812, 20037, 22470, 34520, 31706, 9614, 31301, 13942, 51845, 27477, 9118, 20989, 15190, 45516, 14735, 57523, 14843, 14787, 11569], 'labels': [0, 0, 8, 5, 6, 8, 9, 5, 4, 0, 0, 9, 3, 6, 1, 9, 3, 9, 9, 5], 'scores': [1.0572320818901062, 1.026989221572876, 1.012856364250183, 1.005338966846466, 1.0045923590660095, 1.0001593828201294, 0.9916521906852722, 0.9812601804733276, 0.9752718806266785, 0.9728276431560516, 0.9683265388011932, 0.9677700996398926, 0.963456392288208, 0.9634395241737366, 0.9577009677886963, 0.9572585225105286, 0.9570514559745789, 0.9538800716400146, 0.9519727230072021, 0.9505011141300201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8406832218170166})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5986543893814087})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5473674535751343})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5841675996780396})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5321134328842163})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5385380983352661})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5140067934989929})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5838550329208374})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.608428955078125})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5930260419845581})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.941, 'crossentropy': 0.463010009765625}
store['active_learning_steps'][11]['acquisition']={'indices': [34640, 17005, 17296, 41295, 39818, 49493, 39480, 30214, 38698, 20859, 1075, 18398, 34758, 44998, 31114, 43042, 32880, 1518, 52089, 27448], 'labels': [1, 1, 9, 9, 1, 8, 9, 1, 5, 8, 7, 4, 8, 4, 4, 8, 0, 9, 7, 9], 'scores': [1.0525994896888733, 1.0211305618286133, 1.0184210538864136, 1.0145928263664246, 1.0117498636245728, 1.001592993736267, 1.0007736682891846, 0.992531418800354, 0.9807384610176086, 0.9783058762550354, 0.9695606827735901, 0.9665801525115967, 0.963287353515625, 0.955388754606247, 0.9543922543525696, 0.9518992304801941, 0.9516343474388123, 0.9506752490997314, 0.9453620612621307, 0.94172203540802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9488112330436707})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5892138481140137})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.534119725227356})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5644057989120483})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5568537712097168})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5216702818870544})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5203461647033691})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6690076589584351})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6673674583435059})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6184216737747192})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9389, 'crossentropy': 0.455004931640625}
store['active_learning_steps'][12]['acquisition']={'indices': [59401, 32776, 58022, 37060, 59390, 22272, 28293, 3456, 39943, 13195, 13259, 50743, 31345, 45666, 14722, 3694, 24360, 31637, 30418, 5936], 'labels': [4, 4, 1, 9, 2, 5, 2, 1, 4, -1, 1, 7, 3, 1, 0, -1, 2, 5, 8, 4], 'scores': [1.0578553080558777, 1.0358128547668457, 1.0125563740730286, 1.0083787441253662, 1.0036338567733765, 0.994591236114502, 0.9943096041679382, 0.9926928877830505, 0.9851358532905579, 0.9842623472213745, 0.975284218788147, 0.9692484140396118, 0.958685040473938, 0.9568352699279785, 0.9558826684951782, 0.9513777494430542, 0.9482408165931702, 0.9482268691062927, 0.9478983283042908, 0.9460232257843018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0907199382781982})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6572730541229248})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5178859233856201})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5601971745491028})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5541324019432068})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6055864095687866})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.48786748046875}
store['active_learning_steps'][13]['acquisition']={'indices': [14307, 36810, 33057, 39449, 49525, 31512, 32301, 27898, 52937, 5842, 22513, 26528, 52938, 33162, 40466, 18042, 59314, 11711, 31065, 52306], 'labels': [7, 6, 7, 7, 8, 2, 4, 2, 7, 1, 7, 7, 2, 8, 8, 0, 9, 2, -1, 8], 'scores': [0.8446664810180664, 0.8218728303909302, 0.8137705326080322, 0.8120869994163513, 0.8063719272613525, 0.8036746978759766, 0.7964388132095337, 0.7953611016273499, 0.79384446144104, 0.7890499830245972, 0.7886513471603394, 0.7861137390136719, 0.7800995111465454, 0.7797064781188965, 0.777873158454895, 0.7773599624633789, 0.775928258895874, 0.7733551859855652, 0.7729213237762451, 0.7700307369232178]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9792229533195496})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5960994362831116})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5727908611297607})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4965045154094696})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49307286739349365})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5231946706771851})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5414668917655945})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5005382299423218})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.42096005859375}
store['active_learning_steps'][14]['acquisition']={'indices': [20171, 59726, 39942, 55496, 7949, 23027, 32702, 7638, 16043, 16909, 14394, 25310, 33892, 27514, 32640, 33364, 8883, 13021, 25332, 53309], 'labels': [5, 5, 9, 9, -1, -1, 5, 8, 0, 2, 3, 1, 5, 4, 2, 2, 2, 5, 2, 5], 'scores': [1.0578165650367737, 0.9939203858375549, 0.9866303205490112, 0.9524851441383362, 0.9514099955558777, 0.9290437698364258, 0.9205105900764465, 0.9203272461891174, 0.9116870760917664, 0.906392902135849, 0.9024194478988647, 0.8925485610961914, 0.8921756744384766, 0.8849105834960938, 0.8810876607894897, 0.880946159362793, 0.878337562084198, 0.8768286108970642, 0.8749578595161438, 0.8744747340679169]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1249477863311768})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6800349950790405})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5415763854980469})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5031139850616455})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5455113649368286})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47567272186279297})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5400636196136475})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5588415861129761})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5578218698501587})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.938, 'crossentropy': 0.42509072265625}
store['active_learning_steps'][15]['acquisition']={'indices': [48360, 18324, 34765, 43574, 30872, 47626, 46580, 6012, 29530, 4123, 33301, 43897, 34828, 20206, 52140, 56014, 52889, 39595, 29002, 6309], 'labels': [3, 0, 6, 5, 2, -1, 6, -1, 4, -1, -1, 1, -1, 7, 4, 5, -1, -1, 7, 3], 'scores': [0.9126015305519104, 0.900847315788269, 0.8910585045814514, 0.8858268857002258, 0.885786771774292, 0.8817828893661499, 0.8815736770629883, 0.8786298632621765, 0.8773297071456909, 0.8772532939910889, 0.8706024289131165, 0.8688209056854248, 0.8686316609382629, 0.8650045394897461, 0.8648746013641357, 0.863423228263855, 0.8609799146652222, 0.8605626225471497, 0.8582934141159058, 0.8577259182929993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.050735592842102})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5786263942718506})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49088433384895325})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42949551343917847})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4031045734882355})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47044700384140015})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4518919587135315})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4710102677345276})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.36971943359375}
store['active_learning_steps'][16]['acquisition']={'indices': [28633, 5443, 53872, 47626, 1674, 30900, 50370, 36744, 37048, 14896, 26072, 39355, 40398, 44095, 24479, 35401, 48010, 27458, 37583, 34406], 'labels': [3, -1, 8, -1, 9, 5, 7, 1, 9, 8, 1, 8, -1, 2, 8, 3, 7, 2, -1, 4], 'scores': [0.9396132826805115, 0.9255198240280151, 0.9179372787475586, 0.9176101684570312, 0.9146276116371155, 0.9086360931396484, 0.9077871441841125, 0.8988698720932007, 0.8910173177719116, 0.888536274433136, 0.8877348303794861, 0.8783169388771057, 0.875353217124939, 0.8688852787017822, 0.8669828772544861, 0.8654069304466248, 0.8651300668716431, 0.8644695281982422, 0.8567851185798645, 0.8508592247962952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0120511054992676})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6176025867462158})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5068991184234619})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4872167706489563})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47758615016937256})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.485418438911438})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5114704966545105})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5758669376373291})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.423934326171875}
store['active_learning_steps'][17]['acquisition']={'indices': [37469, 28512, 53990, 32276, 36409, 40624, 25462, 17382, 51764, 17079, 36704, 9383, 7720, 31738, 50317, 2148, 26405, 5790, 16488, 33301], 'labels': [2, 5, -1, 3, 3, -1, 6, 6, 5, 6, 2, 2, -1, 8, 3, 6, 9, 2, 9, -1], 'scores': [0.9417988657951355, 0.9109318852424622, 0.8906127214431763, 0.8904067873954773, 0.877504825592041, 0.8751354813575745, 0.8659685850143433, 0.8649450540542603, 0.8603941798210144, 0.8575489521026611, 0.8568603992462158, 0.8458991646766663, 0.8432285785675049, 0.8426561951637268, 0.8383153080940247, 0.8344868421554565, 0.8336781859397888, 0.8271943032741547, 0.825961172580719, 0.8189316987991333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0532710552215576})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6434937715530396})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5324162244796753})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4640349745750427})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47232484817504883})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4711403250694275})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4412917196750641})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4385085999965668})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45758795738220215})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4774973690509796})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4744727611541748})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9502, 'crossentropy': 0.3920224365234375}
store['active_learning_steps'][18]['acquisition']={'indices': [30062, 47626, 36417, 28110, 56006, 7949, 37208, 2618, 42428, 52889, 36450, 44286, 42415, 52644, 1423, 8450, 26748, 46368, 59286, 2782], 'labels': [3, -1, 6, -1, 3, -1, 6, 7, 5, -1, 2, 8, 7, 7, 0, 3, 9, 8, 8, -1], 'scores': [1.0025049448013306, 1.0012295246124268, 0.9880906343460083, 0.9837390780448914, 0.9826938509941101, 0.9776597023010254, 0.9775575399398804, 0.971169501543045, 0.9649873375892639, 0.96455317735672, 0.9577066898345947, 0.9550172090530396, 0.9499704837799072, 0.9492509961128235, 0.9472131133079529, 0.9457995891571045, 0.9456523060798645, 0.9439548254013062, 0.9391434788703918, 0.9339897632598877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0369213819503784})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6281622648239136})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5631705522537231})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47910594940185547})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4298827052116394})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40943610668182373})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4013383090496063})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3960200548171997})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44023630023002625})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4842274785041809})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46911630034446716})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.362062353515625}
store['active_learning_steps'][19]['acquisition']={'indices': [53844, 5684, 50403, 1376, 5536, 966, 42559, 12650, 54401, 56512, 20110, 27296, 50371, 11029, 47068, 47626, 8447, 36196, 635, 30614], 'labels': [5, 6, -1, 7, 8, 3, -1, 5, -1, -1, 4, -1, 7, 0, 4, -1, 3, -1, 5, 1], 'scores': [0.9922304153442383, 0.9795970320701599, 0.9207640886306763, 0.917047917842865, 0.911404550075531, 0.9066156148910522, 0.9000530242919922, 0.8956709504127502, 0.8928420543670654, 0.8924345970153809, 0.8858458399772644, 0.8823972940444946, 0.878982663154602, 0.8770833015441895, 0.8765842318534851, 0.8757230043411255, 0.8704187273979187, 0.866631031036377, 0.8651619553565979, 0.8644654154777527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0823907852172852})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5813766717910767})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4682736396789551})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4268731474876404})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3926194906234741})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3787700831890106})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.431982159614563})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.401347815990448})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42005276679992676})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9523, 'crossentropy': 0.341006396484375}
store['active_learning_steps'][20]['acquisition']={'indices': [3470, 34946, 48681, 52294, 4822, 32668, 18598, 11074, 17855, 1239, 49563, 48460, 9472, 21601, 57728, 41608, 9552, 20150, 41933, 11621], 'labels': [2, 8, 2, 0, 4, 9, 9, 9, 6, 8, 8, 2, 2, 1, 9, -1, 0, 3, 5, 2], 'scores': [0.8645748496055603, 0.8481416702270508, 0.8478713035583496, 0.8441964983940125, 0.8392086029052734, 0.8214238286018372, 0.8213573694229126, 0.8119941353797913, 0.8112665414810181, 0.7999314069747925, 0.7954086065292358, 0.7924412488937378, 0.7906736731529236, 0.7902915477752686, 0.7893227338790894, 0.7855548858642578, 0.7854251265525818, 0.7845818996429443, 0.7802855968475342, 0.7771947383880615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1478089094161987})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7034664154052734})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4736849069595337})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48110145330429077})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4669739902019501})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37293171882629395})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4387178122997284})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4778752028942108})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43947142362594604})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9553, 'crossentropy': 0.33110986328125}
store['active_learning_steps'][21]['acquisition']={'indices': [52889, 11292, 40378, 39320, 37583, 10256, 5126, 50736, 25624, 39545, 8116, 49518, 33505, 53990, 59081, 18501, 39561, 26882, 52086, 38912], 'labels': [-1, 1, -1, 6, -1, 2, 6, -1, -1, -1, 0, -1, 2, -1, -1, 4, 2, 7, 5, -1], 'scores': [0.8998733758926392, 0.8940657377243042, 0.8659887313842773, 0.8533141016960144, 0.8379296064376831, 0.8280274868011475, 0.8253828287124634, 0.8249929547309875, 0.8194018602371216, 0.8164540529251099, 0.8118230104446411, 0.8083091974258423, 0.8081036806106567, 0.8057413101196289, 0.8001942038536072, 0.7996692061424255, 0.7982364892959595, 0.7980551719665527, 0.7976648807525635, 0.7931463718414307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2202692031860352})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6732124090194702})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4356284439563751})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4928419589996338})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4200853705406189})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.408748060464859})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3905564248561859})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.38376444578170776})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41827547550201416})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39592862129211426})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4061277508735657})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9532, 'crossentropy': 0.356715771484375}
store['active_learning_steps'][22]['acquisition']={'indices': [47626, 26738, 1160, 50930, 43112, 5052, 33318, 8006, 41293, 20169, 44013, 54858, 14546, 7434, 54813, 20287, 8207, 46734, 41713, 29376], 'labels': [-1, 4, 4, 0, -1, 0, 6, 4, 4, 4, 4, 3, 4, 6, -1, 4, 4, 4, 0, -1], 'scores': [0.9541482925415039, 0.9078019857406616, 0.9072856307029724, 0.9046803712844849, 0.9045528173446655, 0.8904757499694824, 0.8748384714126587, 0.8612109422683716, 0.857753574848175, 0.8562730550765991, 0.8531510829925537, 0.8515008091926575, 0.8504889011383057, 0.8456695675849915, 0.8402748107910156, 0.840000569820404, 0.8370347619056702, 0.8361073732376099, 0.8324746489524841, 0.8321017622947693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.216955304145813})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6349050998687744})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5201255083084106})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44160139560699463})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44161078333854675})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3959144949913025})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4033139944076538})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4079046845436096})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4638597369194031})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.3694448486328125}
store['active_learning_steps'][23]['acquisition']={'indices': [23730, 52808, 42136, 20476, 33752, 37588, 20709, 38171, 8704, 3644, 42504, 36256, 51863, 44698, 49242, 11572, 32250, 26240, 3694, 4153], 'labels': [3, 8, 0, 5, 1, 2, 8, 2, 1, 1, 8, 5, 9, 1, 7, 5, 2, 5, -1, 2], 'scores': [0.965623140335083, 0.9609789848327637, 0.9448001980781555, 0.9350994825363159, 0.9094445705413818, 0.9000322222709656, 0.8981767296791077, 0.8947339653968811, 0.8833989500999451, 0.8816254138946533, 0.8740314245223999, 0.8694539070129395, 0.867700457572937, 0.8654400110244751, 0.8622599244117737, 0.8605238199234009, 0.8593500852584839, 0.857464075088501, 0.8544430136680603, 0.8519048690795898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.094792127609253})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.587587833404541})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4168514609336853})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4229426383972168})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3777931034564972})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3660579323768616})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4062950611114502})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39807236194610596})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39663165807724})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.3051834228515625}
store['active_learning_steps'][24]['acquisition']={'indices': [43176, 34396, 45446, 24589, 4784, 22832, 3810, 11482, 54756, 17091, 15913, 12702, 36818, 3136, 22531, 8853, 52800, 32425, 54378, 31664], 'labels': [2, 3, 7, 8, 7, 0, 3, 8, 2, 4, 9, 3, 7, 6, 4, 2, 9, 4, 7, 3], 'scores': [0.8357487916946411, 0.8288827538490295, 0.8204936981201172, 0.811491072177887, 0.8096369504928589, 0.808106541633606, 0.8056450486183167, 0.8049330711364746, 0.8047177195549011, 0.8017823100090027, 0.7992475032806396, 0.7988364696502686, 0.7977814078330994, 0.7971293926239014, 0.7905625104904175, 0.7891672253608704, 0.7863562107086182, 0.7822405099868774, 0.781909167766571, 0.7814795970916748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1590043306350708})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7289881110191345})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5044973492622375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41201820969581604})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40269291400909424})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3758026957511902})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3963637351989746})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.320222944021225})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37766727805137634})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3622008264064789})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3935670256614685})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.283012939453125}
