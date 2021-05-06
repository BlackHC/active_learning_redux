store = {}
store['timestamp']=1620258234
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=9']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=9
store['worker_id']=9
store['num_workers']=40
store['config']={'seed': 11, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.599018096923828})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.039743423461914})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.129556179046631})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.5468454360961914})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6579, 'crossentropy': 2.2578328125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 12268], ['id', 39531], ['ood', 53377], ['id', 23042], ['id', 56103], ['id', 24075], ['id', 57839], ['id', 9346], ['id', 52971], ['id', 878]], 'labels': [8, 0, 3, 9, 0, 0, 7, 9, 2, 3], 'scores': [0.8479141592979431, 1.04454505443573, 0.57038414478302, 0.7765188217163086, 0.8646632432937622, 0.9729461073875427, 0.833530068397522, 1.0095881819725037, 0.991726279258728, 0.5693739056587219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.7533156871795654})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.1241769790649414})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.2981040477752686})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.5242700576782227})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6852, 'crossentropy': 1.7099271484375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 56652], ['id', 28485], ['id', 53332], ['id', 52090], ['id', 26635], ['id', 51835], ['id', 28497], ['id', 7842], ['id', 7845], ['id', 5618]], 'labels': [7, 3, 3, 8, 2, 2, 6, 5, 5, 2], 'scores': [0.5081056356430054, 0.8011834025382996, 0.6918783187866211, 0.7113258838653564, 0.6832998991012573, 0.729308009147644, 0.6515386700630188, 0.7045464515686035, 0.7610410451889038, 0.7265645265579224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4971923828125})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.645829200744629})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.7739050388336182})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8418147563934326})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7387, 'crossentropy': 1.38937060546875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 53109], ['id', 40025], ['id', 2772], ['id', 16200], ['id', 29886], ['id', 5309], ['id', 8048], ['id', 7839], ['id', 10173], ['id', 31349]], 'labels': [4, 4, 4, 2, 8, 5, 3, 2, 5, 3], 'scores': [0.7961455583572388, 0.7757631540298462, 0.5269784927368164, 0.6779612302780151, 0.7817938327789307, 0.6891411542892456, 0.8467326164245605, 0.9809615015983582, 0.64777672290802, 0.6834729909896851]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.348473072052002})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5376605987548828})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4053425788879395})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.6784089803695679})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7701, 'crossentropy': 1.1737677734375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 25156], ['id', 55372], ['id', 32572], ['id', 40575], ['id', 55764], ['id', 19372], ['id', 50320], ['id', 52638], ['id', 47619], ['id', 12497]], 'labels': [2, 6, 6, 3, 8, 7, 5, 9, 0, 0], 'scores': [0.507033109664917, 0.5346149206161499, 0.7126318216323853, 0.680630087852478, 0.5270997285842896, 0.6118833422660828, 0.798301100730896, 0.5514671206474304, 0.7066678404808044, 0.618985116481781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0284727811813354})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.181734561920166})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.182678461074829})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3100608587265015})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.812, 'crossentropy': 0.96150576171875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 53171], ['id', 44604], ['id', 10586], ['id', 17370], ['id', 33041], ['id', 37060], ['id', 39768], ['id', 26372], ['id', 27225], ['ood', 52640]], 'labels': [7, 8, 5, 7, 9, 9, 3, 6, 7, 5], 'scores': [0.4888368844985962, 0.5242574214935303, 0.4379239082336426, 0.5914475321769714, 0.7321616411209106, 0.4475562572479248, 0.580761730670929, 0.674075186252594, 0.6098572015762329, 0.5403356552124023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9727860689163208})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0232970714569092})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.087303638458252})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.2465150356292725})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8137, 'crossentropy': 0.89048994140625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 5934], ['id', 3739], ['id', 52708], ['id', 13895], ['id', 34332], ['id', 38698], ['id', 14373], ['id', 36473], ['id', 11550], ['id', 31656]], 'labels': [5, 4, 4, 8, 9, 5, 2, 8, 9, 8], 'scores': [0.5998418927192688, 0.6204662322998047, 0.5622172951698303, 0.5391477346420288, 0.7158187627792358, 0.6676969528198242, 0.5673472881317139, 0.5026460886001587, 0.5275802612304688, 0.5843585133552551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8043485283851624})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6985170841217041})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8211863040924072})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8877257108688354})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8793967366218567})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8709, 'crossentropy': 0.682850634765625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 37829], ['id', 43072], ['id', 25632], ['id', 13905], ['id', 31020], ['id', 59229], ['id', 16022], ['id', 2636], ['id', 56612], ['ood', 55344]], 'labels': [6, 8, 2, 7, 0, 3, 8, 8, 2, 5], 'scores': [0.6707963943481445, 0.7594707012176514, 0.6244091391563416, 0.7184703946113586, 0.5141555070877075, 0.7414520978927612, 0.9095004796981812, 0.8986412882804871, 0.7547231316566467, 0.45800256729125977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9013786315917969})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8696616888046265})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8137680292129517})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9454302787780762})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0542755126953125})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9300180673599243})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8733, 'crossentropy': 0.737895654296875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 42140], ['id', 42108], ['id', 38172], ['id', 22102], ['id', 45666], ['id', 42838], ['id', 47828], ['id', 32348], ['id', 27344], ['id', 52887]], 'labels': [3, 5, 6, 5, 1, 9, 5, 5, 9, 1], 'scores': [0.7959190011024475, 0.5729525089263916, 0.5608989596366882, 0.5718791484832764, 0.7342122793197632, 0.7706199288368225, 0.9103886485099792, 0.9007513523101807, 0.4235800504684448, 0.6235997676849365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7913047075271606})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6481035947799683})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6939917802810669})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6980710029602051})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6436488628387451})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7196291089057922})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7329676151275635})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8304480314254761})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8986, 'crossentropy': 0.6529435546875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 56107], ['id', 30466], ['id', 14791], ['id', 10565], ['id', 44267], ['id', 53641], ['id', 1454], ['id', 53379], ['id', 40422], ['id', 30139]], 'labels': [7, 6, 8, 1, 8, 5, 0, 9, 5, 6], 'scores': [0.9930530488491058, 0.7194714248180389, 0.8479498624801636, 0.4568193256855011, 1.039456069469452, 0.7086256146430969, 0.6479385495185852, 0.9635365605354309, 0.5593523681163788, 0.669116199016571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7553925514221191})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6297869682312012})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7137254476547241})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6813915371894836})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7555087208747864})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.553205029296875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 46034], ['id', 18223], ['id', 56134], ['id', 48407], ['id', 11113], ['id', 11545], ['id', 32724], ['id', 53131], ['id', 39034], ['id', 21304]], 'labels': [8, 4, 3, 8, 4, 3, 5, 8, 9, 4], 'scores': [0.909281313419342, 0.3975594639778137, 0.40378740429878235, 0.6523879170417786, 0.7384583353996277, 0.5206267833709717, 0.4464558959007263, 0.7013944387435913, 0.6054746508598328, 0.7480688691139221]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.708157479763031})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.572989821434021})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5425745248794556})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6072465181350708})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5676742196083069})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6166830658912659})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.485177001953125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 59297], ['id', 22937], ['id', 7325], ['id', 22545], ['id', 33949], ['id', 58776], ['id', 9782], ['id', 32447], ['id', 41464], ['id', 57523]], 'labels': [1, 1, 0, 1, 1, 8, 8, 1, 8, 3], 'scores': [0.8096162676811218, 0.8379389047622681, 0.6622093915939331, 0.8021110892295837, 0.39598768949508667, 0.7374991774559021, 0.708554744720459, 0.7993308901786804, 0.637467622756958, 0.8009048104286194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.787405252456665})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5569414496421814})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5329506397247314})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6065382361412048})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5501421689987183})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5687785148620605})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.49484169921875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 33162], ['id', 5790], ['id', 43015], ['id', 44301], ['id', 14580], ['id', 5042], ['id', 23386], ['id', 40712], ['id', 22229], ['id', 15538]], 'labels': [8, 2, 4, 4, 9, 8, 7, 7, 2, 5], 'scores': [0.9524126052856445, 0.7861904501914978, 0.6680084466934204, 0.6681955456733704, 0.7789466381072998, 0.5243839621543884, 0.7256754040718079, 0.6933441758155823, 0.9130827188491821, 0.8014723062515259]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7801599502563477})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5704364776611328})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5682103037834167})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5391741991043091})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.564467191696167})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5771583318710327})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.555120587348938})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.470587060546875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 22481], ['id', 19302], ['id', 16922], ['id', 37339], ['id', 12137], ['id', 54743], ['id', 37712], ['id', 10570], ['id', 29560], ['id', 5905]], 'labels': [7, 3, 3, 4, 5, 9, 4, 2, 0, 0], 'scores': [0.7367085814476013, 0.6361033916473389, 0.6431124210357666, 0.6870324611663818, 0.68904709815979, 0.619964212179184, 0.8653833270072937, 0.7045825123786926, 0.7138057947158813, 0.8117859959602356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8249998092651367})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5252835750579834})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5319949388504028})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5982376337051392})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5705246925354004})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.52257177734375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 14484], ['id', 20637], ['id', 21880], ['id', 2856], ['id', 10514], ['id', 39305], ['id', 54264], ['id', 25287], ['id', 11084], ['id', 37080]], 'labels': [2, 6, 2, 4, 2, 7, 4, 1, 2, 4], 'scores': [0.6904060244560242, 0.6228728294372559, 0.7623264193534851, 0.846627414226532, 0.5133769512176514, 0.7817274332046509, 0.6479475498199463, 0.650261640548706, 0.8018582463264465, 0.38773804903030396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8064569234848022})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5673443675041199})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4602457284927368})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4768967032432556})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5024133324623108})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5515441298484802})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.4279181640625}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 3094], ['id', 52828], ['id', 28014], ['id', 25910], ['id', 37116], ['id', 40167], ['id', 25803], ['id', 17472], ['id', 36716], ['id', 58832]], 'labels': [8, 3, 7, 1, 1, 9, 0, 1, 3, 3], 'scores': [0.7735452651977539, 0.5802835822105408, 0.6690661311149597, 0.8078932166099548, 0.6042178869247437, 0.5487694144248962, 0.8841204643249512, 0.6613075733184814, 0.6450168490409851, 0.7316654920578003]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.813685417175293})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5470740795135498})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4780990481376648})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.529965341091156})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4961823523044586})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5366432666778564})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.426140478515625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 3791], ['ood', 23646], ['id', 25157], ['id', 11600], ['id', 45048], ['id', 7196], ['id', 57575], ['id', 41700], ['id', 38069], ['ood', 54528]], 'labels': [2, 5, 2, 2, 4, 2, 0, 7, 8, 1], 'scores': [1.0575357675552368, 0.63796067237854, 0.7200566530227661, 0.7591320872306824, 0.8121601343154907, 0.6155558824539185, 0.6852951049804688, 0.7184731960296631, 0.5946141481399536, 0.35948455333709717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8269633650779724})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5037581920623779})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.440838098526001})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48375236988067627})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4586222767829895})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47582826018333435})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9432, 'crossentropy': 0.3841899169921875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 2278], ['id', 28512], ['id', 23035], ['id', 9628], ['id', 10744], ['id', 17153], ['id', 46368], ['ood', 6482], ['id', 27197], ['id', 24311]], 'labels': [0, 5, 8, 1, 7, 2, 8, 0, 8, 8], 'scores': [0.47578251361846924, 0.7611740231513977, 0.443240225315094, 0.406406044960022, 0.7369069457054138, 0.6807025671005249, 0.7096773982048035, 0.444277286529541, 0.5891185402870178, 0.5620401501655579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8851045370101929})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4621186852455139})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40950167179107666})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42804527282714844})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4532458782196045})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44662564992904663})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.365284228515625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 34743], ['id', 41537], ['id', 7833], ['id', 36471], ['id', 36732], ['id', 13373], ['id', 21990], ['id', 43537], ['id', 4666], ['id', 40304]], 'labels': [9, 3, 5, 3, 3, 6, 1, 3, 5, 6], 'scores': [0.6490864753723145, 0.8493354320526123, 0.9624921679496765, 0.6410326957702637, 0.5002384185791016, 0.37923020124435425, 0.6375594139099121, 0.709426760673523, 0.5074682831764221, 0.6816706657409668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8777283430099487})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4567554295063019})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3797333240509033})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3880276083946228})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39056503772735596})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4388583302497864})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9513, 'crossentropy': 0.3574700927734375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 38718], ['id', 54002], ['id', 7510], ['id', 14896], ['id', 2801], ['ood', 35320], ['id', 4784], ['id', 56220], ['id', 45516], ['id', 57665]], 'labels': [1, 5, 2, 8, 4, 5, 7, 7, 1, 8], 'scores': [0.6033918857574463, 0.5793654918670654, 0.7158722281455994, 0.7360484004020691, 0.5443992018699646, 0.3752812147140503, 0.5743533968925476, 0.5596165657043457, 0.6431159377098083, 0.6899774670600891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9460177421569824})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.508811354637146})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4501228928565979})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43073922395706177})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4614076614379883})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45064863562583923})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47424203157424927})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9438, 'crossentropy': 0.3650514404296875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 18824], ['id', 11787], ['id', 36760], ['id', 14825], ['id', 46524], ['id', 10091], ['id', 11096], ['id', 9608], ['id', 28930], ['id', 8765]], 'labels': [7, 6, 7, 3, 6, 3, 9, 8, 7, 3], 'scores': [0.6252089738845825, 0.4674282670021057, 0.811771035194397, 0.671751081943512, 0.7715772390365601, 0.518006443977356, 0.6631351709365845, 0.6110950708389282, 0.5603467226028442, 0.7067280411720276]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9570862054824829})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47665679454803467})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45545974373817444})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3977929353713989})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37949904799461365})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41714388132095337})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3908199071884155})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49591732025146484})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9505, 'crossentropy': 0.3381778076171875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 17129], ['id', 45972], ['id', 9948], ['id', 32195], ['id', 19642], ['id', 23578], ['id', 13259], ['id', 35736], ['id', 52666], ['id', 46285]], 'labels': [1, 2, 8, 7, 7, 2, 1, 6, 7, 8], 'scores': [0.6383458375930786, 0.6181010007858276, 0.8505040407180786, 0.5356796979904175, 0.6347178220748901, 0.6590625047683716, 0.7929207682609558, 0.6012235879898071, 0.6335265636444092, 0.7513406872749329]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9382027387619019})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4460639953613281})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3966265916824341})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4143249988555908})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.376544713973999})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3806478977203369})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37985312938690186})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3903339207172394})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.3099380126953125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 54814], ['id', 43548], ['id', 5402], ['id', 52624], ['id', 8780], ['id', 16031], ['id', 11675], ['id', 43547], ['id', 1814], ['id', 34829]], 'labels': [4, 8, 9, 1, 8, 0, 0, 2, 4, 5], 'scores': [0.7857241630554199, 0.695077121257782, 0.6956446170806885, 0.7621662616729736, 0.7756731510162354, 0.6734610199928284, 0.8138166666030884, 0.8473787307739258, 0.8490447998046875, 0.7403373122215271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9571951627731323})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4898056983947754})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38342005014419556})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3985115587711334})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41846978664398193})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.407055526971817})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.3524053955078125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 37078], ['id', 18487], ['id', 26722], ['id', 21598], ['id', 7270], ['id', 49537], ['id', 42491], ['id', 36363], ['id', 53470], ['id', 32202]], 'labels': [8, 4, 0, 2, 5, 2, 2, 6, 5, 2], 'scores': [0.7156040072441101, 0.7495985627174377, 0.5551363229751587, 0.6617878079414368, 0.6389179825782776, 0.7100470066070557, 0.5164953470230103, 0.6700741052627563, 0.37644970417022705, 0.42081236839294434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.874608039855957})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44600504636764526})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4441760778427124})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37754499912261963})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.381049245595932})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38277482986450195})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3646280765533447})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3786166310310364})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41363954544067383})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47522836923599243})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9509, 'crossentropy': 0.3222988525390625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 50025], ['ood', 12635], ['id', 48772], ['id', 37065], ['id', 32747], ['id', 42167], ['id', 35464], ['id', 4842], ['id', 56914], ['id', 40589]], 'labels': [3, 2, 6, 3, 8, 4, 9, 7, 0, 2], 'scores': [0.8380517959594727, 0.40439867973327637, 0.4818422794342041, 0.6857354640960693, 0.9199591875076294, 0.5130856037139893, 0.6306098103523254, 0.7489641904830933, 0.7711875438690186, 0.8950721025466919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9816453456878662})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5039141178131104})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42037683725357056})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4044618606567383})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3590749502182007})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3653027415275574})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3594540059566498})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37714967131614685})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.959, 'crossentropy': 0.3186745361328125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 49217], ['id', 6929], ['id', 1840], ['id', 42948], ['id', 52115], ['id', 37877], ['id', 59314], ['id', 13365], ['id', 55906], ['id', 5365]], 'labels': [8, 5, 4, 6, 8, 9, 9, 8, 2, 6], 'scores': [0.674201250076294, 0.6909610629081726, 0.8326187133789062, 0.7679691910743713, 0.77971351146698, 0.6954417824745178, 0.9819976091384888, 0.6496633887290955, 0.5392143130302429, 0.4425634741783142]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0488431453704834})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5382857322692871})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.359874963760376})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3572353720664978})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3477333188056946})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36421874165534973})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3678014874458313})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31707829236984253})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36744770407676697})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3599180579185486})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3627290725708008})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.2861440185546875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 6905], ['id', 18654], ['ood', 12837], ['id', 16193], ['id', 4761], ['ood', 27318], ['id', 29759], ['ood', 57522], ['id', 38990], ['id', 3108]], 'labels': [8, 4, 5, 3, 8, 3, 5, 0, 3, 3], 'scores': [0.7732341885566711, 0.6903291344642639, 0.4868454933166504, 0.69423708319664, 0.82094806432724, 0.5033718347549438, 0.6422995328903198, 0.5905865430831909, 0.6906606554985046, 0.7772183418273926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.106500267982483})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5017382502555847})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39205020666122437})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3416086435317993})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3517296314239502})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3358849883079529})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33572036027908325})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34986233711242676})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3373871147632599})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3983894884586334})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.2769056640625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 51232], ['id', 22272], ['id', 52713], ['id', 59747], ['id', 19396], ['id', 23788], ['id', 22531], ['id', 34328], ['id', 51764], ['id', 36152]], 'labels': [6, 5, 3, 5, 5, 1, 4, 8, 5, 7], 'scores': [0.4800504446029663, 0.7542699575424194, 0.6310199499130249, 0.9471571445465088, 0.8857942819595337, 0.8186312317848206, 0.9410564303398132, 0.9733574390411377, 0.779940664768219, 0.6839519143104553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0496183633804321})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46389901638031006})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3670428395271301})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33202603459358215})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31891965866088867})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29495856165885925})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31745606660842896})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30089086294174194})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29377642273902893})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31717029213905334})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.316494882106781})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32690662145614624})
store['active_learning_steps'][27]['training']['best_epoch']=9
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.26530615234375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 1682], ['id', 49515], ['id', 8867], ['id', 37758], ['id', 39516], ['id', 7920], ['id', 28674], ['id', 41299], ['id', 42384], ['id', 14015]], 'labels': [0, 2, 8, 0, 5, 2, 9, 3, 8, 9], 'scores': [0.8856775164604187, 0.7192771434783936, 0.7954113483428955, 0.8413597345352173, 0.8897987604141235, 0.7469494342803955, 0.7501109838485718, 0.6948967576026917, 0.7624313831329346, 0.8241962194442749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9532790184020996})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5292230248451233})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3626430630683899})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37710320949554443})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3279690742492676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3397473692893982})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32305246591567993})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3070841133594513})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.319470077753067})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35850024223327637})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3108972907066345})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.2960783935546875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 2571], ['id', 12778], ['id', 11295], ['id', 15280], ['id', 29431], ['id', 31094], ['id', 10282], ['id', 57054], ['id', 36072], ['id', 14550]], 'labels': [5, 8, 0, 6, 8, 9, 3, 8, 2, 2], 'scores': [0.6880409419536591, 0.7718583047389984, 0.6373156905174255, 0.6472409069538116, 0.4136398732662201, 0.895050048828125, 0.7722311317920685, 0.5900098085403442, 0.9550724029541016, 0.6140505075454712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1584937572479248})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5807862281799316})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3768013119697571})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32365095615386963})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2874952554702759})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31134849786758423})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3051246702671051})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3340732753276825})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.2913267822265625}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 14629], ['ood', 52081], ['id', 27431], ['id', 55153], ['id', 13149], ['id', 23490], ['id', 34771], ['id', 50078], ['ood', 21765], ['ood', 23776]], 'labels': [0, 8, 5, 8, 7, 3, 0, 9, 8, 8], 'scores': [0.8315950036048889, 0.24063706398010254, 0.7601277232170105, 0.752351701259613, 0.6798967123031616, 0.7191193103790283, 0.6548668146133423, 0.8092776536941528, 0.5614564418792725, 0.3283653259277344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9924109578132629})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4473327696323395})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35704874992370605})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3293922245502472})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3110349178314209})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28524506092071533})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28570133447647095})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2916732430458069})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.324459433555603})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.272001025390625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 58599], ['id', 45520], ['id', 24284], ['id', 470], ['id', 56464], ['id', 10012], ['id', 18598], ['id', 50576], ['id', 30960], ['id', 24497]], 'labels': [0, 8, 3, 1, 9, 8, 9, 2, 3, 9], 'scores': [0.7932071685791016, 0.8431573510169983, 0.6921785473823547, 0.6856104731559753, 0.6337937116622925, 0.7749242186546326, 0.790530800819397, 0.5311803221702576, 0.6174663305282593, 0.5493782460689545]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1065001487731934})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5376083254814148})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39205652475357056})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3038538694381714})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2993963062763214})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3088843822479248})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32811421155929565})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3186665177345276})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.28725673828125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 58438], ['id', 47662], ['id', 33182], ['id', 18003], ['id', 14697], ['ood', 10520], ['id', 15191], ['id', 21058], ['id', 27317], ['id', 8093]], 'labels': [6, 9, 9, 2, 8, 0, 0, 5, 5, 0], 'scores': [0.5254819989204407, 0.8597726821899414, 0.704578697681427, 0.7151963114738464, 0.47811007499694824, 0.5681752562522888, 0.7511952519416809, 0.6393865942955017, 0.43914109468460083, 0.692467451095581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.104952335357666})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5163074731826782})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36871880292892456})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31751111149787903})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30821895599365234})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30902761220932007})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29615676403045654})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27623218297958374})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27567586302757263})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3028527498245239})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2929990291595459})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29686349630355835})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2587166259765625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 370], ['id', 331], ['id', 45116], ['id', 57465], ['id', 55844], ['id', 16706], ['id', 25766], ['id', 52600], ['id', 50916], ['id', 21532]], 'labels': [7, 6, 8, 7, 3, 4, 8, 4, 4, 5], 'scores': [0.690864086151123, 0.6400656402111053, 0.5301823019981384, 0.4358222484588623, 0.4850061386823654, 0.5874313712120056, 0.5825722813606262, 0.458204984664917, 0.7582736611366272, 0.7222796082496643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9713486433029175})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4702931046485901})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3448328673839569})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30517876148223877})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2801833748817444})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28394249081611633})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27037280797958374})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2871391177177429})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.279731810092926})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2893790602684021})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.266950048828125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 49200], ['id', 39672], ['id', 670], ['id', 11210], ['id', 57732], ['id', 42004], ['id', 9340], ['id', 57242], ['id', 46605], ['ood', 37432]], 'labels': [0, 7, 3, 8, 9, 7, 5, 5, 7, 5], 'scores': [0.5476439595222473, 0.6050813794136047, 0.8920642733573914, 0.3761351704597473, 0.8587827682495117, 0.772391140460968, 0.9077460765838623, 0.6688207983970642, 0.5667274594306946, 0.4141700267791748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0937671661376953})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5112177729606628})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3825574219226837})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33110737800598145})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30260100960731506})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30211353302001953})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27977627515792847})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2608008086681366})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27861714363098145})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2725818157196045})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2941340506076813})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.251691064453125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 43575], ['id', 52169], ['id', 41713], ['id', 18031], ['id', 37704], ['id', 18669], ['id', 10239], ['id', 45274], ['id', 23028], ['id', 26214]], 'labels': [2, 2, 0, 4, 8, 9, 1, 6, 2, 9], 'scores': [0.7534207701683044, 0.756475031375885, 0.7847711443901062, 0.7410248517990112, 0.8654587268829346, 0.6156385540962219, 0.7189691662788391, 0.7699859142303467, 0.6802218556404114, 0.8344313502311707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.1966902017593384})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5231956243515015})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40884363651275635})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32378464937210083})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3034181296825409})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27206915616989136})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2879485487937927})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2726020812988281})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26832759380340576})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2804467976093292})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2671545147895813})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2639366686344147})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2960124611854553})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2886428236961365})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29054713249206543})
store['active_learning_steps'][35]['training']['best_epoch']=12
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.24235810546875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 32668], ['id', 49014], ['id', 20905], ['id', 635], ['id', 6130], ['ood', 39074], ['id', 1357], ['id', 14872], ['id', 31562], ['id', 56204]], 'labels': [9, 0, 8, 5, 7, 0, 3, 8, 3, 3], 'scores': [1.084946095943451, 0.6929121017456055, 0.8767428696155548, 0.6047264933586121, 0.6821885704994202, 0.6996329426765442, 0.9463948607444763, 0.9703154563903809, 0.9460161626338959, 0.7023209929466248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.100682258605957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.495724081993103})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.345902681350708})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29724961519241333})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2866203188896179})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2571451961994171})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26208192110061646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2525535821914673})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25100821256637573})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28963714838027954})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26699963212013245})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2658616900444031})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9747, 'crossentropy': 0.22972666015625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 13376], ['id', 38316], ['id', 19844], ['id', 32481], ['id', 13588], ['id', 11753], ['id', 57728], ['id', 8443], ['id', 28710], ['id', 11737]], 'labels': [3, 4, 7, 2, 8, 8, 9, 2, 8, 2], 'scores': [0.5944034457206726, 0.7252358198165894, 0.7165952920913696, 0.6565614342689514, 0.6514798402786255, 0.6254956126213074, 0.974464476108551, 0.5289999842643738, 0.646790623664856, 0.5716630220413208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.114833950996399})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48990169167518616})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.406421422958374})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32231882214546204})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31187570095062256})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3151450753211975})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29326170682907104})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27816081047058105})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2858502268791199})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3031978905200958})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2969476580619812})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.256414892578125}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 45930], ['id', 33812], ['id', 6152], ['id', 38370], ['id', 11616], ['id', 38920], ['id', 15893], ['id', 4860], ['id', 12651], ['id', 30900]], 'labels': [7, 6, 8, 4, 7, 7, 5, 8, 9, 5], 'scores': [0.470278799533844, 0.8568720817565918, 0.8369464874267578, 0.4443216323852539, 0.6285848021507263, 0.5523025393486023, 0.6031151711940765, 0.5573393106460571, 0.7395715713500977, 0.7112088799476624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0802431106567383})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.49287134408950806})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3716166615486145})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3058720827102661})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31468141078948975})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29784759879112244})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26311740279197693})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2715981602668762})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2619098424911499})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2656169831752777})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26165688037872314})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31111735105514526})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.289256751537323})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2937309741973877})
store['active_learning_steps'][38]['training']['best_epoch']=11
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.24133837890625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 32492], ['id', 31046], ['id', 2550], ['id', 34520], ['id', 50562], ['id', 40208], ['id', 4820], ['id', 50572], ['id', 29530], ['id', 28633]], 'labels': [5, 6, 2, 6, 9, 0, 5, 1, 4, 3], 'scores': [0.48546117544174194, 0.6839926838874817, 0.753193199634552, 0.9858676791191101, 0.9834812879562378, 0.7683186531066895, 0.4895355999469757, 0.7642640471458435, 0.7053587436676025, 0.7054843604564667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2079048156738281})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6091917157173157})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3996394872665405})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33058714866638184})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33527228236198425})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2811112105846405})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2681228518486023})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26113203167915344})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.266899436712265})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25936612486839294})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3017496168613434})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29781171679496765})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32739078998565674})
store['active_learning_steps'][39]['training']['best_epoch']=10
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.2648115234375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 50896], ['id', 51394], ['id', 49890], ['id', 27766], ['id', 15076], ['id', 52086], ['id', 31345], ['id', 41377], ['id', 3136], ['id', 27026]], 'labels': [9, 8, 5, 9, 3, 5, 3, 9, 6, 2], 'scores': [0.7783128619194031, 0.5896002650260925, 0.7466710209846497, 0.510701447725296, 0.641752690076828, 0.8279902935028076, 0.5431004762649536, 0.40142345428466797, 0.6268174052238464, 0.3690897226333618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.2511097192764282})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.6066442728042603})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4255082607269287})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2870139479637146})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29540199041366577})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29058748483657837})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2870481312274933})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.3139798095703125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 14878], ['id', 20641], ['id', 44927], ['id', 42080], ['id', 38622], ['id', 1674], ['id', 24261], ['id', 39734], ['id', 41772], ['id', 59670]], 'labels': [3, 9, 7, 6, 4, 9, 8, 2, 5, 5], 'scores': [0.6692638397216797, 0.5724719762802124, 0.5982487797737122, 0.4072270393371582, 0.4302380681037903, 0.7060650587081909, 0.5022843480110168, 0.4764644503593445, 0.7510870695114136, 0.5248296856880188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0810080766677856})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5352304577827454})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3838217258453369})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2940126657485962})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2936832308769226})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2575947046279907})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2508929669857025})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2581482231616974})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2616170048713684})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24859371781349182})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2505025267601013})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2740323841571808})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2709026634693146})
store['active_learning_steps'][41]['training']['best_epoch']=10
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.2276173828125}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 28664], ['id', 52727], ['id', 33304], ['id', 26718], ['id', 52800], ['id', 55314], ['id', 21457], ['id', 25829], ['id', 52953], ['id', 34500]], 'labels': [8, 4, 7, 2, 9, 6, 8, 3, 2, 8], 'scores': [0.5552893280982971, 0.7390965223312378, 0.6800377368927002, 0.4200013279914856, 0.8088156580924988, 0.6426325440406799, 0.6100094318389893, 0.5940759181976318, 0.7013953328132629, 0.7262190580368042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2465301752090454})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6095774173736572})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3783873915672302})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3279092609882355})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30096349120140076})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25516000390052795})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28016361594200134})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2666282653808594})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2768516540527344})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.250541357421875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 46724], ['id', 11007], ['id', 15252], ['id', 36908], ['id', 9118], ['id', 48040], ['id', 23114], ['id', 44789], ['id', 20912], ['ood', 45569]], 'labels': [7, 7, 1, 1, 9, 1, 2, 8, 1, 9], 'scores': [0.46356460452079773, 0.5664491057395935, 0.627862811088562, 0.7242103815078735, 0.5981494784355164, 0.4572596549987793, 0.3918216824531555, 0.34694164991378784, 0.4481923580169678, 0.40587568283081055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1829662322998047})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6312268972396851})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4116091728210449})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3728131949901581})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29468995332717896})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29104724526405334})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28662675619125366})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2947372794151306})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29541295766830444})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28279221057891846})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28657156229019165})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2779483497142792})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29005664587020874})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29891419410705566})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28111332654953003})
store['active_learning_steps'][43]['training']['best_epoch']=12
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.260801220703125}
